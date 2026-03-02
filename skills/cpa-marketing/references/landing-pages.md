# CPA Landing Pages Guide

## Landing Page Types

### 1. Pre-Sell Page
**Purpose:** Warm up visitors before sending to offer

**Structure:**
- Hook headline
- Problem identification
- Solution introduction
- Benefits list
- Social proof
- CTA button

**Best For:** High-payout offers, cold traffic

---

### 2. Content Locker Page
**Purpose:** Lock valuable content behind offer completion

**Structure:**
- Value proposition
- Content preview
- Lock notice
- Clear instructions
- Download/access button

**Best For:** Files, guides, tools, exclusive content

---

### 3. Bridge Page
**Purpose:** Connect ad to offer with context

**Structure:**
- Attention-grabber matching ad
- Brief explanation
- Strong CTA
- Link to offer

**Best For:** Email submits, app installs, simple offers

---

### 4. Review/Comparison Page
**Purpose:** Build trust and guide decision

**Structure:**
- Problem statement
- Product comparison
- Pros/cons
- Recommendation
- CTA

**Best For:** Trial offers, purchases, subscriptions

---

### 5. Quiz/Funnel Page
**Purpose:** Engage and qualify leads

**Structure:**
- Quiz questions
- Personalization
- Results + offer
- CTA

**Best For:** Health, finance, dating offers

---

## High-Converting Elements

### Headlines That Convert
```
✅ "Get [Desired Result] in [Time Frame]"
✅ "[Number] Ways to [Achieve Goal]"
✅ "Free [Valuable Thing] - Limited Time"
✅ "Unlock [Exclusive Content] Now"
✅ "[Problem]? Here's the Solution"

❌ "Click Here"
❌ "Buy Now"
❌ Generic statements
```

### CTA Buttons
```
✅ "Get Your Free [Item]"
✅ "Unlock Now"
✅ "Claim Your [Benefit]"
✅ "Start Free Trial"
✅ "Download Now"

❌ "Submit"
❌ "Continue"
❌ "Click Here"
```

### Trust Indicators
- Social proof (testimonials, reviews)
- Trust badges (SSL, security icons)
- Statistics (downloads, users)
- Media mentions
- Guarantees

---

## Mobile Optimization

### Must-Have Elements
- [ ] Responsive design (mobile-first)
- [ ] Fast load time (<3 seconds)
- [ ] Large, tappable buttons (min 44x44px)
- [ ] Readable font size (16px+)
- [ ] Minimal form fields
- [ ] No pop-ups on mobile
- [ ] Thumb-friendly navigation

### Mobile Landing Page Template
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Unlock [Content]</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }
        .container { max-width: 480px; margin: 0 auto; padding: 20px; }
        h1 { font-size: 24px; margin-bottom: 15px; text-align: center; }
        .preview { background: #f5f5f5; padding: 20px; border-radius: 10px; margin: 20px 0; }
        .cta-button { 
            display: block; 
            width: 100%; 
            padding: 18px; 
            background: #007bff; 
            color: white; 
            text-align: center; 
            text-decoration: none; 
            border-radius: 10px; 
            font-size: 18px; 
            font-weight: bold;
            margin-top: 20px;
        }
        .trust { text-align: center; margin-top: 20px; color: #666; font-size: 14px; }
    </style>
</head>
<body>
    <div class="container">
        <h1>🔓 Unlock [Valuable Content]</h1>
        
        <div class="preview">
            <p>Preview of content...</p>
        </div>
        
        <p style="text-align: center;">Complete a quick offer to unlock:</p>
        
        <a href="YOUR_OFFER_LINK" class="cta-button">Unlock Now - Free</a>
        
        <p class="trust">✓ Instant access ✓ Free ✓ Secure</p>
    </div>
</body>
</html>
```

---

## A/B Testing Checklist

### Test These Elements
1. **Headlines** - Test 3-5 variations
2. **CTA text** - Test different phrases
3. **Button color** - Test 3 colors
4. **Images** - Test different visuals
5. **Layout** - Test 2-3 designs
6. **Copy length** - Short vs long
7. **Trust elements** - With vs without

### Testing Process
1. Run A/B test for 100+ conversions
2. Statistical significance (95%+ confidence)
3. Implement winner
4. Test new element
5. Repeat continuously

---

## Landing Page Tools

### Builders (No Code)
| Tool | Price | Best For |
|------|-------|----------|
| Carrd | $19/year | Simple pages |
| Leadpages | $49/month | High-converting templates |
| Unbounce | $99/month | Advanced optimization |
| ClickFunnels | $147/month | Full funnels |
| Instapage | $199/month | Enterprise |

### Free Options
- Google Sites
- WordPress + Elementor
- GitHub Pages
- Netlify

---

## Speed Optimization

### Target: <3 Second Load Time

**Quick Wins:**
1. Compress images (TinyPNG)
2. Use CDN (Cloudflare free)
3. Minify CSS/JS
4. Lazy load images
5. Remove unused scripts
6. Use caching
7. Optimize fonts

**Testing Tools:**
- Google PageSpeed Insights
- GTmetrix
- Pingdom
- WebPageTest

---

## Conversion Rate Benchmarks

| Landing Page Type | Poor | Average | Good | Excellent |
|-------------------|------|---------|------|-----------|
| Content Locker | <5% | 5-10% | 10-20% | >20% |
| Pre-Sell | <2% | 2-5% | 5-10% | >10% |
| Bridge Page | <10% | 10-20% | 20-30% | >30% |
| Quiz/Funnel | <3% | 3-8% | 8-15% | >15% |

---

## Compliance Checklist

- [ ] FTC disclosure visible
- [ ] Privacy policy linked
- [ ] Terms of service
- [ ] Contact information
- [ ] No misleading claims
- [ ] No fake countdown timers
- [ ] No fake scarcity
- [ ] Accurate content preview