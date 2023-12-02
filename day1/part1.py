with open('input.txt') as f:
    lines = f.readlines()

sum = 0
for line in lines:
    first, last = None, None
    for c in line:
        if c.isdigit():
            if first is None:
                first = c
                last = c
            else:
                last = c
    sum += int(first+last)
                
print(sum)

import re

sum = 0
for line in lines:
    nums = re.findall(r'\d', line)
    sum += int(nums[0]+nums[-1])

print(sum)