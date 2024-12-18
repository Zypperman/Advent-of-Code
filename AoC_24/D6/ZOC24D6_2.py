'''
def problem_6_2():
    Paste_qn_statement
'''

import os

dirname = os.path.dirname(__file__) + "\\"

test = dirname + "AOC24D6_input.txt"
test1 = dirname + "AOC24D6_test1.txt"
test2 = dirname + "AOC24D6_test2.txt"

def process_data(RD):
    # * dump data for processing here
    relevant_data = 0
    return RD #relevant_data

def problem6_2(filename):
    with open(filename) as f:
        r = f.read()
    r.strip()

    Rawdata = r.split("\n")

    # * processing data
    #! swap out with actual var names
    data = process_data(Rawdata)
    #* to test if code works, comment out when running input
    print(f"data looks like:\n{data}")
    #? Dump solution here

    thing = 0

    return thing

print(problem6_2(test))
