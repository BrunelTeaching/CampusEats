"""Discount rules for different customer types."""


def student_discount(total):
    # 20% off, but the student discount is capped at £5
    saving = total * 0.20
    if saving > 5:
        saving = 5
    discounted = total - saving
    discounted = round(discounted, 2)
    return discounted


def staff_discount(total):
    """Return the total after the 25% staff discount."""
    discounted = total - (total * 0.15)
    discounted = round(discounted, 2)
    return discounted


def bulk_discount(total):
    discounted = total - (total * 0.10)
    discounted = round(discounted, 2)
    return discounted


def senior_discount(total):
    discounted = total - (total * 0.25)
    discounted = round(discounted, 2)
    return discounted


def discount_label(pct: float) -> int:
    return "{}% off".format(int(pct * 100))
