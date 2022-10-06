dataIn = [-1, 2, -3, 4, -5, 6]


def myAbs(data):
    return data if data > 0 else -data


def mySum(data1, data2):
    return data1 + data2


def myMap(func, *data):
    result = []
    for d in zip(*data):
        result.append(func(*d))
    return result


def myMapGenerator(func, *data):
    return (func(*d) for d in zip(*data))


print(myMap(myAbs, dataIn))
print(myMap(mySum, dataIn, dataIn))

print(list(myMapGenerator(myAbs, dataIn)))
print(list(myMapGenerator(mySum, dataIn, dataIn)))
