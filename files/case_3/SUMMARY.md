# 📊 CASE 3: FOOD DELIVERY DEMAND PULSE

## Submission Package Summary

---

## ✅ What's Inside

| File                               | Purpose                                                | How to Use                        |
| ---------------------------------- | ------------------------------------------------------ | --------------------------------- |
| **README.md**                      | Start here! Quick start guide with everything you need | Read first (5 min)                |
| **EXEC_SUMMARY.md**                | Key findings written simply for the decision-maker     | Show to boss (5 min read)         |
| **PRESENTATION.md**                | 5-slide presentation outline + speaker notes           | Present findings (10 min)         |
| **app.py**                         | Interactive Streamlit dashboard with 4 tabs            | Run: `streamlit run app.py`       |
| **case3_analysis.ipynb**           | Full Jupyter notebook with all analysis + code         | Open in Jupyter                   |
| **case3_food_delivery_orders.csv** | 50,000 orders raw data                                 | Used by both notebook & dashboard |
| **requirement.txt**                | Python packages needed                                 | `pip install -r requirement.txt`  |

---

## 🚀 Quick Start (3 Steps)

### Step 1: Install packages

```bash
pip install -r requirement.txt
```

### Step 2: Run the dashboard

```bash
streamlit run app.py
```

### Step 3: Open in browser

```
http://localhost:8501
```

---

## 📈 Dashboard Overview

**4 Interactive Tabs:**

1. **🔥 Demand Heatmap**
   - Shows when demand peaks (hours × days)
   - See lunch (12-2 PM) and dinner (7-10 PM) peaks
   - Weekend spikes clearly visible

2. **🏙️ City Comparison**
   - All 7 cities compared side-by-side
   - Shows Kolkata is different (stronger lunch)
   - Other cities follow same pattern

3. **⚡ Surge vs Demand**
   - Where surge is being wasted
   - Visual of low-demand slots getting surge
   - Quantifies the waste (13%)

4. **📈 Forecast**
   - 7-day demand forecast for selected city
   - Simple seasonal-naive model
   - Shows actual vs predicted

---

## 💡 Main Findings

**✓ Demand follows predictable pattern:**

- Lunch: 12 PM - 2 PM
- Dinner: 7 PM - 10 PM
- Mid-afternoon is NOT a peak

**✓ Weekends 30% busier than weekdays:**

- Especially true for dinner
- Lunch busier on weekends too

**✓ Cities mostly identical:**

- Except Kolkata (stronger lunch demand)
- Policy should be Kolkata-specific only

**✓ Surge misaligned with demand:**

- 13% of surge in low-demand times
- Wastes ₹11k/month

---

## 💰 Recommendations

| Play                     | What                         | Savings        |
| ------------------------ | ---------------------------- | -------------- |
| Stop mid-afternoon surge | Remove 3 PM - 5 PM surge     | ₹5,000/mo      |
| Strengthen true peaks    | Boost lunch & dinner surge   | ₹4,000/mo      |
| Kolkata special          | Lunch boost for Kolkata only | ₹2,000/mo      |
| **TOTAL**                |                              | **₹11,000/mo** |

---

## 📊 Data Details

- **Rows:** 50,000 food delivery orders
- **Time period:** ~2 months
- **Cities:** 7 (Delhi, Mumbai, Bangalore, Pune, Kolkata, Hyderabad, Chennai)
- **Key columns:** timestamp, city, cuisine, order_value, surge_applied, delivery_time_min

---

## 🛠️ Technologies

- Python (analysis)
- Pandas (data manipulation)
- Streamlit (interactive dashboard)
- Plotly (interactive charts)
- Matplotlib (static charts)

---

## 📝 Analysis Methodology

1. **Data loading & sanity checks** - Verify data integrity
2. **Time-based features** - Extract hour, day, weekend flags
3. **Demand analysis** - Group by hour × day × city to find patterns
4. **Surge analysis** - Compare surge placement vs actual demand
5. **Visualization** - Create interactive dashboard
6. **Forecasting** - Build simple seasonal model

---


## 📞 Next Steps

1. ✅ Show dashboard to stakeholders
2. ✅ Review findings and get buy-in
3. ⏳ **Run 1-week pilot** in 2-3 cities
4. ⏳ Measure: delivery times, customer satisfaction
5. ⏳ If good → Roll out to all cities

---

