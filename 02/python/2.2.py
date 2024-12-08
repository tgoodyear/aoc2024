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
    reports = list(map(int,line.split()))
    ascending = reports == sorted(reports)
    descending = reports == sorted(reports, reverse=True)
    if not ascending and not descending:
        return 0
    
    diffs = [abs(a - b) for a, b in zip(reports, reports[1:])]
    if all([1 <= diff <= 3 for diff in diffs]):
        return 1
    else:
        return 0


for line in lines:
    reports = list(map(int,line.split()))
    print(reports)
    direction = 0
    unsafeElems = 0
    lineSafe = True
    pops = 0
    for i, element in enumerate(reports):
        popElem = i
        if unsafeElems > 1:
            unsafe += 1
            lineSafe = False
            break
        if i == 0:
            continue

        curr = reports[i]
        prev = reports[i-1]

        # Set ascending or descending
        if direction == 0:
            if curr > prev:
                direction = 1
            elif curr < prev:
                direction = -1
            else:
                unsafeElems += 1
                print("Elems equal: ", curr, prev)
                if(unsafeElems > 1):
                    lineSafe = False
                    print("More than 1 unsafe")
                    unsafe += 1
                    break
                reports.pop(popElem)
                continue
        else:
            if prev > curr and direction == 1:
                unsafeElems += 1
                if(unsafeElems > 1):
                    lineSafe = False
                    print("More than 1 unsafe")
                    unsafe += 1
                    break
                print("Unsafe:", curr, ">", prev, direction)
                reports.pop(popElem)
                continue
            elif prev < curr and direction == -1:
                unsafeElems += 1
                if(unsafeElems > 1):
                    lineSafe = False
                    print("More than 1 unsafe")
                    unsafe += 1
                    break
                print("Unsafe:", curr, "<", prev, direction)
                reports.pop(popElem)
                continue
        
        # Check if the difference is between 1 and 3
        diff = abs(curr - prev)
        if not((diff > 0) and (diff < 4)):
            unsafeElems += 1
            print("Unsafe: ", curr, " - ", prev, " = ", diff)
            if(unsafeElems > 1):
                lineSafe = False
                print("More than 1 unsafe")
                unsafe += 1
                break
            reports.pop(popElem)
            continue
        
    safe += 1 if lineSafe else 0
    # if not lineSafe:
    print(reports, lineSafe,direction)

print("Safe: ", safe)
print("Unsafe: ", unsafe)
