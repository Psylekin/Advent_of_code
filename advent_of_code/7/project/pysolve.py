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

def remove_used_condition(requirements, steps, nextStep):
        deleteList = []
        for index, item in enumerate(requirements):
                if item == nextStep:
                        deleteList.append(index)
        reversedDeleteList = deleteList[::-1]
        for deleteIndex in reversedDeleteList:
                requirements.pop(deleteIndex)
                steps.pop(deleteIndex)
        return requirements, steps

def create_result(requirements, steps):
        result = ""
        while True:
                nextStep = find_nextStep(requirements, steps)
                result += nextStep
                requirements, steps = remove_used_condition(requirements, steps, nextStep)

                if len(steps) == 1:
                        result += requirements[0]
                        result += steps[0]
                        break

        return result

def solve_riddle_1():
        data = loadData("advent_of_code/7/project/input.txt")
        conditions = transform_into_conditions(data)
        requirements = extract_listinfo(conditions, 0)
        steps = extract_listinfo(conditions, 1)
        result = create_result(requirements, steps)
        print(result)

#solve_riddle_1()


# Riddle two is about the same riddle, but!
# When you want to add a letter you have to care if
# A worker is free. Otherwise you have to wait, till
# the workers are done and than give the next step.

# 0 Start (start counting)
# 1 What are the letters to do?
# 2 Give the letters to the people in alphabetical order
# 3 Wait one tick. 
# 4 Is anything ready? No: GO to 3; Yes: Go to 2
# Break, when all letters are done.
# Print(iterations)

"""
data = loadData("advent_of_code/7/project/input.txt")
conditions = transform_into_conditions(data)
requirements = extract_listinfo(conditions, 0)
steps = extract_listinfo(conditions, 1)
capacity = 2

result = ""
tick = 0

nextStep = find_nextStep(requirements, steps)
"""
