import skfuzzy as fuzz
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(int(input('Для скольки ядер ')))
function = [1,8,100]
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