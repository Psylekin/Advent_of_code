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
    newDf = dataDf
    newDf.X += newDf.VeloX * days
    newDf.Y += newDf.VeloY * days
    return newDf

dataDf = load_data_in_df()
lowestValue = 222
newDataDf = add_velocity(dataDf, 10521)
plot = newDataDf.plot.scatter(x="X",y="Y")
plt.show()
