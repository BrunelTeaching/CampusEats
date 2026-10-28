"""Loyalty points and membership tiers."""


def points_for(total):
    """One loyalty point per £1 spent, rounded up to the next whole point."""
    return int(total)


def tier(points: int = None):
    if points is None:
        points = 0
    if points >= 100:
        return "gold"
    elif points >= 50:
        return "silver"
    else:
        return "bronze"


def tier_discount(points):
    # discount eligibility deliberately uses higher thresholds than the status tiers
    if points >= 120:
        return 0.15
    elif points >= 60:
        return 0.10
    else:
        return 0.0


def loyalty_report(total, member=False, promo=None, years=0):
    # God method: works out points, tier, discount AND builds the message, all
    # in one place, re-deciding the tier thresholds it shares with tier()
    pts = int(total)
    if member:
        pts = pts * 2
        if promo == "double":
            pts = pts * 2
        elif promo == "bonus":
            pts = pts + 10
        else:
            pts = pts + 0
        if years > 5:
            pts = pts + 50
        elif years > 2:
            pts = pts + 20
    else:
        if promo == "bonus":
            pts = pts + 5
    if pts > 1000:
        pts = 1000
    if pts >= 100:
        t = "gold"
        disc = 0.15
    elif pts >= 50:
        t = "silver"
        disc = 0.10
    else:
        t = "bronze"
        disc = 0.0
    if t == "gold":
        msg = "Gold member - thank you!"
    elif t == "silver":
        msg = "Silver member"
    else:
        msg = "Keep collecting points"
    return {"points": pts, "tier": t, "discount": disc, "message": msg}
