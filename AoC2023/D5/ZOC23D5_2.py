"""
def problem_5_2():
    --- Part Two ---
    Everyone will starve if you only plant such a small number of seeds. Re-reading the almanac, it looks like the seeds: line actually describes ranges of seed numbers.

    The values on the initial seeds: line come in pairs. Within each pair, the first value is the start of the range and the second value is the length of the range. So, in the first line of the example above:

    seeds: 79 14 55 13
    This line describes two ranges of seed numbers to be planted in the garden. The first range starts with seed number 79 and contains 14 values: 79, 80, ..., 91, 92. The second range starts with seed number 55 and contains 13 values: 55, 56, ..., 66, 67.

    Now, rather than considering four seed numbers, you need to consider a total of 27 seed numbers.

    In the above example, the lowest location number can be obtained from seed number 82, which corresponds to soil 84, fertilizer 84, water 84, light 77, temperature 45, humidity 46, and location 46. So, the lowest location number is 46.

    Consider all of the initial seed numbers listed in the ranges on the first line of the almanac. What is the lowest location number that corresponds to any of the initial seed numbers?
"""

import os

dirname = os.path.dirname(__file__)

filename = dirname + "\\AOC23D5_input.txt"

test = dirname + "\\AOC23D5_test_1.txt"
test2 = dirname + "\\AOC23D5_test_2.txt"


def process_data(Rawdata):
    maps = tuple([i.split(":")[1] for i in Rawdata])
    changes = [i.split(":")[0] for i in Rawdata][1:]
    changes = [i.replace(" map", "") for i in changes]
    origin_list = maps[0].split(" ")
    seeds = [int(i) for i in origin_list if i != '']

    maps2 = maps[1:]

    maps2 = [conversion.split("\n") for conversion in maps2]
    maps = []

    for conversion in maps2:
        thing = []
        for row in conversion:
            if row == "":
                continue
            else:
                row = row.split(" ")
                row = [int(b) for b in row if b != ""]
                dr, sr, steps = row

                thing.append([dr, (sr, sr+steps-1)])
        maps.append(thing)

    # * seeds into seed ranges
    newseeds = []
    seed1 = seeds[::2]
    seed2 = seeds[1::2]
    for i in range(len(seed1)):
        newseeds += [("cur", seed1[i], seed1[i]+seed2[i]-1)]
        # * for later,tracking original or newly inserted range
    # print(f"""maps: {maps}\n\n\nchanges : {changes}
    #      \n\n\nnewseeds: {newseeds}\n\n""")
    return maps, changes, newseeds


def plant_plant_plant_plant_get_planted_get_planted_2(filename):
    with open(filename) as f:
        r = f.read()
    r.strip()

    # step 1: processing data
    Rawdata = r.split("\n\n")
    maps, changes, seeds = process_data(Rawdata)
    # print("maps:\n" + str(maps), "convertibles:\n" + str(changes),
    #      "original seeds:\n"+str(seeds), sep='\n\n')
    #print("\n\n" + "-"*5 + " ACTUAL CONVERSIONS " + "-"*5 + "\n\n")

    row, conversion = [], []
    # ? to watch list
    # for i in maps:
    #    print(i)

    for cnum in range(len(maps)):
        conversion = maps[cnum]
        change = changes[cnum]
        origin = seeds[:]
        modded = seeds[:]
        final = seeds[:]
        #print(f"CHANGE SEGMENT: {change}")
        #print()
        origin = seeds[:]
        modded = seeds[:]
        for row in conversion:
            #print(f"current seedstate: {modded}\t{change.split("-")[0]}")
            #print()
            #print(f"conversion row:\t   {row} {change}")
            #print()

            destination, source = row
            o_start, o_end = source
            for i in range(len(modded)):
                seedrange = modded[i]
                if seedrange[1:] == (57, 69):
                    n = 0
                if "new" in seedrange:
                    continue

                seedstart, seedend = seedrange[1:]

                # * Seedrange    (old,79, 92)
                # * origin range     (98, 99)
                #! Case 0: dunnid care if seed range not within origin range
                #print(f"Seed - {seedrange[1:]} - {source} conversion")

                #!Case 1: seed range fully within origin range
                if seedstart >= o_start and seedend <= o_end:
                    modded[i] = ("new", seedstart + (destination -
                                                     o_start), seedend + (destination-o_start))
                    #print("seed is fully in range")
                    
                    
                #!Case 2: seed range on left side isnt covered
                elif seedstart < o_start and o_start <= seedend <= o_end:
                    modded[i] = ("new", o_start + (destination -
                                                   o_start), seedend + (destination-o_start))
                    oldpart = ("cur", seedstart, o_start-1)
                    modded.insert(i, oldpart)
                    #print("seed pokes left")
                    
                    
                #!Case 3: seed range on right side isnt covered
                elif o_end > seedstart >= o_start and seedend > o_end:
                    modded[i] = ("new", seedstart + (destination -
                                                     o_start), o_end + (destination-o_start))
                    newpart = ("cur", o_end+1, seedend)
                    modded.insert(i+1, newpart)
                    #print("seed pokes right")
                    
                    
                
                    #print("no conversion")

            #print()
            #print(f"new seedstate:\t   {modded}\t{change.split("-")[2]}")
            #print()
            #print("-"*30)
            #print()
        modded = [("cur", q[1], q[2]) for q in modded]
        seeds = modded[:]
        #print("*"*30)
        #print()
        #print("\tSummary Changes:")
        #print(f"\t{origin} {change.split("-")[0]} (OLD)")
        #print(f"\t{seeds} {change.split("-")[2]} (NEW)")
        #print()
        #print("*"*30)

    # * return lowest location number that corresponds to any of the initial seed numbers?
    return min([i[1] for i in seeds])


print(plant_plant_plant_plant_get_planted_get_planted_2(filename))
