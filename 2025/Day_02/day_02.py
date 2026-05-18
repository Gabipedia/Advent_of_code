# -*- coding: utf-8 -*-
"""
Created on Tue Dec  2 08:30:39 2025
@author: Gabriel Guillocheau
"""
import math
from textwrap import wrap
from pathlib import Path


# --- Configuration ---

INPUT_FILE = "input_d2.txt"

# --- Utilities ---

def parse_ranges(filepath: str) -> list[tuple[int, int]]:
    """Parse a comma-separated list of ranges from a file."""
    content = Path(filepath).read_text()
    ranges = []
    for id_range in content.split(","):
        first, last = id_range.strip().split("-")
        ranges.append((int(first), int(last)))
    return ranges


def iter_ids(ranges: list[tuple[int, int]]):
    """Yield every integer ID from a list of inclusive ranges."""
    for first, last in ranges:
        yield from range(first, last + 1)


def digit_count(n: int) -> int:
    """Return the number of digits in a non-negative integer."""
    if n == 0:
        return 1
    return math.floor(math.log10(abs(n))) + 1


def factor_list(length: int) -> list[int]:
    """
    Return all factors of `length` (excluding 1 and itself),
    sorted in descending order, with 1 appended at the end.
    """
    factors = [i for i in range(2, length) if length % i == 0]
    return factors[::-1] + [1]


# --- Part 1 ---

def has_even_digits(n: int) -> bool:
    """Return True if `n` has an even number of digits."""
    return digit_count(n) % 2 == 0


def is_repeated(n: int) -> bool:
    """Return True if the first half of the digit string equals the second half."""
    pid = str(n)
    mid = len(pid) // 2
    return pid[:mid] == pid[mid:]


def solve_part1(ranges: list[tuple[int, int]]) -> tuple[int, list[int]]:
    """Return the sum and list of invalid IDs according to Part 1 rules."""
    invalid = [pid for pid in iter_ids(ranges)
        if has_even_digits(pid) and is_repeated(pid)]
    return sum(invalid), invalid


# --- Part 2 ---

def is_uniform_split(n: int) -> bool:
    """
    Return True if the digit string can be split into equal repeated chunks
    for any valid factor of its length.
    """
    pid = str(n)
    return any(
        len(set(wrap(pid, f))) == 1
        for f in factor_list(len(pid))
    )


def solve_part2(ranges: list[tuple[int, int]]) -> tuple[int, list[int]]:
    """Return the sum and list of invalid IDs according to Part 2 rules."""
    invalid = [
        pid for pid in iter_ids(ranges)
        if pid >= 11 and is_uniform_split(pid)
    ]
    return sum(invalid), invalid


# --- Main ---

def main():
    ranges = parse_ranges(INPUT_FILE)

    total1, ids1 = solve_part1(ranges)
    print(f"[Part 1] Sum: {total1} — {len(ids1)} invalid ID(s) found")

    total2, ids2 = solve_part2(ranges)
    print(f"[Part 2] Sum: {total2} — {len(ids2)} invalid ID(s) found")


if __name__ == "__main__":
    main()
