import os

# The engineers are trying to figure out which reports are safe. 
# The Red-Nosed reactor safety systems can only tolerate levels that are either g
# radually increasing or gradually decreasing. So, a report only counts as safe if 
# both of the following are true:
#     The levels are either all increasing or all decreasing.
#     Any two adjacent levels differ by at least one and at most three.

# Part 2 
# Now, the same rules apply as before, except if removing a single level from an unsafe
# report would make it safe, the report instead counts as safe.

with open('2.input.txt', 'r') as file:
    lines = file.readlines()

unsafe = 0
safe = 0

def isSafe(reports):
    ascending = reports == sorted(reports)
    descending = reports == sorted(reports, reverse=True)
    if not ascending and not descending:
        return 0
    
    diffs = [abs(a - b) for a, b in zip(reports, reports[1:])]
    if all([1 <= diff <= 3 for diff in diffs]):
        return 1
    else:
        return 0

def remove_one_element(input_list):
    """
    Generate a set of lists by removing one element from the input list.
    
    Args:
        input_list (list): The input list to remove elements from
    
    Returns:
        set: A set of lists, where each list is created by removing one element from the input list
    """
    print(input_list)
    return {
        tuple(input_list[:i] + input_list[i+1:])
        for i in range(len(input_list))
    }

for line in lines:
    reports = list(map(int,line.split()))
    if isSafe(reports):
        safe += 1
    else:
        # Check all permutations of list
        for report in remove_one_element(reports):
            if isSafe(list(report)):
                # print(str(report) + " safe")
                safe += 1
                break
        unsafe += 1


print("Safe: ", safe)
print("Unsafe: ", unsafe)
