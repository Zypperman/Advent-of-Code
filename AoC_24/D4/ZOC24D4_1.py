"""
def problem_4_1():
    --- Day 4: Ceres Search ---
    "Looks like the Chief's not here. Next!" One of The Historians pulls out a device and pushes the only button on it. After a brief flash, you recognize the interior of the Ceres monitoring station!

    As the search for the Chief continues, a small Elf who lives on the station tugs on your shirt; she'd like to know if you could help her with her word search (your puzzle input). She only has to find one word: XMAS.

    This word search allows words to be horizontal, vertical, diagonal, written backwards, or even overlapping other words. It's a little unusual, though, as you don't merely need to find one instance of XMAS - you need to find all of them. Here are a few ways XMAS might appear, where irrelevant characters have been replaced with .:


    ..X...
    .SAMX.
    .A..A.
    XMAS.S
    .X....
    The actual word search will be full of letters instead. For example:

    MMMSXXMASM
    MSAMXMSMSA
    AMXSXMAAMM
    MSAMASMSMX
    XMASAMXAMM
    XXAMMXXAMA
    SMSMSASXSS
    SAXAMASAAA
    MAMMMXMMMM
    MXMXAXMASX
    In this word search, XMAS occurs a total of 18 times; here's the same word search again, but where letters not involved in any XMAS have been replaced with .:

    ....XXMAS.
    .SAMXMS...
    ...S..A...
    ..A.A.MS.X
    XMASAMX.MM
    X.....XA.A
    S.S.S.S.SS
    .A.A.A.A.A
    ..M.M.M.MM
    .X.X.XMASX
    Take a look at the little Elf's word search. How many times does XMAS appear?
"""

import os
import re

dirname = os.path.dirname(__file__) + "\\"

test = dirname + "AOC24D4_input.txt"
test1 = dirname + "AOC24D4_test1.txt"
test2 = dirname + "AOC24D4_test2.txt"


def process_data(RD):
    # * dump data for processing here

    RD = [list(i) for i in RD]

    return RD  # relevant_data


def diagonal_generator(arr):
    width = len(arr[0])
    length = len(arr)

    transposed = False
    if width > length:
        transposed = True
        arr = [[arr[i][j] for i in range(len(arr))] for j in range(len(arr[0]))]

    diag = []
    # add middle rows
    thing = []
    for i in range(1, abs(length - width)):
        thing = [(j + i, j) for j in range(width)]
        diag.append(thing.copy())
    # add top square matrix diagonals

    bottomleftdiag = [[(abs(width - length) + i, i) for i in range(width)]]

    base_bld = bottomleftdiag[0]

    while len(base_bld) != 1:
        base_bld = [(i[0], i[1] - 1) for i in base_bld]
        base_bld.pop(0)
        bottomleftdiag.append(base_bld.copy())

    toprightdiagonal = []

    if width == length:
        base_trd = bottomleftdiag[0]
    else:
        toprightdiagonal = [[(i, i) for i in range(width)]]
        base_trd = toprightdiagonal[0]

    while len(base_trd) != 1:
        base_trd = [(i[0] - 1, i[1]) for i in base_trd]
        base_trd.pop(0)
        # print("added", base_trd.copy())
        toprightdiagonal.append(base_trd.copy())

    diag.extend(bottomleftdiag)
    diag.extend(toprightdiagonal)

    if transposed:
        diag = [[j[::-1] for j in i] for i in diag]

    diag.sort(key=lambda x: (-x[0][0], -len(x)))
    return diag


def problem4_1(filename):
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

    counter = 0
    # get all vertical
    exp1 = "XMAS"
    exp2 = "SAMX"
    exp = "(XMAS)|(SAMX)"

    # get horizontal matches
    horizontals = ["".join(i) for i in var_name]
    # print(horizontals)
    counter = 0
    for i in horizontals:
        doodoo = re.findall(exp1, i)
        doodoo2 = re.findall(exp2, i)
        doodoo3 = re.findall(exp, i)
        # if doodoo or doodoo2:
        # print(i)
        # print(len(doodoo) + len(doodoo2), "horizontals")
        # print(doodoo3)
        counter += len(doodoo) + len(doodoo2)
    # print(f"added {counter} from horizontal search")
    save = counter
    # get vertical matches
    verticals = []
    for i in range(len(var_name)):
        verticals.append("".join([j[i] for j in var_name]))
    # print()
    # print("Verticals:", verticals)

    for i in verticals:
        doodoo = re.findall(exp1, i)
        doodoo2 = re.findall(exp2, i)
        counter += len(doodoo) + len(doodoo2)

    # print(f"added {counter-save} from vertical search")
    save = counter

    # get forward diagonals
    fdcoords = diagonal_generator(var_name)
    fd = []

    print("fdcoords")
    for i in fdcoords[:5]:
        print(i)
    print()

    for i in range(len(fdcoords)):
        string = "".join([var_name[j[0]][j[1]] for j in fdcoords[i]])
        print(string)
        fd.append(string)

    for i in fd:
        doodoo = re.findall(exp1, i)
        doodoo2 = re.findall(exp2, i)
        counter += len(doodoo) + len(doodoo2)

    print(f"added {counter-save} from frontslash search")
    save = counter

    var_name2 = [
    [row[len(var_name[0]) - i - 1] for row in var_name]
    for i in range(max(len(r) for r in var_name))
]

    rd = []
    for i in range(len(fdcoords)):
        string = "".join([var_name2[j[0]][j[1]] for j in fdcoords[i]])
        print(string)
        rd.append(string)

    for i in rd:
        doodoo = re.findall(exp1, i)
        doodoo2 = re.findall(exp2, i)
        counter += len(doodoo) + len(doodoo2)

    print(f"added {counter-save} from frontslash search")

    return counter


print(problem4_1(test1))
