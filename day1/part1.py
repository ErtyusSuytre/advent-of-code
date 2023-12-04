with open('input.txt') as f:
    lines = f.readlines()

sum = 0
for line in lines:
    first, last = None, None
    for c in line:
        if c.isdigit():
            first = c
            break
    for c in line[::-1]:
        if c.isdigit():
            last = c
            break
    sum += int(first+last)
                
print(sum)

import re

regex_pattern = re.compile(r'\d')

sum = 0
for line in lines:
    nums = regex_pattern.findall(line)
    sum += int(nums[0]+nums[-1])

print(sum)