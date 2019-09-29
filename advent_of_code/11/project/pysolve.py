import pandas as pd

def connection_test():
    return 1

def find_final_result():
    return "0,0"

def calculate_power_level(x :int,y :int,grid_serial):
    rackID = x + 10
    powerLevel = str((rackID * y + grid_serial) * rackID)
    calcPowerLevel = int(powerLevel[-3]) - 5
    return calcPowerLevel

def create_powerGrid(grid_serial):
    nrList = [x for x in range (1,301)]
    powerGrid = pd.DataFrame(columns = nrList, index = nrList, data = 0)
    for x in powerGrid:
        print(x)
        for y in powerGrid:
            powerGrid.loc[x,y] = calculate_power_level(x,y,grid_serial)
    
    return powerGrid

def calculate_gridPower(powerGrid):
    gridPower = powerGrid.sum().sum()

    return gridPower

serial_number = 42
#powerGrid = create_powerGrid(serial_number)
#powerGrid.to_excel("result_{}.xlsx".format(serial_number))
powerGrid = pd.read_excel("11/project/result_9005.xlsx", index_col=0)

"""
highestPower = 0
for x in range(298):
    for y in range(298):
        gridPower = calculate_gridPower(powerGrid.iloc[x:x+2,y:y+2])
        if highestPower < gridPower:
            print("Power:\t{}, X:\t{}, Y:\t{}".format(gridPower, x, y))
            highestPower = gridPower
"""