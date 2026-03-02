#!/usr/bin/env python3
"""
CPA Link Rotator - Rotate between multiple affiliate offers
Usage: python link_rotator.py
"""

import random
from datetime import datetime
import json
import os

# Configuration file path
CONFIG_FILE = os.path.join(os.path.dirname(__file__), 'offers.json')

def load_offers():
    """Load offers from config file"""
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as f:
            return json.load(f)
    return []

def save_offers(offers):
    """Save offers to config file"""
    with open(CONFIG_FILE, 'w') as f:
        json.dump(offers, f, indent=2)

def get_offer(offers=None):
    """Get a weighted random offer"""
    if offers is None:
        offers = load_offers()
    
    if not offers:
        return None
    
    total_weight = sum(o.get('weight', 50) for o in offers)
    r = random.randint(1, total_weight)
    cumulative = 0
    
    for offer in offers:
        cumulative += offer.get('weight', 50)
        if r <= cumulative:
            return offer
    
    return offers[0]

def add_offer(name, url, payout, weight=50, niche=None):
    """Add a new offer to rotation"""
    offers = load_offers()
    offers.append({
        'name': name,
        'url': url,
        'payout': payout,
        'weight': weight,
        'niche': niche,
        'added': datetime.now().isoformat(),
        'clicks': 0,
        'conversions': 0
    })
    save_offers(offers)
    print(f"✓ Added: {name} (${payout})")

def list_offers():
    """List all offers"""
    offers = load_offers()
    if not offers:
        print("No offers configured")
        return
    
    print("\n📊 Current Offers:")
    print("-" * 60)
    for i, offer in enumerate(offers, 1):
        stats = f"[{offer.get('clicks', 0)} clicks, {offer.get('conversions', 0)} conv]"
        print(f"{i}. {offer['name']}")
        print(f"   URL: {offer['url']}")
        print(f"   Payout: ${offer['payout']} | Weight: {offer['weight']}% | {stats}")
    print("-" * 60)

def record_click(offer_name):
    """Record a click for an offer"""
    offers = load_offers()
    for offer in offers:
        if offer['name'] == offer_name:
            offer['clicks'] = offer.get('clicks', 0) + 1
            save_offers(offers)
            return True
    return False

def record_conversion(offer_name):
    """Record a conversion for an offer"""
    offers = load_offers()
    for offer in offers:
        if offer['name'] == offer_name:
            offer['conversions'] = offer.get('conversions', 0) + 1
            save_offers(offers)
            return True
    return False

def stats():
    """Show statistics for all offers"""
    offers = load_offers()
    if not offers:
        print("No offers configured")
        return
    
    print("\n📈 Offer Statistics:")
    print("-" * 80)
    print(f"{'Name':<20} {'Clicks':>10} {'Conv':>10} {'CR':>10} {'Revenue':>12} {'EPC':>10}")
    print("-" * 80)
    
    total_clicks = 0
    total_conv = 0
    total_rev = 0
    
    for offer in offers:
        clicks = offer.get('clicks', 0)
        conv = offer.get('conversions', 0)
        rev = conv * offer['payout']
        cr = (conv / clicks * 100) if clicks > 0 else 0
        epc = (rev / clicks) if clicks > 0 else 0
        
        total_clicks += clicks
        total_conv += conv
        total_rev += rev
        
        print(f"{offer['name']:<20} {clicks:>10} {conv:>10} {cr:>9.1f}% ${rev:>10.2f} ${epc:>9.2f}")
    
    print("-" * 80)
    total_cr = (total_conv / total_clicks * 100) if total_clicks > 0 else 0
    total_epc = (total_rev / total_clicks) if total_clicks > 0 else 0
    print(f"{'TOTAL':<20} {total_clicks:>10} {total_conv:>10} {total_cr:>9.1f}% ${total_rev:>10.2f} ${total_epc:>9.2f}")
    print("-" * 80)

# CLI interface
if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("CPA Link Rotator")
        print("\nUsage:")
        print("  python link_rotator.py get              - Get weighted random offer")
        print("  python link_rotator.py add              - Add new offer (interactive)")
        print("  python link_rotator.py list             - List all offers")
        print("  python link_rotator.py stats            - Show statistics")
        print("  python link_rotator.py click <name>     - Record click")
        print("  python link_rotator.py conv <name>      - Record conversion")
        sys.exit(1)
    
    command = sys.argv[1]
    
    if command == 'get':
        offer = get_offer()
        if offer:
            print(f"Selected: {offer['name']}")
            print(f"URL: {offer['url']}")
            print(f"Payout: ${offer['payout']}")
        else:
            print("No offers configured. Add some first!")
    
    elif command == 'add':
        name = input("Offer name: ")
        url = input("Affiliate URL: ")
        payout = float(input("Payout ($): "))
        weight = int(input("Weight (1-100, default 50): ") or "50")
        niche = input("Niche (optional): ")
        add_offer(name, url, payout, weight, niche if niche else None)
    
    elif command == 'list':
        list_offers()
    
    elif command == 'stats':
        stats()
    
    elif command == 'click':
        if len(sys.argv) < 3:
            print("Usage: python link_rotator.py click <offer_name>")
            sys.exit(1)
        record_click(sys.argv[2])
        print(f"✓ Click recorded for: {sys.argv[2]}")
    
    elif command == 'conv':
        if len(sys.argv) < 3:
            print("Usage: python link_rotator.py conv <offer_name>")
            sys.exit(1)
        record_conversion(sys.argv[2])
        print(f"✓ Conversion recorded for: {sys.argv[2]}")
    
    else:
        print(f"Unknown command: {command}")