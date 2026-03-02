# CPA Tracking & Analytics Guide

## Why Tracking Matters

**"You can't optimize what you don't measure."**

Without proper tracking:
- ❌ Don't know which ads work
- ❌ Can't calculate ROI
- ❌ Waste money on losers
- ❌ Can't scale effectively

With tracking:
- ✅ Know exactly what converts
- ✅ Optimize campaigns
- ✅ Cut losing ads fast
- ✅ Scale winners profitably

---

## Key Metrics to Track

### Primary Metrics

| Metric | Formula | Target |
|--------|---------|--------|
| **Impressions** | Times ad shown | Volume indicator |
| **Clicks** | Total clicks | Traffic volume |
| **CTR** | Clicks ÷ Impressions × 100 | 1-5%+ |
| **Conversions** | Completed actions | Revenue source |
| **CR** | Conversions ÷ Clicks × 100 | 3-10%+ |
| **Revenue** | Conversions × Payout | Earnings |
| **Cost** | Ad spend | Investment |
| **Profit** | Revenue - Cost | Goal: Positive |
| **ROI** | (Revenue - Cost) ÷ Cost × 100 | 100%+ |
| **EPC** | Revenue ÷ Clicks | $0.50+ |

### Secondary Metrics

| Metric | Purpose |
|--------|---------|
| **CPV** | Cost Per View (pop traffic) |
| **CPC** | Cost Per Click |
| **CPA** | Cost Per Acquisition |
| **LTV** | Lifetime Value (recurring) |
| **Bounce Rate** | Landing page quality |
| **Time on Page** | Engagement level |

---

## Tracking Tools

### Professional Trackers

#### Voluum
- **Price:** $69-999/month
- **Best For:** High-volume affiliates
- **Features:** Real-time analytics, AI optimization, multi-offer paths

#### Binom
- **Price:** $69-299/month (self-hosted)
- **Best For:** Privacy-focused, technical users
- **Features:** Fast, full control, one-time fee option

#### BeMob
- **Price:** Free-$399/month
- **Best For:** Beginners to intermediate
- **Features:** Cloud-based, easy setup

### Free/Low-Cost Options

| Tool | Price | Limitations |
|------|-------|-------------|
| Google Analytics | Free | Not built for CPA |
| Pretty Links | Free/$49/year | Basic link tracking |
| Bitly | Free/$29/month | Link shortener only |
| Prosper202 | Free | Self-hosted, outdated |

---

## Tracking Setup

### Link Structure

```
Base URL: https://your-offer-link.com
Parameters:
  - sub1: Traffic source (instagram, tiktok, etc.)
  - sub2: Campaign name
  - sub3: Ad creative ID
  - sub4: Device type
  - sub5: Geographic target

Final URL:
https://your-offer-link.com?sub1=instagram&sub2=gaming_cheats&sub3=video1&sub4=mobile&sub5=us
```

### UTM Parameters (Standard)

```
?utm_source=instagram
&utm_medium=social
&utm_campaign=gaming_cheats
&utm_content=video1
&utm_term=us_mobile
```

---

## Tracking Pixel Setup

### How Pixels Work
1. User clicks your link
2. Cookie/session stores tracking data
3. User completes offer
4. Pixel fires on thank-you page
5. Conversion recorded in tracker

### Implementation

**On Landing Page (Head):**
```html
<!-- Landing Page Pixel -->
<script>
(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-XXXXXX');
</script>
```

**On Thank You Page:**
```html
<!-- Conversion Pixel -->
<img src="https://tracker.com/pixel?amount=1.50&subid={subid}" height="1" width="1" />
```

---

## Dashboard Setup

### Key Reports to Monitor

#### Daily Overview
```
Date: 2026-03-02
Impressions: 10,000
Clicks: 500 (CTR: 5%)
Conversions: 25 (CR: 5%)
Revenue: $125.00
Cost: $50.00
Profit: $75.00
ROI: 150%
EPC: $0.25
```

#### By Traffic Source
```
Source       | Clicks | Conv | Rev    | Cost   | Profit | ROI
-------------|--------|------|--------|--------|--------|-----
Instagram    | 200    | 12   | $60    | $20    | $40    | 200%
TikTok       | 150    | 8    | $40    | $15    | $25    | 167%
YouTube      | 100    | 3    | $15    | $10    | $5     | 50%
Twitter      | 50     | 2    | $10    | $5     | $5     | 100%
```

#### By Offer
```
Offer        | Clicks | Conv | CR    | Rev    | EPC
-------------|--------|------|-------|--------|-----
Gift Card    | 200    | 15   | 7.5%  | $75    | $0.38
App Install  | 300    | 10   | 3.3%  | $50    | $0.17
```

---

## A/B Test Tracking

### Test Structure
```
Test: Landing Page A vs B
Traffic Split: 50/50
Duration: Until 100 conversions per variant

Variant A (Control):
- Views: 1000
- Conversions: 30
- CR: 3.0%

Variant B (Test):
- Views: 1000
- Conversions: 45
- CR: 4.5%

Winner: Variant B (+50% improvement)
```

### Statistical Significance
Use a calculator to ensure 95%+ confidence:
- https://www.optimizely.com/sample-size-calculator/
- https://vwo.com/tools/ab-test-significance-calculator/

---

## Optimization Rules

### Cut Losers When:
- 100+ clicks, 0 conversions → Kill
- ROI < -50% after $20 spend → Kill
- CTR < 0.5% → Test new creative or kill

### Scale Winners When:
- ROI > 100% for 3+ days → Increase budget 20-50%
- Consistent conversions → Duplicate to new audiences
- EPC > $0.50 → Test similar offers

### Pause When:
- ROI drops below 0% → Investigate
- Conversion rate drops 50%+ → Check offer
- Traffic quality drops → Check source

---

## Reporting Schedule

### Daily Tasks
- [ ] Check yesterday's stats
- [ ] Update profit/loss spreadsheet
- [ ] Pause losing ads
- [ ] Scale winning ads

### Weekly Tasks
- [ ] Full campaign audit
- [ ] Calculate weekly ROI
- [ ] Plan next week's tests
- [ ] Research new offers

### Monthly Tasks
- [ ] Review top performers
- [ ] Archive old campaigns
- [ ] Update tracking systems
- [ ] Network for new opportunities