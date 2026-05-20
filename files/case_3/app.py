"""
CASE 3: FOOD DELIVERY DEMAND PULSE
===================================
Interactive dashboard to analyze food delivery demand patterns
and show where surge pricing is being applied incorrectly.

For: Ops Head (decides rider incentives and surge policy)
"""
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path

st.set_page_config(page_title="Demand Pulse", layout="wide", page_icon="🍱")

# ========== LOAD DATA ==========
@st.cache_data
def load_data():
    """Load CSV and create time-based columns for analysis"""
    data_path = Path(__file__).resolve().parent / "case3_food_delivery_orders.csv"
    if not data_path.exists():
        raise FileNotFoundError(f"{data_path.name} not found next to app.py")

    df = pd.read_csv(data_path, parse_dates=["timestamp"])
    
    # Create hour, day, weekend flags for grouping
    df["hour"] = df.timestamp.dt.hour
    df["dow"] = df.timestamp.dt.dayofweek
    df["dow_name"] = df.timestamp.dt.day_name()
    df["date"] = df.timestamp.dt.date
    df["is_weekend"] = df.dow >= 5  # Saturday=5, Sunday=6
    return df

df = load_data()

# ========== HEADER & DESCRIPTION ==========
st.title("🍱 Demand Pulse — Food Delivery Surge Analysis")
st.caption(
    f"📊 Data: {len(df):,} orders from {df.timestamp.min().date()} to {df.timestamp.max().date()}"
)

# ========== FILTERS (SIDEBAR) ==========
st.sidebar.header("🔍 Filter Data")
st.sidebar.write("Choose which cities and cuisines to analyze:")

cities = st.sidebar.multiselect("Cities", sorted(df.city.unique()),
                                 default=sorted(df.city.unique()))
cuisines = st.sidebar.multiselect("Cuisines", sorted(df.cuisine.unique()),
                                   default=sorted(df.cuisine.unique()))
weekend = st.sidebar.radio("Day type", ["All days", "Weekdays only", "Weekends only"], 0)

# Apply filters
f = df[df.city.isin(cities) & df.cuisine.isin(cuisines)]
if weekend == "Weekdays only":
    f = f[~f.is_weekend]
elif weekend == "Weekends only":
    f = f[f.is_weekend]

# ========== KEY METRICS ==========
st.subheader("📈 Key Metrics")
c1, c2, c3, c4 = st.columns(4)
c1.metric("Total Orders", f"{len(f):,}")
c2.metric("Surge Rate", f"{f.surge_applied.mean():.1%}")
c3.metric("Avg Order Value", f"₹{f.order_value.mean():.0f}")
c4.metric("Median Delivery Time", f"{f.delivery_time_min.median():.0f} min")

# ---- Top KPIs ----
c1, c2, c3, c4 = st.columns(4)
c1.metric("Orders (filtered)", f"{len(f):,}")
c2.metric("Surge rate", f"{f.surge_applied.mean():.1%}")
c3.metric("Avg order value", f"₹{f.order_value.mean():.0f}")
c4.metric("Median delivery (min)", f"{f.delivery_time_min.median():.0f}")

# ---- Tab layout ----
tab1, tab2, tab3, tab4 = st.tabs(["🔥 Demand Heatmap",
                                   "🏙️ City Comparison",
                                   "⚡ Surge vs Demand",
                                   "📈 Forecast"])

with tab1:
    st.subheader("Where does demand actually peak?")
    heat = f.groupby(["dow", "hour"]).size().unstack(fill_value=0)
    heat.index = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    fig = px.imshow(
        heat.values, x=list(range(24)), y=heat.index,
        color_continuous_scale="YlOrRd", aspect="auto",
        labels=dict(x="Hour", y="Day", color="Orders"),
    )
    fig.update_layout(height=380, margin=dict(l=0, r=0, t=10, b=0))
    st.plotly_chart(fig, use_container_width=True)
    st.info(
        "**Reading this map:** Two clear bands — lunch 12–14 and dinner 19–22. "
        "Weekend evenings (Fri–Sun, 20–21) are darkest. The mid-afternoon "
        "(15–17) is NOT a peak, despite often being treated as one."
    )

with tab2:
    st.subheader("Do cities behave differently?")
    by_city_hour = (f.groupby(["city", "hour"]).size()
                      .reset_index(name="orders"))
    city_totals = f.groupby("city").size()
    by_city_hour["share"] = by_city_hour.apply(
        lambda r: r.orders / city_totals[r.city] * 100, axis=1
    )
    fig = px.line(by_city_hour, x="hour", y="share", color="city",
                  labels={"share": "% of city's orders", "hour": "Hour of day"},
                  markers=False)
    fig.update_layout(height=420, margin=dict(l=0, r=0, t=10, b=0))
    st.plotly_chart(fig, use_container_width=True)
    
    # Concentration table
    conc = pd.DataFrame({
        "share_evening_19_22": f.groupby("city").apply(
            lambda g: g.hour.between(19, 22).mean()).round(3),
        "share_lunch_12_14": f.groupby("city").apply(
            lambda g: g.hour.between(12, 14).mean()).round(3),
    }).sort_values("share_evening_19_22", ascending=False)
    st.dataframe(conc, use_container_width=True)
    st.info(
        "**Honest finding:** Cities are *more similar* than expected. "
        "Kolkata has a slightly stronger lunch share. That's the one to tailor."
    )

with tab3:
    st.subheader("Is surge firing where demand actually is?")
    slot = (f.groupby(["city", "date", "hour"])
              .agg(orders=("order_id", "size"),
                   surge_rate=("surge_applied", "mean"))
              .reset_index())
    slot["demand_decile"] = (slot.groupby("city")["orders"]
                                .transform(lambda x: pd.qcut(x, 10, labels=False,
                                                              duplicates="drop")))
    dec = (slot.groupby("demand_decile")
               .agg(slot_count=("orders", "size"),
                    avg_orders=("orders", "mean"),
                    avg_surge_rate=("surge_rate", "mean"))
               .reset_index())
    dec["surge_pct"] = (dec.avg_surge_rate * 100).round(1)
    
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=dec.demand_decile, y=dec.surge_pct,
        marker_color=["#cccccc"] * 7 + ["#f4a261"] + ["#e76f51"] * 2,
        text=dec.surge_pct.astype(str) + "%",
        textposition="outside",
    ))
    fig.update_layout(
        xaxis_title="Demand decile (within city, 0=lowest)",
        yaxis_title="Avg surge rate (%)",
        height=380, margin=dict(l=0, r=0, t=10, b=0),
        title="Surge rises with demand — but fires non-trivially even at bottom",
    )
    st.plotly_chart(fig, use_container_width=True)

    THRESHOLD = st.slider(
        "Legitimate-surge baseline for low-demand slots (%)",
        min_value=0, max_value=30, value=10, step=1,
        help="The surge rate we believe is 'legitimate' even in low-demand slots "
             "(genuine driver shortage etc.). Excess above this is removable."
    )
    bottom = slot[slot.demand_decile < 5]
    current_rate = bottom.surge_rate.mean()
    low_orders = bottom.orders.sum()
    excess_3mo = max(0, (current_rate - THRESHOLD/100) * low_orders)
    excess_monthly = excess_3mo / 3
    savings = excess_monthly * 40  # ₹40/surge order assumption
    
    cc1, cc2, cc3 = st.columns(3)
    cc1.metric("Current low-demand surge rate", f"{current_rate:.1%}")
    cc2.metric("Removable excess surge orders/month", f"{excess_monthly:,.0f}")
    cc3.metric("Estimated savings/month", f"₹{savings:,.0f}",
               help="Assumes ₹40 surge cost per order")

with tab4:
    st.subheader("Short-horizon demand forecast — pick a city")
    city = st.selectbox("City", sorted(f.city.unique()), index=0)
    sub = f[f.city == city]
    hourly = (sub.set_index("timestamp")
                 .resample("h").size().rename("orders").to_frame())
    hourly["hour"] = hourly.index.hour
    hourly["dow"] = hourly.index.dayofweek
    
    test_start = hourly.index.max() - pd.Timedelta(days=7) + pd.Timedelta(hours=1)
    train = hourly.loc[hourly.index < test_start].copy()
    test = hourly.loc[hourly.index >= test_start].copy()
    sn_lookup = (train.groupby(["dow", "hour"]).orders.mean()
                       .rename("forecast").reset_index())
    test_idx = test.reset_index().merge(sn_lookup, on=["dow", "hour"], how="left")
    test["forecast"] = test_idx["forecast"].values
    
    mae = (test.orders - test.forecast).abs().mean()
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=test.index, y=test.orders, name="Actual",
                              line=dict(color="black", width=1.5)))
    fig.add_trace(go.Scatter(x=test.index, y=test.forecast, name="Seasonal naive",
                              line=dict(color="#e76f51", width=2.2, dash="dot")))
    fig.update_layout(
        xaxis_title="", yaxis_title="Orders/hour",
        title=f"{city} — last 7 days actual vs forecast (MAE={mae:.2f})",
        height=400, margin=dict(l=0, r=0, t=40, b=0),
        legend=dict(orientation="h", y=1.1),
    )
    st.plotly_chart(fig, use_container_width=True)
    st.caption("Method: seasonal-naive (avg of same hour-of-week from training period). "
               "Sufficient day-1 baseline for sizing decisions.")


st.markdown("---")
st.caption("Built for Case 3 · Fresher submission · Synthetic data matching documented schema · "
           "Code: see GitHub repo · Decisions log in DECISIONS.md")
