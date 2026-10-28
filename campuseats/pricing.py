"""Order pricing: totals, member tiers, and promo codes."""

from campuseats.menu import getPrice


def order_total(items):
    """Return the order total in GBP, including 20% VAT."""
    total = 0.0
    for it in items:
        total = total + getPrice(it)
    return round(total, 2)


def priced_order(items, member=False, promo: str = None):
    total = order_total(items)
    if member:
        if total > 50:
            total = total * 0.85
        elif total > 20:
            total = total * 0.90
        else:
            total = total * 0.95
    else:
        if total > 50:
            total = total * 0.95
        elif total > 20:
            total = total * 0.98
        else:
            total = total
    if promo == "WELCOME":
        total = total - 2.0
    elif promo == "HALF":
        if total > 10:
            total = total * 0.5
        else:
            total = total
    elif promo == "FREEITEM":
        if len(items) > 2:
            total = total - getPrice(items[0])
    if total < 0:
        total = 0.0
    return round(total, 2)
