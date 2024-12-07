import os
import datetime


#! Code assumes that its in the folder where you wanna work in.

# **Get Year and Date, leave blank if creating for current day
Year = input("Enter Year (if current year, then leave blank)")
Day = input("Enter Day  (if current Day,  then leave blank)")

Today = datetime.date.today()
Year = str(Today).split("-")[0] if Year == "" else Year
Day = int(str(Today).split("-")[2]) if Day == "" else Day

dirname = os.path.dirname(__file__)
rootfoldername = dirname + "\\AoC" + Year[2:]
print(rootfoldername)

