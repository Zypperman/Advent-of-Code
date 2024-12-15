"""
def problem_4_2():
    --- Part Two ---
    The Elf looks quizzically at you. Did you misunderstand the assignment?

    Looking for the instructions, you flip over the word search to find that this isn't actually an XMAS puzzle; it's an X-MAS puzzle in which you're supposed to find two MAS in the shape of an X. One way to achieve that is like this:

    M.S
    .A.
    M.S
    Irrelevant characters have again been replaced with . in the above diagram. Within the X, each MAS can be written forwards or backwards.

    Here's the same example from before, but this time all of the X-MASes have been kept instead:

    .M.S......
    ..A..MSMS.
    .M.S.MAA..
    ..A.ASMSM.
    .M.S.M....
    ..........
    S.S.S.S.S.
    .A.A.A.A..
    M.M.M.M.M.
    ..........
    In this example, an X-MAS appears 9 times.

    Flip the word search from the instructions back over to the word search side and try again. How many times does an X-MAS appear?
"""

import os
import re

dirname = os.path.dirname(__file__) + "\\"

tes = dirname + "AOC24D4_input2.txt"
test = dirname + "AOC24D4_input.txt"
test1 = dirname + "AOC24D4_test1.txt"


def process_data(RD):
    # * dump data for processing here
    relevant_data = 0
    return [list(i) for i in RD]  # relevant_data


def detect_mas(arr):
    """
    modified from part 1, checks for crossings now
    """

    if not arr:
        return 0

    if arr[1][1] != "A":
        return 0

    counter = 0
    # get all vertical
    exp1 = "MAS"
    exp2 = "SAM"

    has_MAS = lambda x: bool(exp1 in "".join(x) or exp2 in "".join(x))

    # check forward diagonals
    bs = "".join([arr[i][j] for i in range(3) for j in range(3) if i == j])
    fs = "".join([arr[2 - i][j] for i in range(3) for j in range(3) if i == j])

    if has_MAS(bs) and has_MAS(fs):
        counter += 1

    return counter


def get_mas_kernel_input(arr, corner_x, corner_y):
    # check array requirements
    length = len(arr)
    width = len(arr[0])
    if (width - corner_x) < 3:
        return []
    if (width - corner_y) < 3:
        return []

    kernel = []
    for i in range(3):
        kernel.append(arr[corner_x + i][corner_y : corner_y + 3])
    return kernel


def problem4_2(filename):
    with open(filename) as f:
        r = f.read()
    r.strip()
    Rawdata = r.split("\n")

    # * processing data
    #! swap out with actual var names
    data = process_data(Rawdata)
    # * to test if code works, comment out when running input
    # print(f"data looks like:\n{data}")
    # ? Dump solution here

    length = len(data)
    width = len(data[0])
    counter = 0

    for row in range(length):
        for col in range(width):
            arr = get_mas_kernel_input(data, row, col)
            # print("resulted in")
            # for i in arr:
            #    print(i)
            num = detect_mas(arr)
            if num:
                print(f"checking {row} {col}")
                print(f"found {detect_mas(arr)} MAS")
                for i in arr:
                    print(i)
                print()
                counter += num
    return counter

print(problem4_2(test1))
