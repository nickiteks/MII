import skfuzzy as fuzz
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(int(input()))
function = [1,8,100]

#mfx = fuzz.trapmf(x, function)

#print(mfx)
# 0 1 2 3 4 5 6 7 8 9 100
# 0 неподходит = 0
# 1 подходит считаeм 1 - (2-1)/(2-1)
# 2 подходит 1
# 7
# 8 подходит 1 - (8-5)/(9-5)

result = []

for i in x:
    if function[0] <= i <= function[2]:
        if function[0] <= i <= function[1]:
            result.append(1 - (function[1] - i) / (function[1] - function[0]))
            continue
        if function[1] <= i <= function[2]:
            result.append(1 - (i - function[1]) / (function[2] - function[1]))
            continue
    else:
        result.append(0)

plt.plot(result)
plt.show()

print(result)