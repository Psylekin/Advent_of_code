def connection_test():
    return 1

def find_input_index():
    global currentMarble
    global currentMarbleList

    index = currentMarbleList.index(currentMarble) + 2
    if index > len(currentMarbleList):
        index -= len(currentMarbleList)

    return index

def make_new_marbleList():
    global currentMarble
    global currentMarbleList

    currentMarbleList.insert(find_input_index(), currentMarble +1)
    currentMarble += 1

    if currentMarble%23 == 0:
        # Find Value of marble 7 counterclockwise (so minus)
        # Save Value to player
        # delete the marble from the list
        # Save Value of currentmarble to player
        pass

    return currentMarbleList

currentMarble = 0
currentMarbleList = [0]
marbles = 23
players = 9
currentPlayer = 0
playerList = [0 for _ in range(players)]

for _ in range(marbles+1):
    currentPlayer += 1
    if currentPlayer > players:
        currentPlayer -= players
    print("{} {}".format(currentPlayer, make_new_marbleList()))
    