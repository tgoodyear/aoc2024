import re

# Read lines from 3.input.txt into a list
with open('/Users/tgoodyear/code/aoc2024/03/python/3.input.txt', 'r') as file:
    lines = file.readlines()

lines = [line.strip() for line in lines]
inputText = "\n".join(lines)

# Find all instances of mul(x,y) and capture the x and y values
pattern = re.compile(r'mul\(\d+,\d+\)')
result = pattern.findall(inputText)

# Extract the x and y values from the result and multiply them
result = sum([int(re.findall(r'\d+', x)[0]) * int(re.findall(r'\d+', x)[1]) for x in result])

print(result)