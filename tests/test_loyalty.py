from campuseats.loyalty import loyalty_report, points_for, tier, tier_discount


def test_points_for_whole_pounds():
    assert points_for(4.30) == 4


def test_tier_bronze_for_small_balance():
    assert tier(10) == "bronze"


def test_tier_discount_thresholds_differ_from_status_tiers():
    # at 100 points you are 'gold' status, but not yet eligible for the 15% discount
    assert tier(100) == "gold"
    assert tier_discount(100) == 0.10
    assert tier_discount(120) == 0.15


def test_loyalty_report_sets_its_own_discount_at_100_50_thresholds():
    # loyalty_report decides the discount at 100/50, NOT the tier_discount 120/60
    # thresholds -- pin it so unifying the two (a behaviour change) is caught here
    assert loyalty_report(100, False)["discount"] == 0.15
    assert loyalty_report(60, False)["discount"] == 0.10
