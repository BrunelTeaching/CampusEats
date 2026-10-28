# CampusEats

A small ordering app for the campus cafe, and the shared codebase for the
CS3616 refactoring coursework.

The test suite passes as shipped. Coverage on the individual modules is **thin by
design**, and several modules carry genuine software-engineering issues. Your job
is to analyse your **assigned** module with the tools, then refactor it without
changing what it does.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
pytest -v
```

## Layout

```
campuseats/
  app.py          # application wiring — calls into every module (a real caller)
  cart.py         # shopping cart — calls pricing, menu, discounts
  cli.py          # tiny command-line front end — calls app
  menu.py         # menu data and item lookups
  pricing.py      # order totals, member tiers, promo codes
  discounts.py    # discount rules per customer type
  loyalty.py      # loyalty points and membership tiers
  receipt.py      # receipt formatting
  inventory.py    # stock tracking and restock logic
tests/            # the passing suite (thin coverage on the modules above)
```

## Your assigned module

Your module is assigned by **student ID mod 6** — you do not choose it:

| ID mod 6 | Module |
|---|---|
| 0 | `campuseats/pricing.py` |
| 1 | `campuseats/discounts.py` |
| 2 | `campuseats/receipt.py` |
| 3 | `campuseats/loyalty.py` |
| 4 | `campuseats/menu.py` |
| 5 | `campuseats/inventory.py` |

Run the **three core tools** on your module — `ruff`, `radon` and `pytest-cov` —
**before and after** your refactoring, and save each tool's output. Working out
which of their findings actually matter for your module is part of the task.
(`mypy` and `vulture` are also installed if you want to look further, but only the
three core tools are required.)

- **`CHECKLIST.html`** — the before-you-start → before-you-submit checklist. Start here.
- **`Submission.docx`** — the one-page Word report you fill in and hand back.

Full requirements and marking criteria are in the Coursework Brief on Brightspace.
