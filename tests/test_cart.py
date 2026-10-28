from campuseats.cart import Cart


def test_cart_subtotal_sums_items():
    cart = Cart()
    cart.add("coffee")
    cart.add("muffin")
    assert cart.subtotal() == 4.30


def test_cart_empty_subtotal_is_zero():
    assert Cart().subtotal() == 0


def test_cart_student_total_applies_discount():
    cart = Cart()
    cart.add("coffee")
    cart.add("muffin")
    assert cart.student_total() == 3.44
