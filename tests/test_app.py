from campuseats.app import checkout, quick_sale


def test_checkout_returns_total_and_points():
    result = checkout(["coffee", "muffin"])
    assert result["total"] == 4.30
    assert result["points"] == 4
    assert result["tier"] == "bronze"
    assert "=== CampusEats ===" in result["receipt"]


def test_quick_sale_reports_note_and_receipt():
    note, receipt = quick_sale("tea")
    assert "tea" in note
    assert "TOTAL" in receipt
