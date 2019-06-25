
adders = list()
frequence = 0
endvalue = 0
frequencyFound = False
frequencyList = []
iterationcounter = 0

for line in open('numbers.txt'):
    adders.append(int(line.strip()))

while frequencyFound == False:    
    for adder in adders:
        frequence = frequence + adder
        if frequence in frequencyList:
            print(frequence)
            frequencyFound = True
            break
        else:
            frequencyList.append(frequence)

        
    iterationcounter = iterationcounter + 1
    print("Iteration: {}".format(iterationcounter))
    if iterationcounter == 200:
        break


