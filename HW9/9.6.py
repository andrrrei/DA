import pandas as pd 
import numpy as np

def triangle(item):
    if (item[0] < item[1] + item[2]) and (item[1] < item[0] + item[2]) and (item[2] < item[0] + item[1]) :
        return True
    else :
        return False

data = pd.read_csv('input.csv')
data = list(triangle(item) for item in data.values)
count = 0
for i in data:
    count += i
print(count)