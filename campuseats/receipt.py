"""Receipt formatting."""

from campuseats.menu import MENU

HEADER = "=== CampusEats ==="


def _unused_divider():
    return "-" * 20


def format_line(name, price):
    """Format one line: the name padded to 20 columns, then the price to 2 dp."""
    return name.ljust(12) + " " + ("%.2f" % price).rjust(6)


def format_receipt(items, prices, total, member=False, promo=None):
    # God method: receipt formatting mixed with discount, promo and footer
    # business logic -- a formatter that also does the pricing maths
    lines = [HEADER]
    i = 0
    while i < len(items):
        lines.append(format_line(items[i], prices[i]))
        i = i + 1
    grand = total
    if member:
        if total > 50:
            grand = total - total * 0.15
            lines.append("MEMBER 15%")
        elif total > 20:
            grand = total - total * 0.10
            lines.append("MEMBER 10%")
        else:
            grand = total - total * 0.05
            lines.append("MEMBER 5%")
    if promo == "WELCOME":
        grand = grand - 2
        lines.append("PROMO WELCOME")
    elif promo == "HALF":
        grand = grand * 0.5
        lines.append("PROMO HALF")
    if grand < 0:
        grand = 0.0
        lines.append("ERROR: negative total")
    lines.append("TOTAL" + " " + ("%.2f" % grand).rjust(6))
    if member and grand > 30:
        lines.append("You earned a bonus on this order!")
    elif grand > 10:
        lines.append("Thanks for your order!")
    return "\n".join(lines)


def short_receipt(total):
    return HEADER + "\nTOTAL " + ("%.2f" % total)


def receipt_for(items):
    # builds a receipt straight from the menu data, doing the price lookup itself
    lines = [HEADER]
    total = 0.0
    for item in items:
        key = item.lower()
        price = MENU[key] if key in MENU else 0.0
        lines.append(format_line(item, price))
        total = total + price
    lines.append("TOTAL" + " " + ("%.2f" % total).rjust(6))
    return "\n".join(lines)


def receipt_width(w: int = None):
    if w is None:
        return 20
    else:
        return w
