import skfuzzy as fuzz
import numpy as np

x = np.arange(11)
function = [1, 2, 5, 9]

mfx = fuzz.trapmf(x, function)

print(mfx)
# 0 1 2 3 4 5 6 7 8 9 100
# 0 неподходит = 0
# 1 подходит считаeм 1 - (2-1)/(2-1)
# 2 подходит 1
# 7
# 8 подходит 1 - (8-5)/(9-5)

result = []

for i in x:
    if function[0] <= i <= function[3]:
        if function[0] <= i <= function[1]:
            result.append(1 - (function[1] - i) / (function[1] - function[0]))
            continue
        if function[1] <= i <= function[2]:
            result.append(1)
            continue
        if function[2] <= i <= function[3]:
            result.append(1 - (i - function[2]) / (function[3] - function[2]))
            continue
    else:
        result.append(0)

print(result)