import numpy as np 

def connection_test():
    return 1

def loadData(location):
    with open(location) as input:
        return input.read().splitlines()

def transform_into_conditions(data):
    conditions = []
    for line in data:
        condition = [line[5], line[-12]]
        conditions.append(condition)
    return conditions

def extract_listinfo(conditions, index):
    listinfo = []
    for condition in conditions:
        listinfo.append(condition[index])
    return listinfo

def find_nextStep(requirements, steps):
    nextStep = []
    for item in unique(requirements):
        if item not in unique(steps):
            nextStep.append(item)
    nextStep = sorted(nextStep)
    return nextStep[0]

def unique(listing):
    return np.unique(np.array(listing))

def delete_listitem(listing, nextStep):
    index = np.argwhere(listing ==  nextStep)
    listing = np.delete(listing, index)
    return listing

data = loadData("advent_of_code/7/project/input.txt")

conditions = transform_into_conditions(data)
requirements = extract_listinfo(conditions, 0)
steps = extract_listinfo(conditions, 1)

result = ""
nextStep = find_nextStep(requirements, steps)
result = result.join(nextStep)


for index, item in enumerate(requirements):
    data = zip(requirements,steps)
    if item == nextStep:
        print(index)
print(set(data))