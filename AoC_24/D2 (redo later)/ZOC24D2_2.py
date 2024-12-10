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
test2 = dirname + "AOC24D2_test_2.txt"
test3 = dirname + "AOC24D2_test_3.txt"
test4 = dirname + "AOC24D2_test_4.txt"
test5 = dirname + "AOC24D2_test_5.txt"


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

    def ascending_or_descending(report):
        front_check = report[1] - report[0]
        back_check = report[-1] - report[-2]

        increasing_checker = lambda x, y: bool(-(x - y) in (range(1, 3 + 1)))
        decreasing_checker = lambda x, y: bool((x - y) in range(1, 3 + 1))

        if front_check > 0 and back_check > 0 or (front_check == 0 and back_check == 0):
            issafe = increasing_checker
        elif front_check < 0 and back_check < 0:
            issafe = decreasing_checker
        else:  # for if first or last element needs to swap
            middle_check = report[len(report) // 2] - report[0]
            if middle_check > 0:
                issafe = increasing_checker
            else:
                issafe = decreasing_checker
        return issafe

    safecounter = 0
    global_safe = False
    for report in var_name:
        text = report
        report = [int(i) for i in report.split(" ")]
        issafe = ascending_or_descending(report)  # for initialization
        safe = True
        # get first error if any
        for i in range(len(report) - 2):
            if not issafe(report[i], report[i + 1]):
                safe = False
                isolate = i
                break

        if safe:
            print("no edits required, pass")
            safecounter += 1
            continue

        print()
        print(text)
        print("isolated term:", f"item {isolate}", report[isolate])

        remove_candidates = [0, len(report) - 1, isolate, isolate + 1]
        labels = ["start", "end", "isolate", "isolate + 1"]
        global_safe = False
        for i in range(len(remove_candidates)):
            localsafe = True
            report_modded = report.copy()
            report_modded.pop(remove_candidates[i])
            issafe = ascending_or_descending(report_modded)

            for j in range(len(report_modded) - 1):
                if not issafe(report_modded[j], report_modded[j + 1]):
                    print(
                        f"unsafe at {labels[i]}, item {j}({report_modded[j]}) and item {j+1} ({report_modded[j+1]} (diff by {abs(report_modded[j] - report_modded[j+1])}))"
                    )
                    localsafe = False
                    break

            if localsafe:
                print("works at", labels[i])
                global_safe = True
                break

            print("global safe is", global_safe)

        if global_safe:
            print("added to count")
            safecounter += 1
            continue

    return safecounter

print(problem2_2(test1))
# actual: 439
