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

def report_findings_in_line(coordinate, newDataDf):
    return newDataDf.loc[:, coordinate].value_counts()[:2]

dataDf = load_data_in_df()
highestValue = 0

for days in range(1000):
    newDataDf = add_velocity(dataDf, 1)
    print(
        report_findings_in_line("Y", newDataDf)
    )


"""
sns.jointplot(x=df.X, y=df.Y, kind='scatter')
plt.show()
"""