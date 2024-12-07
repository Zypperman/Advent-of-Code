"""
def problem_6_1():
    --- Part Two ---
    As the race is about to start, you realize the piece of paper with race times and record distances you got earlier actually just has very bad kerning. There's really only one race - ignore the spaces between the numbers on each line.

    So, the example from before:

    Time:      7  15   30
    Distance:  9  40  200
    ...now instead means this:

    Time:      71530
    Distance:  940200
    Now, you have to figure out how many ways there are to win this single race. In this example, the race lasts for 71530 milliseconds and the record distance you need to beat is 940200 millimeters. You could hold the button anywhere from 14 to 71516 milliseconds and beat the record, a total of 71503 ways!

    How many ways can you beat the record in this one much longer race?
"""

filename = "C:\\Users\\ChunChunMaru\\Desktop\\Baby code\\FeetV2\\AoC\\AoC2023\\D6\\AOC23D6_input2.txt"

test = "C:\\Users\\ChunChunMaru\\Desktop\\Baby code\\FeetV2\\AoC\\AoC2023\\D6\\AOC23D6_test_1.txt"
test2 = "C:\\Users\\ChunChunMaru\\Desktop\\Baby code\\FeetV2\\AoC\\AoC2023\\D6\\AOC23D6_test_2.txt"


def process_data(RD):
    timeset = RD[0].split(":")[1]
    timeset = [i for i in timeset.split(" ") if i != ""]
    spaceset = RD[1].split(":")[1]
    spaceset = [i for i in spaceset.split(" ") if i != ""]

    return [(int(timeset[i]), int(spaceset[i])) for i in range(len(timeset))]


def wishin_i_was_fishin2(filename):
    with open(filename) as f:
        r = f.read()
    r.strip()

    Rawdata = r.split("\n")
    # step 1: processing data
    Raceset = process_data(Rawdata)

    # ? turns race data into [(max_time, rec_dist),...]
    # ? basically, have a boat beat rec_dist within max_time.
    # ? max_time = charge_time + travel_time
    # ? charge_time is how long u spend charging your thing, every second more is +1m/
    # ? dist moved by boat afterwards is ust travel_time * charged_speed
    # ? you just need to find all the number of charge_times that you are able to beat the record time.
    #! keep that num as the number of ways you can win, then mutltiply it all together.
    
    final = []
    for race in Raceset:
        time, dist_to_beat = race
        counter = 0
        mintime = dist_to_beat//time
        for possible_time in range(mintime+1, time):
            cur_distance = possible_time * (time - possible_time)
            if cur_distance <= dist_to_beat:
                counter += 1
            else:
                break

    # * return lowest location number that corresponds to any of the initial seed numbers?
    return time - ((counter + mintime) * 2)-1


print(wishin_i_was_fishin2(filename))
