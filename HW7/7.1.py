import numpy as np

with open('input.txt') as f:
  a = f.read().split()
arr = np.array(a, dtype=int)
print(np.searchsorted(arr, 1415))
