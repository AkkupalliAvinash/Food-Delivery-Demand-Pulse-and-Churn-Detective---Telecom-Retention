# 📊 CASE 4: CHURN DETECTIVE

## Submission Package Summary

---

## ✅ What's Inside

| File                        | Purpose                                                | How to Use                        |
| --------------------------- | ------------------------------------------------------ | --------------------------------- |
| **README.md**               | Start here! Quick start guide with everything you need | Read first (5 min)                |
| **EXEC_SUMMARY.md**         | Key findings written simply for the decision-maker     | Show to CMO (5 min read)          |
| **PRESENTATION.md**         | 5-slide presentation outline + speaker notes           | Present findings (10 min)         |
| **app.py**                  | Interactive Streamlit dashboard with 4 tabs            | Run: `streamlit run app.py`       |
| **case4_analysis.ipynb**    | Full Jupyter notebook with all analysis + models       | Open in Jupyter                   |
| **case4_telecom_churn.csv** | 7,000 customer records raw data                        | Used by both notebook & dashboard |
| **requirement.txt**         | Python packages needed                                 | `pip install -r requirement.txt`  |

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

1. **🔴 Who's Churning?**
   - Churn rate by contract type (month-to-month highest)
   - Churn by internet service (fiber highest)
   - Churn by tenure (first 6 months critical)

2. **👥 Segment Profiles**
   - 3 customer segments identified via clustering
   - Churn rate, size, avg tenure for each
   - Segment-specific characteristics

3. **💰 Retention Opportunity**
   - 3 retention plays ranked by ROI
   - Target customer count for each play
   - Expected revenue impact

4. **📈 Risk Model**
   - Feature importance (which factors predict churn)
   - Logistic regression model results
   - Actionable insights from coefficients

---

## 💡 Main Findings

**✓ Contract type determines churn:**

- 2-year contracts: 5% churn
- 1-year contracts: 10% churn
- Month-to-month: 45% churn
- Lock-in is 9x more powerful than anything else

**✓ First 6 months are critical:**

- Months 0-6: 45% churn (make or break)
- Months 6-12: 25% churn (still risky)
- Over 12 months: 5% churn (they're staying)

**✓ 3 distinct customer types:**

- Fiber-Frustrated (1,200) - need support
- At-Risk-New (1,000) - need lock-in
- Stable-Loyal (4,800) - mostly okay

**✓ Support calls = distress signal:**

- 1-2 calls: 10% churn
- 3-5 calls: 25% churn
- 5+ calls: 45% churn

---

## 💰 Retention Plays (ROI Ranked)

| #   | Play          | Target                      | Offer                     | Revenue Protected |
| --- | ------------- | --------------------------- | ------------------------- | ----------------- |
| 🥇  | Fiber Support | 1,200 fiber + high support  | Dedicated rep + 1 free mo | $267,000          |
| 🥈  | New Lock-in   | 1,000 new customers (0-6mo) | 20% discount for annual   | $142,000          |
| 🥉  | Budget Bundle | 1,000 low-bill + signals    | Free streaming 3 months   | $73,000           |
|     | **TOTAL**     | **~3,200 customers**        |                           | **$482,000**      |

---

## 📊 Data Details

- **Rows:** 7,000 telecom customers
- **Churn rate:** 40% (need to reduce!)
- **Key columns:** tenure_months, contract_type, internet_service, monthly_charges, support_calls_3mo, churned
- **Segments:** 3 clusters identified via K-means

---

## 🛠️ Technologies

- Python (analysis & modeling)
- Pandas (data manipulation)
- Scikit-learn (clustering, logistic regression)
- Streamlit (interactive dashboard)
- Plotly (interactive charts)
- Matplotlib (static charts)

---

## 📊 Model Performance

- **Logistic Regression AUC:** 0.89 (very good)
- **Top drivers:** Contract type > Tenure > Support calls > Internet service
- **Segments:** K-means with k=3 (interpretable, distinct profiles)

---

## 📝 Analysis Methodology

1. **Data loading & EDA** - Understand churn distribution
2. **Feature engineering** - Create relevant features
3. **Churn drivers** - Identify what predicts churn
4. **Predictive modeling** - Logistic regression + validation
5. **Customer clustering** - K-means to find segments
6. **Retention strategy** - Design plays for each segment
7. **Impact calculation** - Estimate revenue protected

---

## ❓ FAQ

**Q: How confident are the predictions?**  
A: Model (AUC 0.89) is very accurate on WHO will churn. Save-rates (15-35%) are industry-standard but not measured - needs pilot testing.

**Q: Why fiber customers?**  
A: They churn most (45%) AND have most support calls. Indicates service quality issue, not price problem.

**Q: What about new customers?**  
A: Month-to-month contracts let them leave easily. Locking them in with annual contract + discount is proven retention strategy.

**Q: How do I measure success?**  
A: Compare actual save-rate vs target (15-35%) after 30-day pilot. Calculate ROI = (revenue protected / program cost).

**Q: What could go wrong?**  
A: If save-rates are lower than predicted OR segments don't respond to offers. That's why we pilot first, measure, then scale.

---

## 📞 Next Steps

1. ✅ Show dashboard to CMO/leadership
2. ✅ Review findings and get buy-in
3. ⏳ **Run 30-day pilot** with 20% of each segment
4. ⏳ Track actual save-rate by segment
5. ⏳ If >2x ROI → Scale to 100%

---

## 🎯 Success Metrics 

- **Fiber Support:** Target 70% save rate → 840 customers saved
- **New Lock-in:** Target 50% save rate → 500 customers saved
- **Budget Bundle:** Target 40% save rate → 400 customers saved
- **Break-even ROI:** 2x (each $1 spent = $2 protected revenue)

---

