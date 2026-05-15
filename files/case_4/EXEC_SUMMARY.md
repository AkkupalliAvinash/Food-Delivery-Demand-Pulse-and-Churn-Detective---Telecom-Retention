# Case 4: Churn Detective — Telecom Retention

## Executive Summary

**For:** CMO (decides retention spending)  
**Question:** Who is leaving our telecom service? Can we keep them? Where should we spend retention money?

---

## What I Found

### 1. Who Churns Most?

**By Contract Type:**

- **Month-to-month contracts:** 40-50% churn (HIGHEST RISK)
- **1-year contracts:** ~10% churn
- **2-year contracts:** ~2-5% churn

→ **Lock-in works.** Annual contracts cut churn 10x vs month-to-month.

**By Tenure (How long they've been customers):**

- **Months 0-6:** 40-50% churn (NEW CUSTOMERS ARE AT RISK!)
- **Months 6-12:** 20-30% churn
- **Over 12 months:** ~5% churn (they stay loyal)

→ **First 6 months are critical.** If we keep them past month 6, they usually stay.

**By Internet Service:**

- **Fiber optic:** 45% churn (problem!)
- **DSL:** 25% churn
- **No internet:** 15% churn

→ **Fiber customers unhappy** - probably service quality issues, not price.

**By Support Calls:**

- **1-2 calls in 3 months:** 10% churn
- **3-4 calls in 3 months:** 25% churn
- **5+ calls in 3 months:** 40% churn

→ **More support calls = distressed customer.** They're struggling.

---

## The Real Problem: 3 Different Types of Churners

I ran clustering analysis (K-means) to find customer segments. Here's what I found:

| Segment              | Size             | Who They Are                                                 | Why They Leave                                       | What to Offer                                 |
| -------------------- | ---------------- | ------------------------------------------------------------ | ---------------------------------------------------- | --------------------------------------------- |
| **Fiber-Frustrated** | ~1,200 customers | New ($90/mo), high support calls (4-5/month), fiber internet | **Poor service quality** - too many problems         | Better support + 1 free month if 3+ issues    |
| **At-Risk New**      | ~1,000 customers | Very new (3-6 months), month-to-month, $40-70/mo             | **Don't know if switch is worth it** - still testing | Lock-in discount: 20% off if switch to annual |
| **Stable Loyal**     | ~4,800 customers | Long tenure (20+ months), 2-year contract, $50-80/mo         | **Generally happy** - low churn                      | Loyalty rewards (free upgrades, discounts)    |

---

## My 3 Retention Plays (Ranked by ROI)

### Play 1: Fiber Support Escalation (Highest ROI)

- **Who:** Fiber customers with 3+ support calls/month
- **Offer:** Assign dedicated support rep + 1 free month credit
- **Why it works:** They're in pain; help them today, they stay tomorrow
- **Expected impact:** Save ~$267k over 18 months

### Play 2: New Customer Lock-in

- **Who:** Customers in months 0-6, on month-to-month contracts
- **Offer:** Switch to annual contract, get 20% discount
- **Why it works:** Lock them in before they churn; discount costs less than acquisition
- **Expected impact:** Save ~$142k over 18 months

### Play 3: Value Bundle for Budget Customers

- **Who:** Customers under $50/month, showing early churn signals
- **Offer:** Free streaming add-on or $10/month discount for 3 months
- **Why it works:** Budget customers stay if they feel like they're getting value
- **Expected impact:** Save ~$73k over 18 months

---

## How Confident Am I?

✅ **High confidence on drivers** - Multiple models agree on what causes churn  
⚠️ **Medium confidence on save-rates** - 15-35% per play is industry typical, not measured here  
⚠️ **Needs pilot testing** - Should test on 10-20% of customers first

---

## Why I Think This Works

1. **Different segments need different offers** - Can't use one-size-fits-all approach
2. **Target the moments that matter** - New customer months are critical window
3. **Fiber is a quality issue, not price** - Offering discount won't help; need support
4. **Monthly contracts are risky** - Anyone on month-to-month could leave next month

---

## What I Did

1. Loaded 7,000 customer records
2. Analyzed churn patterns by contract, tenure, internet type, support calls
3. Built a logistic regression model to identify key drivers
4. Used K-means clustering to find 3 distinct customer segments
5. Designed specific offers for each segment
6. Calculated estimated impact (18-month revenue protected)

**Data:** 7,000 telecom customers  
**Churn rate:** 40% (higher than industry benchmark of 1.5% monthly)  
**Key finding:** First 6 months = 50% churn; after 12 months = 5% churn

- Save rates not benchmarked against your historical campaigns — they should be.

---

_Full notebook (EDA → model → segmentation → plays), 5-slide deck, and decisions log are in the repo. Happy to walk through any of it — particularly the segment-labeling logic, where the first pass got it wrong and the second pass is what's reported here._
