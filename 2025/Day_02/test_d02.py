"""Tests for Day 2 : Gift Shop"""
import unittest
from day_02 import solve_part1, solve_part2

SAMPLE_FILE = "sample_d2.txt"
PART1_TOTAL = 1227775554
PART1_IDS = 8
PART2_TOTAL = 4174379265
PART2_IDS = 13


class TestDay02(unittest.TestCase):
    """Test Advent of Code Day 1 solutions"""

    def test_part1_sample(self):
        data = parse_input(SAMPLE_FILE)
        total, ids = solve_part1(data)
        self.assertEqual(total, PART1_TOTAL)
        self.assertEqual(ids, PART1_IDS)

    def test_part2_sample(self):
        data = parse_input(SAMPLE_FILE)
        total, ids = solve_part2(data)
        self.assertEqual(total, PART2_TOTAL)
        self.assertEqual(ids, PART2_IDS)


if __name__ == "__main__":
    unittest.main()
