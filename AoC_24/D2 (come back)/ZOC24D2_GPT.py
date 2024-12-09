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
    relevant_data = RD
    return relevant_data  # relevant_data

def is_mostly_increasing(arr):
    count = 0
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            count += 1
            if count > 1:
                return False
    return True

def is_mostly_decreasing(arr):
    count = 0
    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            count += 1
            if count > 1:
                return False
    return True

def is_mostly_sorted(arr):
    return is_mostly_increasing(arr) or is_mostly_decreasing(arr)

def problem2_2(filename):
    with open(filename) as f:
        r = f.read()
    r.strip()

    Rawdata = r.split("\n")
    var_name = process_data(Rawdata)

    safecounter = 0
    for report in var_name:
        if len(report) < 3:
            safecounter += 1
            continue

        report = [int(i) for i in report.split(" ")]

        if is_mostly_sorted(report):
            safecounter += 1
            continue

        for i in range(len(report)):
            temp_report = report[:i] + report[i+1:]
            if is_mostly_sorted(temp_report):
                safecounter += 1
                break

    return safecounter

print(problem2_2(test1))