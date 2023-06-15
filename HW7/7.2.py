import numpy as np

with open('input.txt') as f:
  first, last, amount = map(int, f.read().split('\n'))
arr = np.linspace(first, last, amount)
arr[0:len(arr):7] /= 3
arr[4:len(arr):7] *= 2
with open('output.txt', 'w') as f:
  for i in range(len(arr)):
    print(f"{arr[i]:.2f}", file=f)
