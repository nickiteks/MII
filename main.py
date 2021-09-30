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
    print(f"Это на {count_cluster(x, [0, 25, 44, 100])} молодой возвраст")
    print(f"Это на {count_cluster(x, [0, 44, 60, 100])} средний  возвраст")
    print(f"Это на {count_cluster(x, [0, 60, 75, 100])} пожилой возвраст")
    print(f"Это на {count_cluster(x, [0, 75, 90, 100])} старческий возвраст")


trigger = True
while trigger:
    clustering(int(input("Введите возвраст ")))