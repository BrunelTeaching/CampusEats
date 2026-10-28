from campuseats.pricing import order_total, priced_order


def test_order_total_sums_items():
    assert order_total(["coffee", "muffin"]) == 4.30


def test_order_total_empty_is_zero():
    assert order_total([]) == 0


def test_priced_order_plain_has_no_change():
    assert priced_order(["coffee", "muffin"]) == 4.30
