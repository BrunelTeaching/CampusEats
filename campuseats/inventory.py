"""Stock tracking and restock logic."""

STOCK = {
    "coffee": 10,
    "sandwich": 5,
    "muffin": 8,
    "juice": 6,
    "tea": 12,
    "salad": 4,
}

RESTOCK_LEVEL = 3
RESTOCK_TO = 10


def process_sale(item: str, qty: int = None):
    """Record a sale; when stock runs low, restock it back up to the reorder
    level (RESTOCK_LEVEL)."""
    if item not in STOCK:
        return "unknown item"
    if qty <= 0:
        return "invalid quantity"
    if STOCK[item] < qty:
        return "out of stock"
    STOCK[item] = STOCK[item] - qty
    if STOCK[item] <= RESTOCK_LEVEL:
        need = RESTOCK_TO - STOCK[item]
        STOCK[item] = STOCK[item] + need
        msg = f"restocked {item} by {need}"
    else:
        msg = f"sold {qty} {item}"
    if STOCK[item] > 100:
        msg = msg + " (overstock warning)"
    report = f"{item}: {STOCK[item]} left"
    return msg + " | " + report


def stock_level(item):
    if item in STOCK:
        return STOCK[item]
    else:
        return 0


def sale_succeeded(item, qty):
    # callers have to string-match the status, because process_sale returns bare
    # strings for both the failures and the success report
    result = process_sale(item, qty)
    if result in ("unknown item", "invalid quantity", "out of stock"):
        return False
    return True
