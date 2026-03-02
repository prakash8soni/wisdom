---
name: cpa-marketing
description: Comprehensive CPA (Cost Per Action) affiliate marketing skill for promoting content locking links, optimizing conversions, and automating traffic generation. Use when: (1) Planning CPA campaigns, (2) Creating promotional content, (3) Setting up tracking and analytics, (4) Optimizing conversion rates, (5) Automating social media traffic, (6) Building landing pages for offers, (7) A/B testing strategies, (8) Scaling affiliate campaigns.
---

# CPA Marketing Skill

Master the art and science of Cost Per Action affiliate marketing.

## Core Concepts

### What is CPA Marketing?
- **CPA = Cost Per Action** - Advertisers pay when users complete specific actions
- **Actions**: Form submissions, app installs, purchases, signups, downloads
- **Key Metric**: EPC (Earnings Per Click) = Total Earnings ÷ Total Clicks

### Content Locking
Users must complete an offer (survey, email submit, app install) to unlock valuable content.

**Best Practices:**
1. Offer real value behind the lock
2. Make the unlock process seamless
3. Use clear, compelling CTAs
4. Mobile-optimize all pages

---

## Skill Modules

### Module 1: Offer Selection
**Reference:** [offers.md](references/offers.md)

Key factors when choosing offers:
- Payout amount
- EPC (Earnings Per Click)
- Conversion rate
- Niche alignment
- Geographic targeting
- Traffic source restrictions

### Module 2: Traffic Sources
**Reference:** [traffic.md](references/traffic.md)

Major traffic sources:
1. **Social Media** - Instagram, TikTok, Facebook, Twitter, Pinterest
2. **Search** - SEO, PPC (Google/Bing Ads)
3. **Native Ads** - Taboola, Outbrain, MGID
4. **Push Notifications** - PropellerAds, EvaDav
5. **Email Marketing** - Solo ads, newsletters
6. **Video** - YouTube, TikTok, Reels

### Module 3: Landing Pages
**Reference:** [landing-pages.md](references/landing-pages.md)

Essential elements:
- Attention-grabbing headline
- Clear value proposition
- Trust indicators
- Strong CTA
- Mobile-first design
- Fast load time (<3 seconds)

### Module 4: Tracking & Analytics
**Reference:** [tracking.md](references/tracking.md)

Must-track metrics:
- Clicks (total, unique)
- Conversions
- Revenue
- CTR (Click-Through Rate)
- CR (Conversion Rate)
- EPC (Earnings Per Click)
- ROI (Return on Investment)

### Module 5: Compliance
**Reference:** [compliance.md](references/compliance.md)

Legal requirements:
- FTC disclosure (#ad, #affiliate)
- Privacy policy
- GDPR compliance (EU)
- CCPA compliance (California)
- Platform ToS adherence

---

## Quick Start Checklist

### Day 1-3: Setup
- [ ] Choose CPA network(s) and get approved
- [ ] Select 3-5 offers to test
- [ ] Set up tracking (Voluum, Binom, or Google Analytics)
- [ ] Create first landing page
- [ ] Set up link cloaking/rotation

### Day 4-7: Launch
- [ ] Create social accounts for traffic
- [ ] Post initial content (5-10 pieces)
- [ ] Drive first 100 clicks
- [ ] Analyze initial data
- [ ] Optimize based on results

### Week 2-4: Scale
- [ ] Double down on winning offers
- [ ] Expand to new traffic sources
- [ ] A/B test landing pages
- [ ] Automate posting schedule
- [ ] Build email list

---

## Automation Scripts

### Link Rotator
```python
# scripts/link_rotator.py - Rotate between multiple offers
import random

OFFERS = [
    {"url": "https://offer1.com/aff_id", "weight": 50},
    {"url": "https://offer2.com/aff_id", "weight": 30},
    {"url": "https://offer3.com/aff_id", "weight": 20},
]

def get_offer():
    total = sum(o["weight"] for o in OFFERS)
    r = random.randint(1, total)
    cumulative = 0
    for offer in OFFERS:
        cumulative += offer["weight"]
        if r <= cumulative:
            return offer["url"]
```

### Social Posting Schedule
```python
# scripts/social_schedule.py - Optimal posting times
POSTING_TIMES = {
    "instagram": ["9am", "12pm", "5pm", "8pm"],
    "tiktok": ["7am", "10am", "3pm", "7pm", "11pm"],
    "twitter": ["8am", "12pm", "5pm", "9pm"],
    "facebook": ["9am", "1pm", "4pm", "8pm"],
}
```

---

## Common Mistakes to Avoid

1. ❌ **Promoting too many offers** - Focus on 3-5 winners
2. ❌ **Ignoring mobile users** - 70%+ traffic is mobile
3. ❌ **Slow landing pages** - Every second costs conversions
4. ❌ **No tracking** - You can't optimize what you don't measure
5. ❌ **Spamming** - Quality > quantity, always
6. ❌ **Ignoring compliance** - FTC fines are real
7. ❌ **Giving up too early** - Test for at least 1000 clicks

---

## Success Metrics

| Metric | Poor | Average | Good | Excellent |
|--------|------|---------|------|-----------|
| CTR | <1% | 1-3% | 3-5% | >5% |
| CR | <1% | 1-3% | 3-5% | >5% |
| EPC | <$0.10 | $0.10-$0.50 | $0.50-$1.00 | >$1.00 |
| ROI | <50% | 50-100% | 100-200% | >200% |

---

## Resources

### CPA Networks
- MaxBounty
- ClickDealer
- CPA Grip
- OfferVault
- PeerFly
- ClickBank

### Tools
- **Tracking**: Voluum, Binom, Prosper202
- **Landing Pages**: Unbounce, Leadpages, ClickFunnels
- **Link Management**: Bitly, Pretty Links, ThirstyAffiliates
- **Social Scheduling**: Buffer, Hootsuite, Later
- **Design**: Canva, Figma, Adobe Express

### Learning
- STM Forum (stmforum.com)
- AffiliateFix (affiliatefix.com)
- BlackHatWorld (blackhatworld.com)
- YouTube: Charles Ngo, Luke Kling