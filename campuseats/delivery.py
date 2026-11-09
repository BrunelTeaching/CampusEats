"""Delivery fees and dispatch estimates for campus orders."""

from bisect import bisect_left

CAMPUS_POSTCODES = {"EX4", "EX1", "TR10"}
DISTANCE_THRESHOLDS = (2, 5)
DISTANCE_BANDS = ((1.0, 15), (2.0, 25), (3.0, 40))


def _distance_band(distance_km):
    return DISTANCE_BANDS[bisect_left(DISTANCE_THRESHOLDS, distance_km)]


def is_on_campus(postcode):
    if postcode in CAMPUS_POSTCODES:
        return True
    return False


def format_address(street, city, postcode):
    return f"{street}, {city} {postcode}"


def delivery_fee(
    street,
    city,
    postcode,
    distance_km,
    weight_kg: float = None,
    express=False,
    member=False,
):
    """Return the delivery fee in GBP. On-campus orders are delivered free."""
    # Long parameter list / address data clump: street+city+postcode travel
    # together through every function but are never grouped. Nested distance and
    # weight tiers with magic numbers drive the fee up.
    if weight_kg is None:
        weight_kg = 1.0
    base_fee, _ = _distance_band(distance_km)
    fee = base_fee
    if weight_kg > 10:
        fee = fee + 2.0
    elif weight_kg > 5:
        fee = fee + 1.0
    if express:
        fee = fee * 2
    if is_on_campus(postcode):
        fee = fee * 0.5
    if member:
        fee = fee * 0.9
    return round(fee, 2)


def estimate_eta(street, city, postcode, distance_km, express=False):
    _, mins = _distance_band(distance_km)
    if express:
        mins = int(mins / 2)
    return f"{format_address(street, city, postcode)} ({mins} mins)"
