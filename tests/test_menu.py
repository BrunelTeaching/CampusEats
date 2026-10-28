from campuseats.menu import MENU, describe_item, getPrice


def test_menu_has_expected_items():
    assert "coffee" in MENU
    assert "sandwich" in MENU


def test_get_price_known_item():
    assert getPrice("coffee") == 2.50


def test_get_price_unknown_returns_zero():
    # pins the ACTUAL behaviour: unknown items return 0.0, they do not raise
    assert getPrice("rocket fuel") == 0.0


def test_vat_rate_food_zero_drink_standard():
    # pins the ACTUAL behaviour: food is zero-rated, drinks are standard-rated
    assert describe_item("salad", "vat") == 0.0
    assert describe_item("coffee", "vat") == 0.20
