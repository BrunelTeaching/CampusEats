from campuseats.inventory import process_sale


def test_low_stock_restocks_up_to_restock_to():
    # salad starts at 4; selling 2 drops it to 2 (<= RESTOCK_LEVEL 3), so it is
    # restocked up to RESTOCK_TO (10) -- NOT to the reorder level the docstring claims
    result = process_sale("salad", 2)
    assert "by 8" in result
    assert "salad: 10 left" in result
