"""A tiny command-line front end. A second real caller of the app layer."""

import sys

from campuseats.app import checkout


def main(argv=None):
    argv = argv if argv is not None else sys.argv[1:]
    items = argv or ["coffee", "muffin"]
    result = checkout(items)
    print(result["receipt"])
    print(f"Points earned: {result['points']} ({result['tier']})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
