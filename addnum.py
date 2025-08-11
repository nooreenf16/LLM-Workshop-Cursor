"""Simple utility to add two numbers.

This module exposes a reusable function `add_numbers` and can also be used
as a command-line program:

    python addnum.py 2 3

It will print the sum of the two numbers.
"""

from typing import Union
import argparse

Number = Union[int, float]


def add_numbers(first_number: Number, second_number: Number) -> Number:
    """Return the sum of two numbers.

    Args:
        first_number: The first addend, integer or float.
        second_number: The second addend, integer or float.

    Returns:
        The arithmetic sum of the two numbers.
    """
    return first_number + second_number


def _parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Add two numbers and print the result.")
    parser.add_argument("a", type=float, help="First number")
    parser.add_argument("b", type=float, help="Second number")
    return parser.parse_args()


def main() -> None:
    args = _parse_arguments()
    result = add_numbers(args.a, args.b)
    print(result)


if __name__ == "__main__":
    main()