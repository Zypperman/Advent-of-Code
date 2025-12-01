"""
def problem_6_1():
    --- Day 6: Guard Gallivant ---
    The Historians use their fancy device again, this time to whisk you all away to the North Pole prototype suit manufacturing lab... in the year 1518! It turns out that having direct access to history is very convenient for a group of historians.

    You still have to be careful of time paradoxes, and so it will be important to avoid anyone from 1518 while The Historians search for the Chief. Unfortunately, a single guard is patrolling this part of the lab.

    Maybe you can work out where the guard will go ahead of time so that The Historians can search safely?

    You start by making a map (your puzzle input) of the situation. For example:

    ....#.....
    .........#
    ..........
    ..#.......
    .......#..
    ..........
    .#..^.....
    ........#.
    #.........
    ......#...
    The map shows the current position of the guard with ^ (to indicate the guard is currently facing up from the perspective of the map). Any obstructions - crates, desks, alchemical reactors, etc. - are shown as #.

    Lab guards in 1518 follow a very strict patrol protocol which involves repeatedly following these steps:

    If there is something directly in front of you, turn right 90 degrees.
    Otherwise, take a step forward.
    Following the above protocol, the guard moves up several times until she reaches an obstacle (in this case, a pile of failed suit prototypes):

    ....#.....
    ....^....#
    ..........
    ..#.......
    .......#..
    ..........
    .#........
    ........#.
    #.........
    ......#...
    Because there is now an obstacle in front of the guard, she turns right before continuing straight in her new facing direction:

    ....#.....
    ........>#
    ..........
    ..#.......
    .......#..
    ..........
    .#........
    ........#.
    #.........
    ......#...
    Reaching another obstacle (a spool of several very long polymers), she turns right again and continues downward:

    ....#.....
    .........#
    ..........
    ..#.......
    .......#..
    ..........
    .#......v.
    ........#.
    #.........
    ......#...
    This process continues for a while, but the guard eventually leaves the mapped area (after walking past a tank of universal solvent):

    ....#.....
    .........#
    ..........
    ..#.......
    .......#..
    ..........
    .#........
    ........#.
    #.........
    ......#v..
    By predicting the guard's route, you can determine which specific positions in the lab will be in the patrol path. Including the guard's starting position, the positions visited by the guard before leaving the area are marked with an X:

    ....#.....
    ....XXXXX#
    ....X...X.
    ..#.X...X.
    ..XXXXX#X.
    ..X.X.X.X.
    .#XXXXXXX.
    .XXXXXXX#.
    #XXXXXXX..
    ......#X..
    In this example, the guard will visit 41 distinct positions on your map.

    Predict the path of the guard. How many distinct positions will the guard visit before leaving the mapped area?
"""

import os

dirname = os.path.dirname(__file__) + "\\"

test = dirname + "AOC24D6_input.txt"
test1 = dirname + "AOC24D6_test1.txt"
test2 = dirname + "AOC24D6_test2.txt"


def process_data(RD):
    # * dump data for processing here
    return RD  # relevant_data


# * functions work the same way:
#  step 1: get the row to scan
#  step 2: split the row by direction, use x for horizontal, use y for vertical
#  step 2b: split the row by direction:

# * left  -> row[: x - 1]
# * Right -> row[x:]
# * Up    -> row[:y-1]
# * Down  -> row[y:]

#  step 3: get number of cells moved and check if obstacle present
#  step 4: move guard to new position


def seek(data, coords, direction):
    x, y = coords
    rotate = False
    has_obstacle = False
    
    if direction in ("up", "down"):
        doo = y - 1 if direction == "up" else y + 1
        new_pos = (x, doo)

    if direction in ("left", "right"):
        doo = x - 1 if direction == "left" else x + 1
        new_pos = (doo, y)
    
    spot = data[new_pos[1]][new_pos[0]]
    
    if spot == "#":
        rotate = True
        new_pos = coords
    else:
        rotate = False

    return new_pos, rotate



def problem6_1(filename):
    # turn right if you hit something, repeat until you leave the area

    with open(filename) as f:
        r = f.read()
    r.strip()

    Rawdata = r.split("\n")

    # * processing data
    #! swap out with actual var names
    data = process_data(Rawdata)
    # * to test if code works, comment out when running input
    # print(f"data looks like:")
    for i in data:
        print(i)
    # ? Dump solution here

    # find starting location
    found = False
    start_x = 0
    start_y = 0
    char = ""

    for row in data:
        start_x = 0
        for cell in row:
            if cell not in ("#", "."):
                found = True
                char = cell
                data[start_y] = data[start_y].replace(cell, ".")
                break
            else:
                start_x += 1
        if found:
            break
        start_y += 1

    charlist = {"^": "up", ">": "right", "v": "down", "<": "left"}
    pos = (start_x, start_y)
    directions = list(charlist.values())
    dir_enum = directions.index(charlist[char])
    direction = charlist[char]

    print("starting position")
    print(pos)
    print()
    has_obstacle = True

    all_cells = [pos]
    cells = []
    
    maze_size = (len(data[0]-1),len(data))
    
    while has_obstacle:
        print("=" * 15)
        direction = directions[dir_enum]
        print("next direction")
        print(direction)
        
        new_pos, rotate = seek(data, pos, direction)
        
        if new_pos[0] not in range(maze_size[0]) or new_pos[1] not in range(maze_size[1]):
            
        
        if new_pos not in all_cells:
            all_cells.append(new_pos)
        
        
        
        if rotate:
            dir_enum += 1
            dir_enum = dir_enum % len(directions)

    all_cells = set(all_cells)
    return len(all_cells)


print(problem6_1(test))
# 329 too low
