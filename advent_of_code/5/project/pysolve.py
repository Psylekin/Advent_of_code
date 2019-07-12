def connection_test():
    return 1

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

string = "AAaBCs"
stringList = []
for chars in string:
    stringList.append(chars)

stringList = oldList

while !(stringList == oldList):
    for index in range(len(stringList)-2):
        oldList = stringList
        if must_destruct(stringList[index:index+2]):
            del stringList[index:index+2]
            break

print(stringList)