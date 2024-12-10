"""
def problem_3_2():
    --- Part Two ---
    As you scan through the corrupted memory, you notice that some of the conditional statements are also still intact. If you handle some of the uncorrupted conditional statements in the program, you might be able to get an even more accurate result.

    There are two new instructions you'll need to handle:

    The do() instruction enables future mul instructions.
    The don't() instruction disables future mul instructions.
    Only the most recent do() or don't() instruction applies. At the beginning of the program, mul instructions are enabled.

    For example:

    xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
    This corrupted memory is similar to the example from before, but this time the mul(5,5) and mul(11,8) instructions are disabled because there is a don't() instruction before them. The other mul instructions function normally, including the one at the end that gets re-enabled by a do() instruction.

    This time, the sum of the results is 48 (2*4 + 8*5).

    Handle the new instructions; what do you get if you add up all of the results of just the enabled multiplications?
"""

import os
import re

dirname = os.path.dirname(__file__) + "\\"

test = dirname + "AOC24D3_test2.txt"
test1 = dirname + "AOC24D3_test_1.txt"


def process_data(RD):
    # * dump data for processing here

    relevant_data = 0

    return RD  # relevant_data


def problem3_2(filename):
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

    # print(Rawdata[-1])

    exp = "(mul\([0-9]{1,3},[0-9]{1,3}\)|don't\(\)|do\(\))"
    total = 0
    muls = []

    toggle = True
    for i in Rawdata:
        get_all_muls = re.findall(exp, i)
        muls.clear()
        print(get_all_muls)
        for i in get_all_muls:
            # print(i)
            if i == "don't()":
                toggle = False
                continue
            if i == "do()":
                toggle = True
                continue
            print("Toggle:", toggle)
            if toggle == True:
                print(i)
            if toggle == True:
                digits = i.split("(")[1].split(")")[0].split(",")
                muls.append(int(digits[0]) * int(digits[1]))
            else:
                continue

        print(muls)
        total += sum(muls)
    return total


print(problem3_2(test1))
# 85711693 too high
