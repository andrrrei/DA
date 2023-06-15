import pandas as pd 
import numpy as np

data = pd.read_csv('input.csv')
print(1 if data.values.sum() >- 8000000 else 0, end = ' ')
print(data.columns.values[data.sum().values.argmax()])