"""
def problem_1_2():
    --- Part Two ---
    Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

    Equipped with this new information, you now need to find the real first and last digit on each line. For example:

    two1nine
    eightwothree
    abcone2threexyz
    xtwone3four
    4nineeightseven2
    zoneight234
    7pqrstsixteen
    In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.

    What is the sum of all of the calibration values?
"""

filename = "C:\\Users\\ChunChunMaru\\Desktop\\Baby code\\FeetV2\\AoC\\AoC2023\\D1\\AOC23D1_input.txt"

test = "C:\\Users\\ChunChunMaru\\Desktop\\Baby code\\FeetV2\\AoC\\AoC2023\\D1\\AOC23D1_test_2.txt"


def sky_coords2(filename):
    with open(filename) as f:
        r = f.read()
    r.strip()
    R = r.split("\n")

    worddict = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }

    final = []

    for i in R:
        stor = []

        sep = ""
        for q in range(len(i)):
            sep += i[q]
            for thing in worddict.keys():
                if thing in sep:
                    sep = sep.replace(thing, worddict[thing])

        for q in sep:
            if q.isdigit():
                stor.append(q)
                break

        S = i[::-1]
        sep = ''

        for q in range(len(S)):
            check = True
            sep += S[q]
            if S[q].isdigit():
                stor.append(S[q])
                break
            for thing in worddict.keys():
                if thing in sep[::-1]:
                    stor.append(worddict[thing])
                    check = False
                    break
            if check == False:
                break

        thing = int(''.join(stor))
        # print(i, sep, thing,"\n")
        final.append(thing)

    # return final
    return sum(final)


print(sky_coords2(filename))
# expect 281
