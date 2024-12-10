"""
def problem_3_1():
    --- Day 3: Mull It Over ---
    "Our computers are having issues, so I have no idea if we have any Chief Historians in stock! You're welcome to check the warehouse, though," says the mildly flustered shopkeeper at the North Pole Toboggan Rental Shop. The Historians head out to take a look.

    The shopkeeper turns to you. "Any chance you can see why our computers are having issues again?"

    The computer appears to be trying to run a program, but its memory (your puzzle input) is corrupted. All of the instructions have been jumbled up!

    It seems like the goal of the program is just to multiply some numbers. It does that with instructions like mul(X,Y), where X and Y are each 1-3 digit numbers. For instance, mul(44,46) multiplies 44 by 46 to get a result of 2024. Similarly, mul(123,4) would multiply 123 by 4.

    However, because the program's memory has been corrupted, there are also many invalid characters that should be ignored, even if they look like part of a mul instruction. Sequences like mul(4*, mul(6,9!, ?(12,34), or mul ( 2 , 4 ) do nothing.

    For example, consider the following section of corrupted memory:

    xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
    Only the four highlighted sections are real mul instructions. Adding up the result of each instruction produces 161 (2*4 + 5*5 + 11*8 + 8*5).

    Scan the corrupted memory for uncorrupted mul instructions. What do you get if you add up all of the results of the multiplications?
"""

import os
import re

dirname = os.path.dirname(__file__) + "\\"

test = dirname + "AOC24D3_input.txt"
test1 = dirname + "AOC24D3_test_1.txt"


def process_data(RD):
    # * dump data for processing here
    relevant_data = 0
    return RD  # relevant_data


def problem3_1(filename):
    with open(filename) as f:
        r = f.read()
    r.strip()

    Rawdata = r.split("\n")

    # * processing data
    #! swap out with actual var names
    var_name = process_data(Rawdata)
    # * to test if code works, comment out when running input
    # print(f"data looks like:\n{var_name}")
    # ? Dump solution here

    print(Rawdata[-1])

    exp = "mul\([0-9]{1,3},[0-9]{1,3}\)"
    total = 0
    muls = []

    for i in Rawdata:
        print()
        print(i)

    for i in Rawdata:
        get_all_muls = re.findall(exp, i)
        muls.clear()
        
        print(get_all_muls)
        for j in get_all_muls:
            digits = j.split("(")[1].split(")")[0].split(",")
            muls.append(int(digits[0]) * int(digits[1]))

        print(muls)
        total += sum(muls)
    return total


print(problem3_1(test1))
