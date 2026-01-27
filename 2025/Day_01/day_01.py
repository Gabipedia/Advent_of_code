# -*- coding: utf-8 -*-
"""
Created on Mon Dec  1 09:44:57 2025

@author: Gabriel Guillocheau
"""
from pathlib import Path

START_DIAL_VALUE = 50
INPUT_FILE = "input_d1.txt"


def parse_input(input_file):
    with open(Path(__file__).parent.joinpath(input_file), 'r') as file:
        input_list = [int(line.strip().replace("L", "-").replace("R", "")) for line in file]
    return(input_list)


def solve1(input_list, dial_value=START_DIAL_VALUE):
    zeros_counter = 0
    for rotation in input_list:
        dial_value = (dial_value + rotation)%100
        if dial_value == 0:
            zeros_counter += 1
    return(zeros_counter)


def solve2(input_list, dial_value=START_DIAL_VALUE):
    zeros_counter = 0
    for rotation in input_list:
        current_rotation = dial_value + rotation
        if current_rotation < 0:
            if dial_value != 0:
                zeros_counter += 1
            zeros_counter += abs(current_rotation)//100
            dial_value = current_rotation%100
        elif current_rotation > 99:
            zeros_counter += current_rotation//100
            dial_value = current_rotation%100
        else:
            dial_value = current_rotation%100
            if dial_value == 0:
                zeros_counter += 1
    return(zeros_counter)


if __name__ == "__main__":
    print(f"Result day 1 - part1: {solve1(parse_input(INPUT_FILE))}")
    print(f"Result day 1 - part2: {solve2(parse_input(INPUT_FILE))}")
