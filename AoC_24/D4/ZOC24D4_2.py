'''
def problem_4_1():
    Paste_qn_statement
'''

import os

dirname = os.path.dirname(__file__) + "\\"

test = dirname + "AOC24D4_input.txt"
test1 = dirname + "AOC24D4_test_1.txt"
test2 = dirname + "AOC24D4_test2.txt"

def process_data(RD):
    # * dump data for processing here

    relevant_data = 0

    return RD #relevant_data

def problem4_2(filename):
    with open(filename) as f:
        r = f.read()
    r.strip()

    Rawdata = r.split("\n")

    # * processing data
    #! swap out with actual var names
    var_name = process_data(Rawdata)
    #* to test if code works, comment out when running input
    print(f"data looks like:\n{var_name}")
    #? Dump solution here

    thing = 0

    return thing

print(problem4_2(test))
