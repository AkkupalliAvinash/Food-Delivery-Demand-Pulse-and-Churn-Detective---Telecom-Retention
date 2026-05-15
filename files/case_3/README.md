# Case 3: Food Delivery Demand Pulse


### What This Project Does

Analyzes 50,000 food delivery orders to find:

- When demand actually peaks (lunch vs dinner)
- Where surge pricing is being wasted
- How to fix the surge policy

### Files Included

| File                             | What It Is                                                           |
| -------------------------------- | -------------------------------------------------------------------- |
| `app.py`                         | **Interactive dashboard** - Start here! See demand patterns visually |
| `case3_analysis.ipynb`           | **Full analysis notebook** - All code, calculations, charts          |
| `case3_food_delivery_orders.csv` | **Raw data** - 50,000 orders with timestamp, city, surge flag, etc.  |
| `EXEC_SUMMARY.md`                | **Key findings** - Read this if you only have 5 minutes              |
| `requirement.txt`                | **Python dependencies** - List of packages needed                    |

---

## How to Run

### Option 1: Run the Dashboard

```bash
# Install packages first
pip install -r requirement.txt

# Run the Streamlit dashboard
streamlit run app.py
```

Then open: **http://localhost:8501**

The dashboard has 4 tabs:

1. **🔥 Demand Heatmap** - See when orders peak (hours × days)
2. **🏙️ City Comparison** - Compare demand patterns across cities
3. **⚡ Surge vs Demand** - See where surge is wasted
4. **📈 Forecast** - Predict demand for next 7 days

### Option 2: Run the Notebook

```bash
# Install packages
pip install -r requirement.txt

# Open Jupyter and run case3_analysis.ipynb
jupyter notebook case3_analysis.ipynb
```

This shows all the analysis step-by-step with code and outputs.

---

## Key Findings 

✅ **Demand peaks at lunch (12-2 PM) and dinner (7-10 PM)**
✅ **Weekend dinners are the hottest** - 30% more orders than weekday lunch
✅ **Most cities follow same pattern** - Except Kolkata (stronger lunch)
❌ **Surge fires in wrong places** - 13% of surge happens in low-demand times
💡 **Can save ₹11k/month** - By turning off surge during low-demand slots

---

## Main Recommendations

1. **Stop surge during off-peaks** (3 PM - 5 PM, late evening)
2. **Increase surge during true peaks** (lunch & dinner windows)
3. **Kolkata special treatment** - Run stronger lunch incentives only in Kolkata

---

## Questions You Might Have

**Q: Why is mid-afternoon surge wasteful?**  
A: Because orders don't actually peak then - it just looks busy. When we compare to true demand, mid-afternoon has 20% fewer orders than real peaks.

**Q: Will this save money?**  
A: Yes. Removing mid-afternoon surge saves ~₹11k/month with no customer impact (they have same delivery times).

**Q: Should all cities run Kolkata's policy?**  
A: No! Only Kolkata has a lunch peak. Other cities should stick to dinner focus.

**Q: What's next?**  
A: Test this policy in 1-2 cities for a week, measure delivery times and customer satisfaction.

---

## Data Details

- **Rows:** 50,000 food delivery orders
- **Date range:** ~2 months
- **Cities:** 7 (Delhi, Mumbai, Bangalore, Pune, Kolkata, Hyderabad, Chennai)
- **Cuisines:** 9 (Pizza, Biryani, Samosa, Noodles, Butter Chicken, Pasta, etc.)
- **Key columns:** timestamp, city, cuisine, order_value, surge_applied, delivery_time_min

---

## Tools Used

- **Python** - Programming language
- **Pandas** - Data manipulation
- **Plotly** - Interactive charts
- **Streamlit** - Dashboard framework
- **Matplotlib** - Static charts (notebook)

---

