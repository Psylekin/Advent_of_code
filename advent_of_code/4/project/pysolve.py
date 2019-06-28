import datetime
import time
import pandas as pd

def connection_test():
    return 1

def split_sleep_entry(entry):
    return entry.lstrip('[').split('] ')

def convert_to_timestamp(entry):
    return datetime.datetime.strptime(entry, '%Y-%m-%d %H:%M')

chosen_minute = 0
guardID = 0



# Lese alle Daten ein + Bereinige Sie
sleepList = [line.rstrip('\n') for line in open('advent_of_code/4/project/input.txt')]
sleepList = list(map(lambda x: split_sleep_entry(x),sleepList))
# Formatiere die Anfangsdaten als time-Werte
for entry in sleepList:
    entry[0] = convert_to_timestamp(entry[0])
# Sortiere die Daten chronologisch
sleepDf = pd.DataFrame(sleepList, columns=["time", "action"]).sort_values(by=['time']).reset_index(drop = True)
# Errechne wie lange die Guards schlafen
guardSleepingTimes = pd.DataFrame(columns=["ID","SleepingTime"])
#   Wenn Guard steht fange die Berechnung für einen Guard an / oder setze ihn auf die Liste.
for index, entry in enumerate(sleepDf.action): 
    if entry.startswith('Guard'):
        sleeptime = datetime.timedelta()
        newguard = False
        iterator = 1
        guardID = int(entry.lstrip('Guard #').rstrip(' begins shift'))
        while newguard == False:
            if index + iterator + 1 > len(sleepDf) - 2:
                break
            sleeptime += sleepDf.time[index + iterator + 1] - sleepDf.time[index + iterator]
            iterator += 2
            if sleepDf.action[index + iterator].startswith('Guard'):
                newguard = True
                new_sleeping_entry = {"SleepingTime": sleeptime, "ID": guardID}
                guardSleepingTimes = guardSleepingTimes.append(new_sleeping_entry, ignore_index=True)

highscore = [datetime.timedelta(),0]
for guardID in guardSleepingTimes.ID:
    sleepingtime = guardSleepingTimes[guardSleepingTimes.ID == guardID].SleepingTime.sum()
    if sleepingtime > highscore[0]:
        highscore[0] = sleepingtime
        highscore[1] = guardID
print(highscore)

# HIGHSCORE: Wache Nr. 3167

# Finde heraus, in welcher Minute er am Meisten schläft (Minute)

# Errechne die Lösung

print("Lösung: {}".format(chosen_minute * guardID))

