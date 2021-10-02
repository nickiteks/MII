import skfuzzy as fuzz
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(int(input('Для скольки ядер ')))
function = [1,4,10]
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

print(result[len(x) - 1])
for i in range(len(result)):
    result[i] = 1-result[i]
print(result[len(x) - 1])
