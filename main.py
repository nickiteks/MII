import matplotlib.pyplot as plt


def count_cluster(x, function):
    result = []
    if function[0] <= x <= function[3]:
        if function[0] <= x <= function[1]:
            result.append(1 - (function[1] - x) / (function[1] - function[0]))
        if function[1] <= x <= function[2]:
            result.append(1)
        if function[2] <= x <= function[3]:
            result.append(1 - (x - function[2]) / (function[3] - function[2]))
    else:
        result.append(0)
    return result


def clustering(x):
    result = []
    print(f"Это на {count_cluster(x, [0, 1, 20, 100])} молодой возвраст")
    print(f"Это на {count_cluster(x, [20, 21, 40, 100])} средний  возвраст")
    print(f"Это на {count_cluster(x, [40, 41, 70, 100])} пожилой возвраст")
    print(f"Это на {count_cluster(x, [70, 71, 90, 100])} старческий возвраст")
    result.append(count_cluster(x, [40, 41, 70, 100]))
    result.append(count_cluster(x, [70, 71, 90, 100]))
    print(result)

    max = result[0]
    for i in result:
        if i > i:
            max = i

    print(max)


while True:
    clustering(int(input("Введите возвраст ")))
