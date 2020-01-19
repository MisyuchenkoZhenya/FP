# binary search imperative

import math

def binarySearch(data, target):
    i = 0
    j = len(data)
    k = 0
    while i < j:
        k = math.floor((i + j) / 2)
        if target <= data[k]:
            j = k
        else:
            i = k + 1

    return i if data[ i ] == target else -1


print(binarySearch([3,4,5,6,7,8,9], 8))

# binary search recursive

def binaryRecursiveSearch(data, target, start, end):
    if end < 1:
        return data[0]

    middle = math.floor(start + (end - start) / 2)

    if target == data[middle]:
        return middle

    if end - 1 == start:
        return data[end] if abs(data[start] - target) > abs(data[end] - target) else data[start]
    
    if target > data[middle]:
        return binaryRecursiveSearch(data, target, middle, end)

    if target < data[middle]:
        return binaryRecursiveSearch(data, target, start, middle)

arr = [9, 7, 5, 4, 3]
print(binaryRecursiveSearch(arr, 8, 0, len(arr) - 1))


# minmax imperative

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [6, 7, 8]
]

def minmaxImperative(matrix):
    maxValue = None
    minValue = None

    for row in matrix:
        for item in row:
            if(maxValue is None or item > maxValue):
                maxValue = item
        if(minValue is None or maxValue < minValue):
            minValue = maxValue

    return minValue

print(minmaxImperative(matrix))


# minmax recursive

recursiveMatrix = [
    [1, 2, 3],
    [4, 5, 6],
    [6, 7, 8]
]

def minmaxRecursive(matrix):
    maxArr = []
    for row in matrix:
        maxArr.append(max(row))

    return min(maxArr)

print(minmaxRecursive(recursiveMatrix))
