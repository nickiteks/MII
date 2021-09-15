import skfuzzy as fuzz
import numpy as np

x = np.arange(11)

mfx = fuzz.trapmf(x, [1, 4, 8, 9])

print(mfx)
# 0 1 2 3 4 5 6 7 8 9 100
# 0 неподходит = 0
# 1 подходит считаeм 1 - (2-1)/(2-1)
# 2 подходит 1
# 7
# 8 подходит 1 - (8-5)/(9-5)
