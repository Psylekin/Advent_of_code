def connection_test():
    return 1


def find_input_index(transfer):
    global currentMarble
    global currentMarbleList
    global index

    # Hier darf der Index nicht über die Position abgelegen werden.
    # Der Index muss frei wandern.
    index = currentMarbleList.index(currentMarble) + transfer

    if index > len(currentMarbleList):
        index -= len(currentMarbleList)
    elif index < 0:
        index += len(currentMarbleList)
        print(index, len(currentMarbleList), currentMarbleList)

    return index


def make_new_marbleList():
    global currentMarble
    global currentMarbleList

    if (currentMarble + 1) % 23 == 0 and currentMarble != 0:
        index = find_input_index(-7)
        playerList[currentPlayer] += currentMarbleList[index] + currentMarble + 1
        currentMarbleList.pop(index)
        currentMarble = currentMarbleList[index - 1]
    else:
        currentMarbleList.insert(find_input_index(2), currentMarble +1)
        currentMarble += 1

    return currentMarbleList

currentMarble = 0
currentMarbleList = [0]
marbles = 25
players = 9
currentPlayer = 1
playerList = [0 for _ in range(players)]
index = 1

for currentMarble in range(marbles+1):
    currentMarble = currentMarble
    currentPlayer += 1
    if currentPlayer >= players:
        currentPlayer -= players

    elif currentMarble > 23:
        print("{}".format(currentPlayer))
        print("{}\n+++\n".format(make_new_marbleList()))

print()
