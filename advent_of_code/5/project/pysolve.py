import string
import time

def connection_test():
    return 1

def react_polymer():
    for string in open ("advent_of_code/5/project/input.txt"):
        correctedString = correct_string(string)
        return (len(correctedString))

def correct_string(string):
    stringList = string_to_list(string)
    new_stringlist = edit_whole_stringList(stringList)
    correctString = list_to_string(new_stringlist)
    return correctString

def string_to_list(string):
    stringList = []
    for chars in string:
        stringList.append(chars)
    return stringList

def edit_whole_stringList(stringList):
    sameList = False
    while sameList == False:
        old_stringlist = stringList[:]
        new_stringlist = delete_double_entry(stringList)
        if len(old_stringlist) == len(new_stringlist):
            sameList = True
    return stringList

def delete_double_entry(stringList):
    for index in range(len(stringList) - 1):
        if must_destruct(stringList[index : index + 2]):
            del stringList[index : index + 2]
            break
    return stringList

def must_destruct(string):
    if string[0].capitalize() == string[1].capitalize():
        if string[0].isupper() and string[1].islower():
            return True
        elif string[0].islower() and string[1].isupper():
            return True
        else: 
            return False
    else:
        return False

def list_to_string(list):
    string = ''.join(list)
    return string

# 1 Schmeiß einen Buchstaben aus dem String Beispiel: "A" und "a"
# 2 Lass es voll durchlaufen
# 3 Schau zu, welches Ergebnis das kürzeste ist.

alphabet = list(string.ascii_lowercase)
highscore = {"letter" : "", "length": 0}

for letter in alphabet:
    for string in open ("advent_of_code/5/project/input.txt"):
        startTime = time.time()
        shorter_string = string.replace(letter, "").replace(letter.swapcase(), "")
        solution = correct_string(shorter_string)
        if len(solution) < highscore["length"]:
            highscore["letter"] = letter.upper()
            highscore["length"] = len(solution)
        timeDelta = time.strftime("%H:%M", time.time() - startTime)
        print("Letter: {}    Length: {}     Time: {}".format(letter.upper(), len(solution), timeDelta))