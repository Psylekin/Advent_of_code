def count_differences(string1,string2):
    differences = 0
    for index, char in enumerate(string1):
        if char != string2[index]:
            differences += 1
    return differences

inputList = [line.rstrip('\n') for line in open('../project/input.txt')]

#Iteriere durch die Liste
for index, base in enumerate(inputList):
    #print("{}: {}".format(index,base))
    # Vergleiche jeden Eintrag mit allen anderen Einträgen (starte ab dem nächsten Eintrag
    for compare in inputList[index+1:]:
        # Prüfe Stück für Stück
        if count_differences(compare, base) == 1:
            print("Gefunden: {} und {}".format(compare, base))


