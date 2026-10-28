from campuseats.discounts import (
    bulk_discount,
    senior_discount,
    staff_discount,
    student_discount,
)


def test_student_discount_small_order():
    assert student_discount(10.0) == 8.0


def test_student_discount_is_capped_at_5_pounds():
    # the student discount never exceeds £5, even on a large order
    assert student_discount(100.0) == 95.0


def test_other_discounts_are_plain_percentages():
    assert staff_discount(100.0) == 85.0
    assert bulk_discount(100.0) == 90.0
    assert senior_discount(100.0) == 75.0
