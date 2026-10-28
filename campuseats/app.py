"""CampusEats application wiring — the entry point that uses every module.

This is the hub: it calls into pricing, menu, loyalty, inventory and receipt, so
each of those modules has at least one real caller here. Finding these call sites
is part of the dependency-check step in the coursework.
"""

from campuseats.cart import Cart
from campuseats.inventory import process_sale
from campuseats.loyalty import points_for, tier
from campuseats.menu import getPrice
from campuseats.pricing import priced_order
from campuseats.receipt import format_receipt, short_receipt


def checkout(items, member=False, promo=None):
    cart = Cart()
    for it in items:
        cart.add(it)
    total = priced_order(items, member, promo)
    prices = [getPrice(it) for it in items]
    receipt = format_receipt(items, prices, total)
    points = points_for(total)
    status = tier(points)
    return {
        "total": total,
        "receipt": receipt,
        "points": points,
        "tier": status,
    }


def quick_sale(item):
    note = process_sale(item, 1)
    receipt = short_receipt(getPrice(item))
    return note, receipt
