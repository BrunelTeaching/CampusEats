from campuseats.receipt import format_line


def test_format_line_pads_name_to_12_columns():
    # pins the ACTUAL width (12), not the 20 the docstring claims
    line = format_line("a", 1.0)
    assert line.startswith("a" + " " * 11)
