import re
import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt

def connection_test():
    return 1

def transform_input(input):
    return list(map(int, re.findall(r'\-?\d+', input)))

def load_data_in_df(): #untested
    with open("project/input.txt") as document:
        data = document.readlines()
        data = list(map(lambda x: transform_input(x), data))
        df = pd.DataFrame(data, columns=["X", "Y", "VeloX", "VeloY"])
        return df

def add_velocity(dataDf, days): #untested
    dataDf.X += dataDf.VeloX * days
    dataDf.Y += dataDf.VeloY * days
    return dataDf

newDataDf = dataDf = load_data_in_df()
lowestValue = 222

for day in range(12000):
    newDataDf = add_velocity(newDataDf, 1)
    if len(newDataDf.X.unique()) < lowestValue:
        plt.clf()
        lowestValue = len(newDataDf.X.unique())
        lowestDay = day
        newDataDf.plot.scatter(x="X",y="Y")
        plt.show()

print("Day: {}, Value: {}".format(lowestDay, lowestValue))
plt.clf()
add_velocity(dataDf, lowestDay -1).plot.scatter(x="X",y="Y")
add_velocity(dataDf, lowestDay +1).plot.scatter(x="X",y="Y")
add_velocity(dataDf, lowestDay +2).plot.scatter(x="X",y="Y")
add_velocity(dataDf, lowestDay +3).plot.scatter(x="X",y="Y")
add_velocity(dataDf, lowestDay +4).plot.scatter(x="X",y="Y")
add_velocity(dataDf, lowestDay +5).plot.scatter(x="X",y="Y")
add_velocity(dataDf, lowestDay +6).plot.scatter(x="X",y="Y")
add_velocity(dataDf, lowestDay +7).plot.scatter(x="X",y="Y")

plt.show()