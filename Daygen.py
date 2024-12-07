import os
import datetime


#! Code assumes that its in the folder where you wanna work in.

# **Get Year and Date, leave blank if creating for current day
Year = input("Enter Year (if current year, then leave blank)")
Day = input("Enter Day  (if current Day,  then leave blank)")

Today = datetime.date.today()
Year = str(Today).split("-")[0] if Year == "" else Year or Type(Year) != int
Day = int(str(Today).split("-")[2]) if Day == "" else Day or int(Day) != int


dirname = os.path.dirname(__file__)

rootfoldername = dirname + "\\AoC_" + Year[2:]

foldername = rootfoldername + f"\\D{Day}"

if not os.path.exists(rootfoldername):
    os.makedirs(rootfoldername)

# print(f"The directory's name is {dirname}")

if os.path.exists(foldername):
    print("Directory already exists, please make sure day has been completed.")
    exit()
else:
    os.makedirs(foldername)



scriptnames = [
    "AOC",
    "_input.txt",
    "_test_1.txt",
    "_test2.txt",
]

# * 1 - create input dump file
filename = foldername + f"\\AOC{Year[2:]}D{Day}_input.txt"
with open(filename, "w") as f:
    f.write("Replace_with_input")

# * 2 - create testcase1 dump file
filename = foldername + f"\\AOC{Year[2:]}D{Day}_test_1.txt"
with open(filename, "w") as f:
    f.write("Replace_with_testinput1")

# * 3 - create testcase2 dump file
filename = foldername + f"\\AOC{Year[2:]}D{Day}_test2.txt"
with open(filename, "w") as f:
    f.write("Replace_with_testinput2")


lazyconvert = f"""\'\'\'
def problem_{Day}_1():
    Paste_qn_statement
\'\'\'

import os

dirname = os.path.dirname(__file__) + "\\\\"

filename = dirname + "AOC{Year[2:]}D{Day}{scriptnames[1]}"
test = dirname + "AOC{Year[2:]}D{Day}{scriptnames[2]}"
test2 = dirname + "AOC{Year[2:]}D{Day}{scriptnames[3]}"

def process_data(RD):
    # * dump data for processing here

    relevant_data = 0

    return RD #relevant_data

def problem{Day}_1(filename):
    with open(filename) as f:
        r = f.read()
    r.strip()

    Rawdata = r.split("\\n")

    # * processing data
    #! swap out with actual var names
    var_name = process_data(Rawdata)
    #* to test if code works, comment out when running input
    print(f"data looks like:\\n{{var_name}}")
    #? Dump solution here

    thing = 0

    return thing

print(problem{Day}_1(filename))
"""

# * 4 - create problem 1 script file
filename = foldername + f"\\ZOC{Year[2:]}D{Day}_1.py"
with open(filename, "w") as f:
    f.write(lazyconvert)

lazyconvert = f"""\'\'\'
def problem_{Day}_1():
    Paste_qn_statement
\'\'\'

import os

dirname = os.path.dirname(__file__) + "\\\\"

filename = dirname + "AOC{Year[2:]}D{Day}{scriptnames[1]}"
test = dirname + "AOC{Year[2:]}D{Day}{scriptnames[2]}"
test2 = dirname + "AOC{Year[2:]}D{Day}{scriptnames[3]}"

def process_data(RD):
    # * dump data for processing here

    relevant_data = 0

    return RD #relevant_data

def problem{Day}_2(filename):
    with open(filename) as f:
        r = f.read()
    r.strip()

    Rawdata = r.split("\\n")

    # * processing data
    #! swap out with actual var names
    var_name = process_data(Rawdata)
    #* to test if code works, comment out when running input
    print(f"data looks like:\\n{{var_name}}")
    #? Dump solution here

    thing = 0

    return thing

print(problem{Day}_2(filename))
"""

# * 4 - create problem 1 script file
filename = foldername + f"\\ZOC{Year[2:]}D{Day}_2.py"
with open(filename, "w") as f:
    f.write(lazyconvert)
