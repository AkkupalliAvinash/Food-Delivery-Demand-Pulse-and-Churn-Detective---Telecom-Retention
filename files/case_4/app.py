"""
CASE 4: CHURN DETECTIVE
=======================
Interactive dashboard to identify which telecom customers are churning,
why they're leaving, and what retention strategies work best.

For: CMO (decides customer retention spending and strategy)
"""
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.cluster import KMeans

st.set_page_config(page_title="Churn Detective", layout="wide", page_icon="📊")

# ========== SECTION 1: LOAD DATA ==========
@st.cache_data
def load_data():
    """Load telecom customer data"""
    data_path = Path(__file__).resolve().parent / "case4_telecom_churn.csv"
    if not data_path.exists():
        raise FileNotFoundError(f"{data_path.name} not found next to app.py")
    
    df = pd.read_csv(data_path)
    return df

df = load_data()

# ========== SECTION 2: HEADER & DESCRIPTION ==========
st.title("📊 Churn Detective — Telecom Retention Strategy")
st.caption(
    f"👥 Data: {len(df):,} customers | "
    f"🔴 Current churn: {df.churned.mean():.1%}"
)

# ========== SECTION 3: FILTERS (SIDEBAR) ==========
st.sidebar.header("🔍 Filter Data")
st.sidebar.write("Choose customer segments to analyze:")

contract_types = st.sidebar.multiselect("Contract Type", 
                                         sorted(df.contract_type.unique()),
                                         default=sorted(df.contract_type.unique()))
internet_services = st.sidebar.multiselect("Internet Service", 
                                            sorted(df.internet_service.unique()),
                                            default=sorted(df.internet_service.unique()))

# Apply filters
f = df[df.contract_type.isin(contract_types) & df.internet_service.isin(internet_services)]

# ========== SECTION 4: KEY METRICS (TOP) ==========
st.subheader("📈 Key Metrics")
c1, c2, c3, c4 = st.columns(4)
c1.metric("Total Customers (filtered)", f"{len(f):,}")
c2.metric("Churn Rate", f"{f.churned.mean():.1%}")
c3.metric("Avg Tenure (months)", f"{f.tenure_months.mean():.1f}")
c4.metric("Avg Monthly Spend", f"${f.monthly_charges.mean():.0f}")

# ---- Tab layout ----
tab1, tab2, tab3, tab4 = st.tabs(["🔴 Who's Churning?",
                                   "👥 Segment Profiles",
                                   "💰 Retention Opportunity",
                                   "📈 Risk Model"])

with tab1:
    st.subheader("Churn drivers: contract, internet, tenure, support")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Contract type
        contract_churn = f.groupby("contract_type").churned.agg(["mean", "size"]).reset_index()
        contract_churn = contract_churn.sort_values("mean", ascending=False)
        fig = px.bar(contract_churn, x="contract_type", y="mean",
                     text="size",
                     labels={"mean": "Churn Rate", "contract_type": "Contract Type", "size": "Count"},
                     color="mean", color_continuous_scale="Reds",
                     title="Churn by Contract Type")
        fig.update_layout(height=380, showlegend=False)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Internet service
        internet_churn = f.groupby("internet_service").churned.agg(["mean", "size"]).reset_index()
        internet_churn = internet_churn.sort_values("mean", ascending=False)
        fig = px.bar(internet_churn, x="internet_service", y="mean",
                     text="size",
                     labels={"mean": "Churn Rate", "internet_service": "Internet Service", "size": "Count"},
                     color="mean", color_continuous_scale="Reds",
                     title="Churn by Internet Service")
        fig.update_layout(height=380, showlegend=False)
        st.plotly_chart(fig, use_container_width=True)
    
    # Tenure impact
    st.subheader("Tenure: the first year is critical")
    tenure_buckets = pd.cut(f.tenure_months, bins=[0,3,6,12,24,48,72], 
                             include_lowest=True,
                             labels=["0-3m","4-6m","7-12m","13-24m","25-48m","49-72m"])
    tenure_churn = f.groupby(tenure_buckets).churned.agg(["mean", "size"]).reset_index()
    tenure_churn.columns = ["tenure_range", "churn_rate", "count"]
    
    fig = px.bar(tenure_churn, x="tenure_range", y="churn_rate",
                 text="count",
                 labels={"churn_rate": "Churn Rate", "tenure_range": "Tenure", "count": "Count"},
                 color="churn_rate", color_continuous_scale="RdYlGn_r",
                 title="Churn Risk by Tenure (first year is critical)")
    fig.update_layout(height=380)
    st.plotly_chart(fig, use_container_width=True)
    
    st.info(
        "**Key insight:** Month 0–6 customers have 40–50% churn risk. "
        "Month 6–12 drops to 20–25%. After 1 year, churn risk stabilizes below 10%."
    )

with tab2:
    st.subheader("Segment customers by support behavior + tenure")
    
    # Create segments
    segment_cols = ["tenure_months", "support_calls_3mo", "monthly_charges"]
    X = f[segment_cols].fillna(0)
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
    f_seg = f.copy()
    f_seg["segment"] = kmeans.fit_predict(X_scaled)
    
    # Name segments
    segment_names = {
        0: "Segment A",
        1: "Segment B", 
        2: "Segment C"
    }
    
    for seg_id in [0, 1, 2]:
        seg_data = f_seg[f_seg["segment"] == seg_id]
        avg_tenure = seg_data["tenure_months"].mean()
        avg_support = seg_data["support_calls_3mo"].mean()
        avg_spend = seg_data["monthly_charges"].mean()
        churn_rate = seg_data["churned"].mean()
        size = len(seg_data)
        
        # Pick name based on characteristics
        if avg_support > 4:
            segment_names[seg_id] = "Service-Frustrated"
        elif avg_tenure < 12:
            segment_names[seg_id] = "At-Risk-New"
        else:
            segment_names[seg_id] = "Stable-Loyal"
    
    f_seg["segment_name"] = f_seg["segment"].map(segment_names)
    
    # Display segment profiles
    col1, col2, col3 = st.columns(3)
    
    for idx, seg_id in enumerate([0, 1, 2]):
        seg_data = f_seg[f_seg["segment"] == seg_id]
        seg_name = segment_names[seg_id]
        
        with [col1, col2, col3][idx]:
            st.metric(f"{seg_name}", 
                     f"{len(seg_data):,} customers",
                     f"Churn: {seg_data.churned.mean():.1%}")
            st.write(f"Avg tenure: {seg_data.tenure_months.mean():.0f}mo")
            st.write(f"Avg support calls: {seg_data.support_calls_3mo.mean():.1f}/3mo")
            st.write(f"Avg spend: ${seg_data.monthly_charges.mean():.0f}/mo")
    
    # Segment churn comparison
    segment_summary = f_seg.groupby("segment_name").churned.agg(["mean", "size"]).reset_index()
    segment_summary = segment_summary.sort_values("mean", ascending=False)
    
    fig = px.bar(segment_summary, x="segment_name", y="mean",
                 text="size",
                 labels={"mean": "Churn Rate", "segment_name": "Segment", "size": "Count"},
                 color="mean", color_continuous_scale="Reds",
                 title="Churn Rate by Segment")
    fig.update_layout(height=380)
    st.plotly_chart(fig, use_container_width=True)

with tab3:
    st.subheader("Where should retention dollars go? Three plays ranked by lift.")
    
    # Play 1: Month 0–6 new customer onboarding
    new_customers = f[f.tenure_months <= 6]
    current_churn_new = new_customers.churned.mean()
    target_churn_new = current_churn_new * 0.7  # 30% reduction
    new_customer_count = len(new_customers)
    retention_lift_1 = (current_churn_new - target_churn_new) * new_customer_count
    
    # Play 2: Support ticket response for high-call users
    high_support = f[f.support_calls_3mo >= 5]
    current_churn_support = high_support.churned.mean()
    target_churn_support = current_churn_support * 0.6  # 40% reduction
    support_count = len(high_support)
    retention_lift_2 = (current_churn_support - target_churn_support) * support_count
    
    # Play 3: Month-to-month contract retention (offer yearly discount)
    mtm = f[f.contract_type == "Month-to-month"]
    current_churn_mtm = mtm.churned.mean()
    target_churn_mtm = current_churn_mtm * 0.75  # 25% reduction
    mtm_count = len(mtm)
    retention_lift_3 = (current_churn_mtm - target_churn_mtm) * mtm_count
    
    plays = pd.DataFrame({
        "Play": [
            "1. New Customer Onboarding",
            "2. Support Escalation for High-Call Users",
            "3. Contract Upgrade Incentive (M2M→Annual)"
        ],
        "Target Group": [
            f"{new_customer_count:,} new customers",
            f"{support_count:,} high-support users",
            f"{mtm_count:,} month-to-month"
        ],
        "Current Churn": [
            f"{current_churn_new:.1%}",
            f"{current_churn_support:.1%}",
            f"{current_churn_mtm:.1%}"
        ],
        "Target Churn": [
            f"{target_churn_new:.1%}",
            f"{target_churn_support:.1%}",
            f"{target_churn_mtm:.1%}"
        ],
        "Est. Saves/Month": [
            f"{retention_lift_1:.0f}",
            f"{retention_lift_2:.0f}",
            f"{retention_lift_3:.0f}"
        ]
    })
    
    plays_sorted = plays.copy()
    plays_sorted["Saves"] = [retention_lift_1, retention_lift_2, retention_lift_3]
    plays_sorted = plays_sorted.sort_values("Saves", ascending=False)
    
    st.dataframe(plays_sorted[["Play", "Target Group", "Current Churn", "Target Churn", "Est. Saves/Month"]],
                 use_container_width=True, hide_index=True)
    
    st.info(
        f"**Total retention opportunity:** {(retention_lift_1 + retention_lift_2 + retention_lift_3):.0f} "
        "customers/month if all three plays succeed."
    )

with tab4:
    st.subheader("What predicts churn? Feature importance from a simple model")
    
    # Train a quick logistic regression
    feature_cols = ["tenure_months", "monthly_charges", "support_calls_3mo"]
    X_model = f[feature_cols].fillna(0)
    y_model = f["churned"].astype(int)
    
    scaler_model = StandardScaler()
    X_scaled_model = scaler_model.fit_transform(X_model)
    
    lr = LogisticRegression(max_iter=1000)
    lr.fit(X_scaled_model, y_model)
    
    coef_df = pd.DataFrame({
        "Feature": feature_cols,
        "Coefficient": lr.coef_[0],
        "Abs Importance": np.abs(lr.coef_[0])
    }).sort_values("Abs Importance", ascending=True)
    
    fig = px.bar(coef_df, x="Coefficient", y="Feature", orientation='h',
                 color="Coefficient",
                 color_continuous_scale="RdBu_r",
                 title="Feature Importance (Logistic Regression Coefficients)",
                 labels={"Coefficient": "Coefficient Value"})
    fig.update_layout(height=300)
    st.plotly_chart(fig, use_container_width=True)
    
    st.write(f"**Model insight:** Negative coefficient = **reduces** churn risk. Positive coefficient = **increases** churn risk.")
    st.caption(f"Trained on {len(f):,} customers with 3-feature logistic regression (no hyperparameter tuning).")

# ---- Footer ----
st.markdown("---")
st.caption("Churn Detective — Telecom Retention Strategy Dashboard")
