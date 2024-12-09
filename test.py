report = "7 6 4 2 1"

trigger = True
report = [int(i) for i in report.split(" ")]
front_check = report[1] - report[0]
back_check = report[-1] - report[-2]
# for verifying if the list is ascending or descending without sorting
# if the difference between the first two numbers is positive, the list is ascending
if front_check > 0 and back_check > 0:
    f = lambda x, y: bool(-(x - y) in (range(1, 3 + 1)))
elif front_check <= 0 and back_check > 0:
    f = lambda x, y: bool((x - y) in range(1, 3 + 1))
else:
    middle_check = report[len(report) // 2] - report[0]
    if middle_check > 0:
        f = lambda x, y: bool(-(x - y) in range(1, 3 + 1))
    else:
        f = lambda x, y: bool((x - y) in range(1, 3 + 1))

print(report)
for value in range(len(report) - 1):

    if not f(report[value], report[value + 1]):
        if (value + 1) == len(report) - 1:

            continue
        if not f(report[value], report[value + 2]):

            trigger = False
            break
        else:

            continue

if trigger == False:
    print("unsafe:", report)
else:
    print("safe")
