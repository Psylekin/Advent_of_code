
def find_unique_characters(word):
    return list(set(word))

inputList = [line.rstrip('\n') for line in open('input.txt')]
endresult = 0

def find_double_and_tribble_chars(inputList):
    counter2 = 0
    counter3 = 0
    # Iteriere durch die Liste
    for entrie in inputList:
        #   Finde einzigartige Buchstaben
        uniqueList = find_unique_characters(entrie)
        #   Mach eine Liste, wie häufig die einzelnen Buchstaben in einem Wort sind.
        charfrequencys = list()
        for uniqueChar in uniqueList:
            charfrequency = entrie.count(uniqueChar)
            charfrequencys.append(charfrequency)
        #   Wenn du einen 2 findest --> Adde es zum Counter
        if 2 in charfrequencys:
            counter2 += 1
        #   Wenn du einee 3 findest --> Add es zum Counter
        if 3 in charfrequencys:
            counter3 += 1
    return (counter2, counter3)


# Multipliziere counter 2 und 3
counter2, counter3 = find_double_and_tribble_chars(inputList)
endresult = counter2*counter3

print("Ergebnis: {}\n1: {}\n2: {}"
    .format(endresult, counter2, counter3))