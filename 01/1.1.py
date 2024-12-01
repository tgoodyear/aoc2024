import os

with open('1.input.txt', 'r') as file:
    lines = file.readlines()

arr1 = []
arr2 = []

for line in lines:
    arr1.append(line.split()[0])
    arr2.append(line.split()[1])

arr1 = list(map(int, arr1))
arr2 = list(map(int, arr2))

arr1.sort()
arr2.sort()

result = sum([abs(a - b) for a, b in zip(arr1, arr2)])
print(result)