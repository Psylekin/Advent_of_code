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


chosen_minute = 0
guardID = 0
sameGuard = True
guardSleepingTimes = pd.DataFrame(columns=["guard", "start", "end", "delta"])

# Lese alle Daten ein + Bereinige Sie
sleepList = [line.rstrip('\n') for line in open('advent_of_code/4/project/input.txt')]
sleepList = list(map(lambda x: split_sleep_entry(x),sleepList))
# Formatiere die Anfangsdaten als time-Werte
for entry in sleepList:
    entry[0] = convert_to_timestamp(entry[0])
# Sortiere die Daten chronologisch
sleepDf = pd.DataFrame(sleepList, columns=["time", "action"]).sort_values(by=['time']).reset_index(drop = True)

print("{}\n".format(sleepDf.head(10)))

for index, entry in enumerate(sleepDf.loc[:,"action"]):
    if entry.startswith("Guard"):
        guard = strip_guard_text(entry)
    elif entry.startswith("falls asleep"):
        durationDf = create_durationDf(index, guard)
        guardSleepingTimes = guardSleepingTimes.append(durationDf.T, ignore_index = True)

print(guardSleepingTimes)

for guard in guardSleepingTimes.guard.unique():
    print("Guard: {}, Time: {}".format(guard, guardSleepingTimes.loc[guardSleepingTimes.guard == guard, "delta"].sum()))

# Errechne wie lange die Guards schlafen

#   Wenn Guard steht fange die Berechnung für einen Guard an / oder setze ihn auf die Liste.

# HIGHSCORE: Wache Nr. 3041

# Finde heraus, in welcher Minute er am Meisten schläft (Minute)

# Errechne die Lösung

#print("Lösung: {}".format(chosen_minute * guardID))

