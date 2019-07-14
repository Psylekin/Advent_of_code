def connection_test():
    return 1

def loadData(location):
    with open(location) as input:
        return input.read()

data = loadData("advent_of_code/8/project/input.txt")
nodeList = []

# Nimm die erste Nummer. Sie ist die Zahl an Subnodes für Objekt 1.
# Nimm die zweite Zahl, Sie ist die Anzahl an MetaData entries für Objekt 1.
# Wenn die Anzahl an Subnodes != 0 ist: Die nächste Zahl ist die Anzahl an Subnodes für Objekt 2.
# Wenn die Anzahl an Subnodes == 0 ist und die Anzahl an Metadata != 0 ist Sind das Metadata für Objekt 2.
# Wenn die Anzahl an Subnodes == 0 ist und die Anzahl an Metadata == 0 ist. Ist das die Anzahl an Subnodes für Objekt 3.


print(data)