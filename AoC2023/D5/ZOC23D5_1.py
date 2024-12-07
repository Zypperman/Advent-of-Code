"""
def problem_5_1():
    --- Day 5: If You Give A Seed A Fertilizer ---
    You take the boat and find the gardener right where you were told he would be: managing a giant "garden" that looks more to you like a farm.

    "A water source? Island Island is the water source!" You point out that Snow Island isn't receiving any water.

    "Oh, we had to stop the water because we ran out of sand to filter it with! Can't make snow with dirty water. Don't worry, I'm sure we'll get more sand soon; we only turned off the water a few days... weeks... oh no." His face sinks into a look of horrified realization.

    "I've been so busy making sure everyone here has food that I completely forgot to check why we stopped getting more sand! There's a ferry leaving soon that is headed over in that direction - it's much faster than your boat. Could you please go check it out?"

    You barely have time to agree to this request when he brings up another. "While you wait for the ferry, maybe you can help us with our food production problem. The latest Island Island Almanac just arrived and we're having trouble making sense of it."

    The almanac (your puzzle input) lists all of the seeds that need to be planted. It also lists what type of soil to use with each kind of seed, what type of fertilizer to use with each kind of soil, what type of water to use with each kind of fertilizer, and so on. Every type of seed, soil, fertilizer and so on is identified with a number, but numbers are reused by each category - that is, soil 123 and fertilizer 123 aren't necessarily related to each other.

    For example:

    seeds: 79 14 55 13

    seed-to-soil map:
    50 98 2
    52 50 48

    soil-to-fertilizer map:
    0 15 37
    37 52 2
    39 0 15

    fertilizer-to-water map:
    49 53 8
    0 11 42
    42 0 7
    57 7 4

    water-to-light map:
    88 18 7
    18 25 70

    light-to-temperature map:
    45 77 23
    81 45 19
    68 64 13

    temperature-to-humidity map:
    0 69 1
    1 0 69

    humidity-to-location map:
    60 56 37
    56 93 4
    The almanac starts by listing which seeds need to be planted: seeds 79, 14, 55, and 13.

    The rest of the almanac contains a list of maps which describe how to convert numbers from a source category into numbers in a destination category. That is, the section that starts with seed-to-soil map: describes how to convert a seed number (the source) to a soil number (the destination). This lets the gardener and his team know which soil to use with which seeds, which water to use with which fertilizer, and so on.

    Rather than list every source number and its corresponding destination number one by one, the maps describe entire ranges of numbers that can be converted. Each line within a map contains three numbers: the destination range start, the source range start, and the range length.

    Consider again the example seed-to-soil map:

    50 98 2
    52 50 48
    The first line has a destination range start of 50, a source range start of 98, and a range length of 2. This line means that the source range starts at 98 and contains two values: 98 and 99. The destination range is the same length, but it starts at 50, so its two values are 50 and 51. With this information, you know that seed number 98 corresponds to soil number 50 and that seed number 99 corresponds to soil number 51.

    The second line means that the source range starts at 50 and contains 48 values: 50, 51, ..., 96, 97. This corresponds to a destination range starting at 52 and also containing 48 values: 52, 53, ..., 98, 99. So, seed number 53 corresponds to soil number 55.

    Any source numbers that aren't mapped correspond to the same destination number. So, seed number 10 corresponds to soil number 10.

    So, the entire list of seed numbers and their corresponding soil numbers looks like this:

    seed  soil
    0     0
    1     1
    ...   ...
    48    48
    49    49
    50    52
    51    53
    ...   ...
    96    98
    97    99
    98    50
    99    51
    With this map, you can look up the soil number required for each initial seed number:

    Seed number 79 corresponds to soil number 81.
    Seed number 14 corresponds to soil number 14.
    Seed number 55 corresponds to soil number 57.
    Seed number 13 corresponds to soil number 13.
    The gardener and his team want to get started as soon as possible, so they'd like to know the closest location that needs a seed. Using these maps, find the lowest location number that corresponds to any of the initial seeds. To do this, you'll need to convert each seed number through other categories until you can find its corresponding location number. In this example, the corresponding types are:

    Seed 79, soil 81, fertilizer 81, water 81, light 74, temperature 78, humidity 78, location 82.
    Seed 14, soil 14, fertilizer 53, water 49, light 42, temperature 42, humidity 43, location 43.
    Seed 55, soil 57, fertilizer 57, water 53, light 46, temperature 82, humidity 82, location 86.
    Seed 13, soil 13, fertilizer 52, water 41, light 34, temperature 34, humidity 35, location 35.
    So, the lowest location number in this example is 35.

    What is the lowest location number that corresponds to any of the initial seed numbers?

    To begin, get your puzzle input.
"""
filename = "C:\\Users\\ChunChunMaru\\Desktop\\Baby code\\FeetV2\\AoC\\AoC2023\\D5\\AOC23D5_input.txt"

test = "C:\\Users\\ChunChunMaru\\Desktop\\Baby code\\FeetV2\\AoC\\AoC2023\\D5\\AOC23D5_test_1.txt"
test2 = "C:\\Users\\ChunChunMaru\\Desktop\\Baby code\\FeetV2\\AoC\\AoC2023\\D5\\AOC23D5_test_2.txt"


def plant_plant_plant_plant_get_planted_get_planted(filename):
    with open(filename) as f:
        r = f.read()
    r.strip()

    Rawdata = r.split("\n\n")

    #Rawdata = filename.split("\n\n")

    # * data looks like:
    # * seeds
    # * seed-to-soil map:
    # , dest. range start, source range start, range length
    # , for 50 98 2:
    # - source range is 98,99 ==> destination range is also the same length, but 50,51
    # - that means 98 -> 50, 99 -> 51
    # - [source val, dest val] => [98,50], [99,51]
    # * soil-to-fertilizer map:
    # * fertilizer-to-water map:
    # * water-to-light map:
    # * light-to-temperature map:
    # * temperature-to-humidity map:
    # * humidity-to-location map:

    # step 1: processing data
    maps = tuple([i.split(":")[1] for i in Rawdata])
    changes = [i.split(":")[0] for i in Rawdata][1:]
    changes = [i.replace(" map", "") for i in changes]
    origin_list = maps[0].split(" ")
    seeds = [int(i) for i in origin_list if i != '']
    print(f"original: {seeds}")
    print()
    print("-"*30)
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

    row, conversion = [], []
    # ? to watch list
    # for i in maps:
    #    print(i)

    for cnum in range(len(maps)):
        conversion = maps[cnum]
        change = changes[cnum]
        origin_list = seeds[:]
        modded = seeds[:]
        final_list = seeds[:]
        for row in conversion:
            print(f"current seedstate:\t{seeds[3]}\t{change.split("-")[0]}")
            if change.split("-")[0] == "fertilizer":
                n = 0
            print()
            print(f"conversion row:\t\t{row}\t{change}")
            print()

            destination, source = row
            o_start, o_end = source
            for i in range(len(seeds)):
                origval = seeds[i]
                if origval >= o_start and origval <= o_end:
                    modded[i] += (destination-o_start)

            for i in range(len(seeds)):
                if origin_list[i] != modded[i]:
                    thing = modded.copy()
                    final_list[i] = thing[i]
            modded = seeds[:]
            print(f"new seedstate:\t\t{seeds[3]}\t{change.split("-")[2]}")
            print()
            print("-"*30)
            print()
        seeds = final_list[:]

    # * return lowest location number that corresponds to any of the initial seed numbers?
    return min(seeds)


#filename = 
'''seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4'''


print(plant_plant_plant_plant_get_planted_get_planted(filename))

# 102886441323 failed
# 530923 failed
# correct is 533775
