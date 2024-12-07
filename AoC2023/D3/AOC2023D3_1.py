"""
def problem_3_1():
    --- Day 3: Gear Ratios ---
    You and the Elf eventually reach a gondola lift station; he says the gondola lift will take you up to the water source, but this is as far as he can bring you. You go inside.

    It doesn't take long to find the gondolas, but there seems to be a problem: they're not moving.

    "Aaah!"

    You turn around to see a slightly-greasy Elf with a wrench and a look of surprise. "Sorry, I wasn't expecting anyone! The gondola lift isn't working right now; it'll still be a while before I can fix it." You offer to help.

    The engineer explains that an engine part seems to be missing from the engine, but nobody can figure out which one. If you can add up all the part numbers in the engine schematic, it should be easy to work out which part is missing.

    The engine schematic (your puzzle input) consists of a visual representation of the engine. There are lots of numbers and symbols you don't really understand, but apparently any number adjacent to a symbol, even diagonally, is a "part number" and should be included in your sum. (Periods (.) do not count as a symbol.)

    Here is an example engine schematic:

    467..114..
    ...*......
    ..35..633.
    ......#...
    617*......
    .....+.58.
    ..592.....
    ......755.
    ...$.*....
    .664.598..
    
    In this schematic, two numbers are not part numbers because they are not adjacent to a symbol: 114 (top right) and 58 (middle right). Every other number is adjacent to a symbol and so is a part number; their sum is 4361.

    Of course, the actual engine schematic is much larger. What is the sum of all of the part numbers in the engine schematic?
"""
filename = "C:\\Users\\ChunChunMaru\\Desktop\\Baby code\\FeetV2\\AoC\\AoC2023\\D3\\AOC23D3_input.txt"

test = "C:\\Users\\ChunChunMaru\\Desktop\\Baby code\\FeetV2\\AoC\\AoC2023\\D3\\AOC23D3_test_1.txt"
test2 = "C:\\Users\\ChunChunMaru\\Desktop\\Baby code\\FeetV2\\AoC\\AoC2023\\D3\\AOC23D3_test_2.txt"


def gear_grinder(filename):
    with open(filename) as f:
        r = f.read()
    r.strip()
    
    Rawdata = r.split("\n")

    final = []

    for i in range(len(Rawdata)):
        prevline = ""
        nextline = ""

        cur = Rawdata[i]
        if i != 0:
            prevline = Rawdata[i-1]
        if i != len(Rawdata)-1:
            nextline = Rawdata[i+1]

        builder = ""
        checker = []

        check_for_nums = [char for char in cur if char.isdigit()]
        if not check_for_nums:
            continue

        #writetofile = f"{prevline}\n{cur}\n{nextline}\n"

        for cnum in range(len(cur)):
            char = cur[cnum]

            if char.isdigit():

                builder += char
                # * left
                checker.append(cur[cnum-1]) if cnum-1 > 0 else 0
                # * topleft
                checker.append(prevline[cnum-1]
                               ) if prevline and cnum-1 > 0 else 0
                # * topright
                checker.append(
                    prevline[cnum+1]) if prevline and cnum+1 <= len(cur)-1 else 0
                
                # * right
                checker.append(cur[cnum+1]) if cnum+1 < len(cur)-1 else 0
                #* botleft
                checker.append(nextline[cnum-1]
                               ) if nextline and cnum-1 > 0 else 0
                #* botright
                checker.append(nextline[cnum+1]
                               ) if nextline and cnum+1 <= len(cur)-1 else 0
                
                #* top
                checker.append(prevline[cnum]) if prevline else 0
                #* bottom
                checker.append(nextline[cnum]) if nextline else 0
                if builder == "682":
                        n = 0
            else:

                if builder != '':

                    checker2 = checker[:]
                    checker = [q for q in checker if not q.isdigit()
                               and q != "."]
                    if len(checker) > 0:

                        final.append(int(builder))
                        
                        builder = ''
                        checker = []
                    else:
                        #writetofile += f"\n\tforgot {builder} +\t{checker2}"
                        builder = ""
                        checker2 = []
            
            if cnum == len(cur)-1 and builder != '':
                checker = [q for q in checker if not q.isdigit() and q != "."]
                if len(checker) > 0:
                    final.append(int(builder))
                    
        #writetofile += "\n\n"

        #with open("C:\\Users\\ChunChunMaru\\Desktop\\Baby code\\FeetV2\\AoC\\AoC2023\\D3\\bruh.txt", "a") as f:
        #    f.write(writetofile)

        writetofile = ""

    return sum(final)

print(gear_grinder(filename))

# 102886441323 failed
# 530923 failed
# correct is 533775
