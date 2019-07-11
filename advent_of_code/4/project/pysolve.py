import datetime
import time
import pandas as pd

def connection_test():
    return 1

def split_sleep_entry(entry):
    return entry.lstrip('[').split('] ')

def convert_to_timestamp(entry):
    return datetime.datetime.strptime(entry, '%Y-%m-%d %H:%M')

def create_durationDf(index, guard):
    start_ind = index
    end_ind = index + 1

    start = sleepDf.loc[start_ind,"time"]
    end = sleepDf.loc[end_ind,"time"]
    delta = calculate_timeDelta(end_ind, start_ind)
    
    durationDf = pd.DataFrame([guard,start, end, delta], index = ["guard", "start", "end", "delta"])
    return durationDf

def calculate_timeDelta(timestamp_later_index, timestamp_earlier_index):
    return sleepDf.loc[timestamp_later_index,"time"] - sleepDf.loc[timestamp_earlier_index,"time"]

def strip_guard_text(string):
    return string.lstrip("Guard #").rstrip(" begins shift")

def extract_minutes(dateTime):
    return dateTime.minute


chosen_minute = 0
guardID = 0
sameGuard = True
guardSleepingTimes = pd.DataFrame(columns=["guard", "start", "end", "delta"])

sleepList = [line.rstrip('\n') for line in open('advent_of_code/4/project/input.txt')]
sleepList = list(map(lambda x: split_sleep_entry(x),sleepList))

for entry in sleepList:
    entry[0] = convert_to_timestamp(entry[0])

sleepDf = pd.DataFrame(sleepList, columns=["time", "action"]).sort_values(by=['time']).reset_index(drop = True)

for index, entry in enumerate(sleepDf.loc[:,"action"]):
    if entry.startswith("Guard"):
        guard = strip_guard_text(entry)
    elif entry.startswith("falls asleep"):
        durationDf = create_durationDf(index, guard).T
        guardSleepingTimes = guardSleepingTimes.append(durationDf, ignore_index = True)

highSleep = (0, datetime.timedelta())
for guard in guardSleepingTimes.guard.unique():
    sleepTime = guardSleepingTimes.loc[guardSleepingTimes.guard == guard, "delta"].sum()
    if  sleepTime > highSleep[1]:
        highSleep = (guard, sleepTime)
guard = int(highSleep[0])

bestguardSleep = guardSleepingTimes.loc[guardSleepingTimes.guard == "3041",["start", "end"]].reset_index().drop("index", axis = 1)
for column in bestguardSleep.columns:
    for index in range(len(bestguardSleep)):
        bestguardSleep.loc[index, column] = bestguardSleep.loc[index, column].minute

bestfrequency = (0,0)
for minute in range(0,60):
    frequency = 0
    for entrie in range(len(bestguardSleep)):
        if minute >= bestguardSleep.iloc[entrie,0] and minute < bestguardSleep.iloc[entrie,1]:
            frequency += 1
    if frequency > bestfrequency[1]:
        bestfrequency = (minute,frequency)
mostFrequentMinute = bestfrequency[0]

print("Lösung: {}".format(mostFrequentMinute * guard))

