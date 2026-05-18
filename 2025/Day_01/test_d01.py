"""Tests for Day 1 : Secret Entrance"""
import unittest
from day_01 import parse_input, solve_p1, solve_p2

SAMPLE_FILE = "sample_d1.txt"
PART1_RES = 3
PART2_RES = 6

class TestDay01(unittest.TestCase):
    """Test Advent of Code Day 1 solutions"""

    def test_part1_sample(self):
        data = parse_input(SAMPLE_FILE)
        result = solve_part1(data)
        self.assertEqual(result, PART1_RES)

    def test_part2_sample(self):
        data = parse_input(SAMPLE_FILE)
        result = solve_part2(data)
        self.assertEqual(result, PART2_RES)


if __name__ == "__main__":
    unittest.main()
