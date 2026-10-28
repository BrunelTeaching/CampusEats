"""A small shopping cart that ties the menu, pricing, and discounts together.

This module is deliberately clean — it is one of the real callers of the pricing,
menu, and discounts modules.
"""

from campuseats.discounts import student_discount
from campuseats.pricing import order_total


class Cart:
    def __init__(self) -> None:
        self.items: list[str] = []

    def add(self, item: str) -> None:
        self.items.append(item)

    def subtotal(self) -> float:
        return order_total(self.items)

    def student_total(self) -> float:
        return student_discount(self.subtotal())
