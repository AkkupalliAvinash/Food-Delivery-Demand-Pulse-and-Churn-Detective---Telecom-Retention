# Case 3: Food Delivery Demand Pulse

## Executive Summary

**For:** Operations Head (decides surge pricing policy)  
**Question:** When does demand actually peak? Where is surge being wasted?

---

## What I Found

### 1. Demand Peaks at Lunch and Dinner 

- **Lunch rush:** 12:00 PM - 2:00 PM (peak around 1 PM)
- **Dinner rush:** 7:00 PM - 10:00 PM (peak around 8 PM)
- Mid-afternoon (3 PM - 5 PM) looks busy but it's NOT a real peak

### 2. Weekends Hit Harder Than Weekdays

- Weekend dinners (Friday-Sunday 8-10 PM) are THE hottest window
- Weekend lunch is also stronger than weekday lunch
- But it's not a massive difference - just 5-10% more orders

### 3. Most Cities Are Actually Similar

- Delhi, Mumbai, Bangalore, Pune, Kolkata, Hyderabad, Chennai
- All follow the same lunch/dinner pattern
- EXCEPT: **Kolkata has stronger lunch demand** - this is the only real outlier

### 4. Surge Is Being Applied in Low-Demand Times 

- **13% of surge orders happen during low-demand periods**
- That's money wasted - riders are incentivized when they're not needed
- Surge should fire ONLY during actual peaks (lunch & dinner)

---

## What I Recommend

### Play 1: Stop Surge in Low-Demand Slots

- Remove surge during mid-afternoon (3 PM - 5 PM)
- Remove surge during off-peak evening hours
- **Estimated savings:** ₹11,000 per month

### Play 2: Boost Surge During True Peaks

- Increase surge during lunch (12-2 PM, especially weekdays)
- Increase surge during dinner (7-10 PM, especially weekends)
- Focus on attracting riders when demand is highest

### Play 3: Kolkata Special

- Kolkata has lunch peak nearly as strong as dinner peak
- Run stronger lunch incentives in Kolkata only
- Other cities don't need this

---

## How Sure Am I?

✅ **High confidence** - The data clearly shows lunch/dinner peaks  
✅ **Simple policy** - Just turn surge on/off at right times  
⚠️ **Needs testing** - Should test on a subset of cities first

---

## What I Did

1. Loaded 50,000 food delivery orders
2. Grouped by hour, day of week, city, cuisine
3. Calculated demand patterns (% of orders)
4. Compared where surge is applied vs where demand actually is
5. Identified waste and opportunities

**Data:** 50,000 orders over ~2 months  
**Cities:** 7 (Delhi, Mumbai, Bangalore, Pune, Kolkata, Hyderabad, Chennai)  
**Key metric:** Surge rate = 23.4% (surge applied to 1 in 4 orders)

| #   | Play                                                                                                                                                  | Estimated impact (monthly)                      | Confidence                                            |
| --- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------- | ----------------------------------------------------- |
| 1   | **Compress surge in low-demand slots.** Tighten threshold so surge only fires above the bottom-5 demand deciles (driver-shortage exceptions allowed). | **₹11k/mo saved** (~7% of current surge budget) | High — directly removes excess identified in the data |
| 2   | **Kolkata-specific lunch window.** Reallocate part of Kolkata's surge budget from 19–22 to 11–14. Do NOT replicate to other cities.                   | ~12% fewer lunch SLA breaches in Kolkata        | Medium — needs a 2-week pilot to calibrate            |
| 3   | **Pre-position riders 30 min before each city's evening peak**, using the forecast. Cuts cold-start surge.                                            | 5–8% reduction in first-30-min peak surge       | Medium — depends on rider-supply flexibility          |

## Assumptions you should challenge before signing off

- Surge cost = **₹40 extra per surge order**. We used this throughout. Real number is Finance's call.
- "Legitimate" surge rate in low-demand slots = **10%**. This is the bottom of what we observed; could be 5% or 15% with better instrumentation.
- All economics are based on **3 months of data** (Jan–Mar 2025). Q2 effects (heat, IPL) not included.

## How we'd evaluate this in production

- **Forecast accuracy:** weighted MAE where peak-hour errors count 5× off-peak. Today's symmetric MAE understates damage from missing a Sat-night spike.
- **Policy success:** SLA-breach rate during peaks (down) + total surge spend (down) at constant order volume.
- **A/B design:** Pilot Play 1 in 2 cities for 30 days; rest as control. Pre-register the metric you'll judge on.

## What we did NOT do

- No rider supply-side modeling — this dataset only has demand. Half the surge story is missing.
- No causal claim that suspending surge in low-demand slots doesn't cost us anything. The pilot is what proves that.
- No weather, holiday, or event features. Worth ~15–20% MAE lift in production.

---

