import os

with open('1.input.txt', 'r') as file:
    lines = file.readlines()

# Calculate a total similarity score by adding up each number in the left list after 
# multiplying it by the number of times that number appears in the right list.

arr1 = []
arr2 = []

for line in lines:
    arr1.append(line.split()[0])
    arr2.append(line.split()[1])

arr1 = list(map(int, arr1))
arr2 = list(map(int, arr2))

def similarity_score(arr1, arr2):
    score = 0
    for i in arr1:
        score += arr2.count(i) * i
    return score

print(similarity_score(arr1, arr2))