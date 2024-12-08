import os

# The engineers are trying to figure out which reports are safe. 
# The Red-Nosed reactor safety systems can only tolerate levels that are either g
# radually increasing or gradually decreasing. So, a report only counts as safe if 
# both of the following are true:
#     The levels are either all increasing or all decreasing.
#     Any two adjacent levels differ by at least one and at most three.

with open('2.input.txt', 'r') as file:
    lines = file.readlines()

unsafe = 0
safe = 0

for line in lines:
    reports = list(map(int,line.split()))
    ascending = reports == sorted(reports)
    descending = reports == sorted(reports, reverse=True)
    if not ascending and not descending:
        unsafe += 1
        continue
    
    diffs = [abs(a - b) for a, b in zip(reports, reports[1:])]
    if all([1 <= diff <= 3 for diff in diffs]):
        safe += 1
    else:
        unsafe += 1

print(safe)
