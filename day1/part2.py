wordtodigit = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}

with open('input.txt') as f:
    lines = f.readlines()

sum = 0
for line in lines:
    first, last = None, None
    for i in range(len(line)):
        if line[i].isdigit():
            if first is None:
                first = line[i]
            last = line[i]
        else:
            for num in wordtodigit.keys():
                if i+len(num) <= len(line) and num == line[i:i+len(num)]:
                    if first is None:
                        first = wordtodigit[num]
                    last = wordtodigit[num]
                
    sum += int(first+last)
                
print(sum)

import re

regex_pattern = re.compile('(?=(' + r'\d|' + '|'.join(wordtodigit.keys()) + '))')

sum = 0
for line in lines:
    nums = regex_pattern.findall(line)
    first, last = nums[0], nums[-1]
    if not first.isdigit():
        first = wordtodigit[first]
    if not last.isdigit():
        last = wordtodigit[last]
    sum += int(first + last)

print(sum)