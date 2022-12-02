import numpy as np
import pandas as pd

from day_1_input import array

b=[]
for elem in array:
    b.append(np.sum(elem))
bs = np.array(b)
bs.sort()
print("Most calories: ", bs[-1])
print("Sum of three highest calories: ", bs[-3:].sum())
