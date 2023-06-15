import pandas as pd 
import numpy as np

data = pd.read_csv('input.csv')
print(data.columns.values[data.mean().values.argmax()])