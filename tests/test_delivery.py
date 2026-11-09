from campuseats.delivery import delivery_fee, estimate_eta


def test_medium_distance_fee_off_campus():
    # distance 5 is NOT over the 5km band: it falls in the 2-5km tier (+2.0),
    # with no weight surcharge on a default 1kg order -> pins the > 5 boundary
    assert delivery_fee("1 High St", "Exeter", "EX2", 5) == 2.0


def test_on_campus_is_half_price_not_free():
    # the docstring claims on-campus orders are delivered free; the code only
    # halves the fee -- pin the real behaviour so "fixing" the code to match the
    # docstring (making it free) is caught here
    assert delivery_fee("1 Campus Rd", "Exeter", "EX4", 1) == 0.5


def test_express_heavy_member_long_distance():
    # distance>5 (+3.0), weight>10 (+2.0), express (x2), member (x0.9)
    assert delivery_fee("1 Far Rd", "Truro", "EX2", 8, weight_kg=12, express=True, member=True) == 9.0


def test_eta_includes_address_and_minutes():
    assert estimate_eta("1 High St", "Exeter", "EX2", 1) == "1 High St, Exeter EX2 (15 mins)"


def test_distance_tier_boundaries_are_shared_by_fee_and_eta():
    assert delivery_fee("1 High St", "Exeter", "EX2", 2) == 1.0
    assert delivery_fee("1 High St", "Exeter", "EX2", 2.1) == 2.0
    assert delivery_fee("1 High St", "Exeter", "EX2", 5) == 2.0
    assert delivery_fee("1 High St", "Exeter", "EX2", 5.1) == 3.0

    assert estimate_eta("1 High St", "Exeter", "EX2", 2) == "1 High St, Exeter EX2 (15 mins)"
    assert estimate_eta("1 High St", "Exeter", "EX2", 2.1) == "1 High St, Exeter EX2 (25 mins)"
    assert estimate_eta("1 High St", "Exeter", "EX2", 5) == "1 High St, Exeter EX2 (25 mins)"
    assert estimate_eta("1 High St", "Exeter", "EX2", 5.1) == "1 High St, Exeter EX2 (40 mins)"
