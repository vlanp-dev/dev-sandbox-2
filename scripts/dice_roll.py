#!/usr/bin/env python3
"""Roll a set of dice from the command line.

Usage: python3 dice_roll.py COUNT FACES

Prints one line per die and a total. Example: python3 dice_roll.py 3 6
"""

import argparse
import random


def parse_args(argv=None):
    """Parse and validate the die count and face count."""
    parser = argparse.ArgumentParser(
        description="Roll COUNT dice that each have FACES faces.",
        epilog="Example: python3 dice_roll.py 3 6",
    )
    parser.add_argument(
        "count",
        type=int,
        help="number of dice to roll (at least 1)",
    )
    parser.add_argument(
        "faces",
        type=int,
        help="number of faces on each die (at least 2)",
    )
    args = parser.parse_args(argv)

    if args.count < 1:
        parser.error("die count must be at least 1 (got {})".format(args.count))
    if args.faces < 2:
        parser.error("face count must be at least 2 (got {})".format(args.faces))
    return args


def main(argv=None):
    """Roll the dice, report each result, and report the total."""
    args = parse_args(argv)

    rolls = [random.randint(1, args.faces) for _ in range(args.count)]
    for index, value in enumerate(rolls, start=1):
        print("Die {}: {}".format(index, value))
    print("Total: {}".format(sum(rolls)))
    return 0


if __name__ == "__main__":
    main()
