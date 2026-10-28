"""Menu data and item lookups."""

MENU = {
    "coffee": 2.50,
    "sandwich": 3.75,
    "muffin": 1.80,
    "juice": 2.00,
    "tea": 1.90,
    "salad": 4.20,
}

CATEGORY = {
    "coffee": "drink",
    "tea": "drink",
    "juice": "drink",
    "sandwich": "food",
    "muffin": "food",
    "salad": "food",
}


def describe_item(name, want="price", discount=None):
    # one function doing many unrelated jobs: price, category, drink check, VAT,
    # and labelling -- dispatched on a string code
    n = name.lower()
    if want == "price":
        if n in MENU:
            p = MENU[n]
            if discount == "student":
                return round(p * 0.8, 2)
            elif discount == "staff":
                return round(p * 0.85, 2)
            else:
                return p
        else:
            return 0.0
    elif want == "category":
        if n in CATEGORY:
            return CATEGORY[n]
        else:
            return "unknown"
    elif want == "is_drink":
        if n in CATEGORY:
            if CATEGORY[n] == "drink":
                return True
            else:
                return False
        else:
            return False
    elif want == "vat":
        # drinks are zero-rated; food is standard-rated at 20%
        if n in CATEGORY:
            if CATEGORY[n] == "food":
                return 0.0
            else:
                return 0.20
        else:
            return 0.20
    elif want == "label":
        if n in MENU:
            p = MENU[n]
            if p > 3:
                return name.title() + " (premium)"
            elif p > 2:
                return name.title()
            else:
                return name.title() + " (value)"
        else:
            return "Unknown item"
    else:
        return None


def getPrice(name):
    """Return the item's price, or raise KeyError if the item is not on the menu."""
    return describe_item(name, "price")


def is_drink(name: str = None):
    return describe_item(name, "is_drink")


def category_of(name: str = None):
    return describe_item(name, "category")
