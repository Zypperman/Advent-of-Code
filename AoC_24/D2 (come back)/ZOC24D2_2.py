"""
def problem_2_1():
    --- Part Two ---
The engineers are surprised by the low number of safe reports until they realize they forgot to tell you about the Problem Dampener.

The Problem Dampener is a reactor-mounted module that lets the reactor safety systems tolerate a single bad level in what would otherwise be a safe report. It's like the bad level never happened!

Now, the same rules apply as before, except if removing a single level from an unsafe report would make it safe, the report instead counts as safe.

More of the above example's reports are now safe:

7 6 4 2 1: Safe without removing any level.
1 2 7 8 9: Unsafe regardless of which level is removed.
9 7 6 2 1: Unsafe regardless of which level is removed.
1 3 2 4 5: Safe by removing the second level, 3.
8 6 4 4 1: Safe by removing the third level, 4.
1 3 6 7 9: Safe without removing any level.
Thanks to the Problem Dampener, 4 reports are actually safe!

Update your analysis by handling situations where the Problem Dampener can remove a single level from unsafe reports. How many reports are now safe?
"""

import os

dirname = os.path.dirname(__file__) + "\\"

test = dirname + "AOC24D2_input.txt"
test1 = dirname + "AOC24D2_test_1.txt"
test2 = dirname + "AOC24D2_test2.txt"
test3 = r"C:\Users\ChunChunMaru\Desktop\Baby code\FeetV2\Advent-of-Code\AoC_24\D2\AOC24D2_test_3.txt"
test4 = r"C:\Users\ChunChunMaru\Desktop\Baby code\FeetV2\Advent-of-Code\AoC_24\D2\AOC24D2_test_4.txt"
test5 = r"C:\Users\ChunChunMaru\Desktop\Baby code\FeetV2\Advent-of-Code\AoC_24\D2\AOC24D2_test_5.txt"


def process_data(RD):
    # * dump data for processing here
    relevant_data = 0
    return RD  # relevant_data


def problem2_2(filename):
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

    safecounter = 0
    for report in var_name:
        # print()
        # print(report)

        if len(report) < 3:
            safe += 1
            continue

        report = [int(i) for i in report.split(" ")]
        # check if first and last 2 elements are descending or not
        front_check = report[1] - report[0]
        back_check = report[-1] - report[-2]

        # lambdas to check if safe range is positive or negative, and in [1,2,3]
        increasing_checker = lambda x, y: bool(-(x - y) in (range(1, 3 + 1)))
        decreasing_checker = lambda x, y: bool((x - y) in range(1, 3 + 1))
        issafe = None  # for initialization

        if front_check > 0 and back_check > 0:
            issafe = increasing_checker
        elif front_check < 0 and back_check < 0:
            issafe = decreasing_checker
        elif (
            front_check == 0 and back_check == 0
        ):  # edge case, if both 0 then alr unsafe
            continue
        else:  # for if first or last element needs to swap
            middle_check = report[len(report) // 2] - report[0]
            if middle_check > 0:
                issafe = increasing_checker
            else:
                issafe = decreasing_checker

        safe = True
        pruned = True
        i = 0
        while i in range(len(report) - 1):
            if not issafe(report[i], report[i + 1]):
                if pruned:
                    safe = False
                    break

                sub1 = True
                sub2 = True
                report2 = report.copy()
                report2.pop(i)
                for j in range(len(report2) - 1):
                    if not issafe(report2[j], report2[j + 1]):
                        sub1 = False

                if sub1 == True:
                    pruned = True
                    continue

                report3 = report.copy()
                report3.pop(i + 1)
                for k in range(len(report3) - 1):
                    if not issafe(report3[k], report3[k + 1]):
                        sub2 = False

                if sub2 == True:
                    pruned = True
                    i += 1
                    continue

            if safe == False:
                break
            i += 1
        if safe:
            safecounter += 1

    return safecounter


print(problem2_2(test1))
# actual: 439
