"""
def problem_3_2():
--- Part Two ---
The engineer finds the missing part and installs it in the engine! As the engine springs to life, you jump in the closest gondola, finally ready to ascend to the water source.

You don't seem to be going very fast, though. Maybe something is still wrong? Fortunately, the gondola has a phone labeled "help", so you pick it up and the engineer answers.

Before you can explain the situation, she suggests that you look out the window. There stands the engineer, holding a phone in one hand and waving with the other. You're going so slowly that you haven't even left the station. You exit the gondola.

The missing part wasn't the only issue - one of the gears in the engine is wrong. A gear is any * symbol that is adjacent to exactly two part numbers. Its gear ratio is the result of multiplying those two numbers together.

This time, you need to find the gear ratio of every gear and add them all up so that the engineer can figure out which gear needs to be replaced.

Consider the same engine schematic again:
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

In this schematic, there are two gears. The first is in the top left; it has part numbers 467 and 35, so its gear ratio is 16345. The second gear is in the lower right; its gear ratio is 451490. (The * adjacent to 617 is not a gear because it is only adjacent to one part number.) Adding up all of the gear ratios produces 467835.

What is the sum of all of the gear ratios in your engine schematic?
"""
filename = "C:\\Users\\ChunChunMaru\\Desktop\\Baby code\\FeetV2\\AoC\\AoC2023\\D3\\AOC23D3_input.txt"

test = "C:\\Users\\ChunChunMaru\\Desktop\\Baby code\\FeetV2\\AoC\\AoC2023\\D3\\AOC23D3_test_1.txt"
test2 = "C:\\Users\\ChunChunMaru\\Desktop\\Baby code\\FeetV2\\AoC\\AoC2023\\D3\\AOC23D3_test_2.txt"


def gear_grinder_2(filename):
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

        check_for_stars = [char for char in cur if char == "*"]
        if not check_for_stars:
            continue

        # writetofile = f"{prevline}\n{cur}\n{nextline}\n"

        for cnum in range(len(cur)):
            char = cur[cnum]

            if char == "*":
                # . checker => checking list = [left, right, top left, top, top right, bottom left, bottom, bottom right]
                checker2 = [4, 6, 7, 8, 9, 1, 2, 3]
                checker = dict.fromkeys(checker2)
                # * corresponds to numpad
                # . basic => tracks number of valid nums near gear
                basic = 0
                # - 4 - Left
                checker[4] = cur[cnum-1] if cnum-1 > 0 else "."
                basic += 1 if checker[4].isdigit() else 0
                left = True if checker[4].isdigit() else False
                # - 6 - Right
                checker[6] = cur[cnum+1] if cnum+1 < len(cur)-1 else "."
                basic += 1 if checker[6].isdigit() else 0
                right = True if checker[6].isdigit() else False

                if prevline:  # - toprow
                    # - 7 - Top left
                    checker[7] = prevline[cnum-1] if cnum-1 > 0 else "."
                    # - 8 - Top
                    checker[8] = prevline[cnum]
                    # - 9 - Top Right
                    checker[9] = prevline[cnum+1] if cnum + \
                        1 < len(cur)-1 else "."

                    top = [checker[7], checker[8], checker[9]]
                    topcount = 0
                    topfilter = [g for g in top if g != None and g.isdigit()]
                    if len(topfilter)==0:
                        topcount+= 0
                    elif len(topfilter) == 2 and top[1] == ".":
                        topcount+= 2
                    else:
                        topcount += 1

                    basic += topcount
                    toprow = True if topcount >0 else False

                if nextline:  # - bottomrow
                    # - 1 - Bottom Left
                    checker[1] = nextline[cnum-1] if cnum-1 > 0 else "."
                    # - 2 - Bottom
                    checker[2] = nextline[cnum]
                    # - 3 - Bottom Right
                    checker[3] = nextline[cnum+1] if cnum + \
                        1 < len(cur)-1 else "."
                        
                    bot = [checker[1], checker[2], checker[3]]
                    botcount = 0
                    botfilter = [g for g in bot if g != None and g.isdigit()]
                    if len(botfilter)==0:
                        botcount+= 0
                    elif len(botfilter) == 2 and bot[1] == ".":
                        botcount+= 2
                    else:
                        botcount += 1

                    basic += botcount
                    botrow = True if botcount >0 else False

                if basic != 2:
                    continue

                nums = []
                if left:
                    getnum = cur[:cnum]
                    nums.append(getnum.split(".")[-1])

                if right:
                    getnum = cur[cnum+1:]
                    nums.append(getnum.split(".")[0])

                #* for top and bottom rows, make sure they have 
                if toprow:
                    # ? screw it we just use top and bot.
                    if topcount == 2:
                            getnum = prevline[cnum-3:cnum+4]
                            nums.extend([bruh for bruh in getnum.split(".") if bruh != ''])
                    
                    if topcount ==1:
                        if (''.join(top)).isdigit():
                            nums.append(''.join(top))
                        elif top[0] != ".":
                            getnum = prevline[cnum-3:cnum+1]
                            nums.append([bruh for bruh in getnum.split(".") if bruh != ''][-1])
                            if len(nums)>2:
                                n = 0
                        elif top[2] != ".":
                            getnum = prevline[cnum:cnum+4]
                            nums.extend([bruh for bruh in getnum.split(".") if bruh != ''and bruh.isdigit()])
                        else:
                            nums.append(prevline[cnum])

                if botrow:
                    if botcount == 2:
                            getnum = nextline[cnum-3:cnum+4]
                            nums.extend([bruh for bruh in getnum.split(".") if bruh != ''and bruh.isdigit()])
                    
                    if botcount ==1:
                        if (''.join(bot)).isdigit():
                            nums.append(''.join(bot))
                        elif bot[0] != ".":
                            getnum = nextline[cnum-3:cnum+1]
                            nums.append([bruh for bruh in getnum.split(".") if bruh != ''and bruh.isdigit()][-1]) 
                        elif bot[2] != ".":
                            getnum = nextline[cnum:cnum+4]
                            if getnum == '.430':
                                n = 0
                            nums.extend([bruh for bruh in getnum.split(".") if bruh != '' and bruh.isdigit()])
                        else:
                            nums.append(nextline[cnum])

                if len(nums) != 2:
                    n = 0
                    writetofile = f"{prevline[cnum - 4:cnum + 5]}\n{cur[cnum - 4:cnum + 5]}\n{nextline[cnum - 4:cnum + 5]}\n"
                    writetofile += str(nums) + "\n" + "-" * 15 + "\n"
                    with open("C:\\Users\\ChunChunMaru\\Desktop\\Baby code\\FeetV2\\AoC\\AoC2023\\D3\\Bigbruh.txt", "a") as f:
                        f.write(writetofile)

                final.append(int(nums[1])*int(nums[0]))



    return sum(final)


print(gear_grinder_2(filename))

# 102886441323 failed
# 78179742 too low
