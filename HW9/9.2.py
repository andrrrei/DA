import pandas as pd 
import numpy as np

data = np.genfromtxt('input.csv', delimiter=',')
mins = list(float(data[:, i:(i + 1)].mean()) for i in range(0, 10))
print(mins.index(sorted(mins)[0]) + 1)