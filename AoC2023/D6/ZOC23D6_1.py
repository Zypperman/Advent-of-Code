"""
def problem_6_1():
    --- Day 6: Wait For It ---
    The ferry quickly brings you across Island Island. After asking around, you discover that there is indeed normally a large pile of sand somewhere near here, but you don't see anything besides lots of water and the small island where the ferry has docked.

    As you try to figure out what to do next, you notice a poster on a wall near the ferry dock. "Boat races! Open to the public! Grand prize is an all-expenses-paid trip to Desert Island!" That must be where the sand comes from! Best of all, the boat races are starting in just a few minutes.

    You manage to sign up as a competitor in the boat races just in time. The organizer explains that it's not really a traditional race - instead, you will get a fixed amount of time during which your boat has to travel as far as it can, and you win if your boat goes the farthest.

    As part of signing up, you get a sheet of paper (your puzzle input) that lists the time allowed for each race and also the best distance ever recorded in that race. To guarantee you win the grand prize, you need to make sure you go farther in each race than the current record holder.

    The organizer brings you over to the area where the boat races are held. The boats are much smaller than you expected - they're actually toy boats, each with a big button on top. Holding down the button charges the boat, and releasing the button allows the boat to move. Boats move faster if their button was held longer, but time spent holding the button counts against the total race time. You can only hold the button at the start of the race, and boats don't move until the button is released.

    For example:

    Time:      7  15   30
    Distance:  9  40  200
    This document describes three races:

    The first race lasts 7 milliseconds. The record distance in this race is 9 millimeters.
    The second race lasts 15 milliseconds. The record distance in this race is 40 millimeters.
    The third race lasts 30 milliseconds. The record distance in this race is 200 millimeters.
    Your toy boat has a starting speed of zero millimeters per millisecond. For each whole millisecond you spend at the beginning of the race holding down the button, the boat's speed increases by one millimeter per millisecond.

    So, because the first race lasts 7 milliseconds, you only have a few options:

    Don't hold the button at all (that is, hold it for 0 milliseconds) at the start of the race. The boat won't move; it will have traveled 0 millimeters by the end of the race.
    Hold the button for 1 millisecond at the start of the race. Then, the boat will travel at a speed of 1 millimeter per millisecond for 6 milliseconds, reaching a total distance traveled of 6 millimeters.
    Hold the button for 2 milliseconds, giving the boat a speed of 2 millimeters per millisecond. It will then get 5 milliseconds to move, reaching a total distance of 10 millimeters.
    Hold the button for 3 milliseconds. After its remaining 4 milliseconds of travel time, the boat will have gone 12 millimeters.
    Hold the button for 4 milliseconds. After its remaining 3 milliseconds of travel time, the boat will have gone 12 millimeters.
    Hold the button for 5 milliseconds, causing the boat to travel a total of 10 millimeters.
    Hold the button for 6 milliseconds, causing the boat to travel a total of 6 millimeters.
    Hold the button for 7 milliseconds. That's the entire duration of the race. You never let go of the button. The boat can't move until you let go of the button. Please make sure you let go of the button so the boat gets to move. 0 millimeters.
    Since the current record for this race is 9 millimeters, there are actually 4 different ways you could win: you could hold the button for 2, 3, 4, or 5 milliseconds at the start of the race.

    In the second race, you could hold the button for at least 4 milliseconds and at most 11 milliseconds and beat the record, a total of 8 different ways to win.

    In the third race, you could hold the button for at least 11 milliseconds and no more than 19 milliseconds and still beat the record, a total of 9 ways you could win.

    To see how much margin of error you have, determine the number of ways you can beat the record in each race; in this example, if you multiply these values together, you get 288 (4 * 8 * 9).

    Determine the number of ways you could beat the record in each race. What do you get if you multiply these numbers together?
"""

filename = "C:\\Users\\ChunChunMaru\\Desktop\\Baby code\\FeetV2\\AoC\\AoC2023\\D6\\AOC23D6_input.txt"

test = "C:\\Users\\ChunChunMaru\\Desktop\\Baby code\\FeetV2\\AoC\\AoC2023\\D6\\AOC23D6_test_1.txt"
test2 = "C:\\Users\\ChunChunMaru\\Desktop\\Baby code\\FeetV2\\AoC\\AoC2023\\D6\\AOC23D6_test_2.txt"


def process_data(RD):
    timeset = RD[0].split(":")[1]
    timeset = [i for i in timeset.split(" ") if i != ""]
    spaceset = RD[1].split(":")[1]
    spaceset = [i for i in spaceset.split(" ") if i != ""]

    return [(int(timeset[i]),int(spaceset[i])) for i in range(len(timeset))]

def wishin_i_was_fishin(filename):
    with open(filename) as f:
        r = f.read()
    r.strip()

    Rawdata = r.split("\n")
    # step 1: processing data
    Raceset = process_data(Rawdata)
    
    #? turns race data into [(max_time, rec_dist),...]
    #? basically, have a boat beat rec_dist within max_time.
    #? max_time = charge_time + travel_time
    #? charge_time is how long u spend charging your thing, every second more is +1m/
    #? dist moved by boat afterwards is ust travel_time * charged_speed
    #? you just need to find all the number of charge_times that you are able to beat the record time. 
    #! keep that num as the number of ways you can win, then mutltiply it all together.
    final = []
    for race in Raceset:
        time,dist_to_beat = race
        counter = 0
        mintime = dist_to_beat//time
        for possible_time in range(mintime+1,time):
            cur_distance = possible_time * (time - possible_time)
            if possible_time == 4:
                n= 0
            if cur_distance > dist_to_beat:
                counter += 1
        final.append(counter)
    
    
    thing = 1
    for i in final:
        thing *= i
        
    # * return lowest location number that corresponds to any of the initial seed numbers?
    return thing

print(wishin_i_was_fishin(filename))
