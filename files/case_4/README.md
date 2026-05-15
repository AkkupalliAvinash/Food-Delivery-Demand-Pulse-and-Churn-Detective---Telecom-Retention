# Case 4: Churn Detective - Telecom Retention


### What This Project Does

Analyzes 7,000 telecom customers to find:

- Who is leaving (churning) and why
- What 3 customer segments need different retention offers
- Where retention spending will have highest ROI

### Files Included

| File                      | What It Is                                                                        |
| ------------------------- | --------------------------------------------------------------------------------- |
| `app.py`                  | **Interactive dashboard** - Start here! Explore churn patterns visually           |
| `case4_analysis.ipynb`    | **Full analysis notebook** - All code, clustering, models, charts                 |
| `case4_telecom_churn.csv` | **Raw data** - 7,000 customers with tenure, contract, support calls, churn status |
| `EXEC_SUMMARY.md`         | **Key findings** - Read this if you only have 5 minutes                           |
| `requirement.txt`         | **Python dependencies** - List of packages needed                                 |

---

## How to Run

### Option 1: Run the Dashboard (Recommended)

```bash
# Install packages first
pip install -r requirement.txt

# Run the Streamlit dashboard
streamlit run app.py
```

Then open: **http://localhost:8501**

The dashboard has 4 tabs:

1. **🔴 Who's Churning?** - Churn rates by contract, internet type, tenure
2. **👥 Segment Profiles** - 3 customer segments with churn rates
3. **💰 Retention Opportunity** - Top 3 retention plays ranked by impact
4. **📈 Risk Model** - Which factors predict churn most

### Option 2: Run the Notebook

```bash
# Install packages
pip install -r requirement.txt

# Open Jupyter and run case4_analysis.ipynb
jupyter notebook case4_analysis.ipynb
```

This shows all the analysis step-by-step with clustering, modeling, charts.

---

## Key Findings (2-Minute Summary)

✅ **Contract type matters MOST** - 2-year contracts churn 20x LESS than month-to-month  
✅ **First 6 months are critical** - New customers have 40-50% churn; older customers 5%  
✅ **Fiber customers struggling** - 45% churn (probably service quality issue)  
✅ **Support calls = distress signal** - Each support call increases churn risk  
✅ **3 distinct customer types** - Each needs different retention offer

---

## The 3 Retention Plays (What to Do)

### Play 1: Fiber Support Escalation 🏥 (Best ROI)

- **Target:** Fiber customers with 3+ support calls/month (~1,200 customers)
- **Offer:** Dedicated support rep + 1 free month
- **Why it works:** They're struggling; help today = loyalty tomorrow
- **Expected savings:** ~$267k over 18 months

### Play 2: New Customer Lock-in 🔒 (Highest Volume)

- **Target:** Customers months 0-6 on month-to-month plans (~1,000 customers)
- **Offer:** Switch to annual contract = 20% discount
- **Why it works:** Lock them in before they leave; discount costs less than acquisition
- **Expected savings:** ~$142k over 18 months

### Play 3: Budget Bundle 💰 (Quick Win)

- **Target:** Customers under $50/month with churn signals (~1,000 customers)
- **Offer:** Free streaming add-on or $10/month discount for 3 months
- **Why it works:** Budget customers stay if they feel like getting value
- **Expected savings:** ~$73k over 18 months

**Total potential impact:** ~$482k protected revenue over 18 months

---

## Main Insights

### Why People Churn:

1. **Month-to-month contracts** - No commitment, easy to leave
2. **New customer (first 6 months)** - Still evaluating if worth keeping
3. **Fiber service problems** - Too many support calls needed
4. **Support calls** - More calls = more frustration = higher churn
5. **Tenure less than 12 months** - Haven't built habit of staying yet

### Why People Stay:

1. **2-year contract** - Locked in; sunk cost psychology
2. **Tenure over 12 months** - Habit built; switching is hassle
3. **Few support calls** - Service is working; no problems
4. **Predictable price** - Know what they're paying each month

---

## Questions You Might Have

**Q: How confident are these numbers?**  
A: Models are very confident on WHO churns. The 15-35% save-rate per play is industry standard but not measured here - should test first.

**Q: Why not just lower prices?**  
A: Fiber customers aren't leaving because of price (they have different speeds/costs). They're leaving because service is bad. Lower price won't help.

**Q: What about month-to-month customers?**  
A: They should be offered annual contracts with discount. Lock-in is most powerful retention tool.

**Q: Should we target everyone?**  
A: No! Start with Play 1 (fiber customers) - highest ROI. Then Play 2 (new customers), then Play 3.

**Q: What's next?**  
A: Run a 30-day pilot on 20% of target customers. Track actual save-rate. If it works, scale.

---

## Data Details

- **Rows:** 7,000 telecom customers
- **Churn rate:** 40% (need to reduce this!)
- **Key columns:**
  - tenure_months (how long they've been customers)
  - contract_type (month-to-month, 1-year, 2-year)
  - internet_service (Fiber, DSL, None)
  - monthly_charges (what they pay)
  - support_calls_3mo (support calls in last 3 months)
  - churned (1=left, 0=stayed)

---

## Tools Used

- **Python** - Programming language
- **Pandas** - Data manipulation
- **Scikit-learn** - Machine learning (clustering, logistic regression)
- **Plotly** - Interactive charts
- **Streamlit** - Dashboard framework
- **Matplotlib** - Static charts (notebook)

---

## Model Performance

- **Logistic Regression:** AUC = 0.89 (very good)
- **Top churn drivers:** Contract type > Tenure > Support calls > Internet service
- **Clustering:** K-means with k=3 identifies 3 distinct customer segments

---


**Date:** May 2026  
**Time taken:** Full analysis + dashboard + clustering from scratch
