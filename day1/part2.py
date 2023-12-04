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
            first = line[i]
        for num in wordtodigit.keys():
            if num == line[i:i+len(num)]:
                first = wordtodigit[num]
        if first:
            break
    
    for i in range(len(line)-1, -1, -1):
        if line[i].isdigit():
            last = line[i]
        for num in wordtodigit.keys():
            if num == line[i:i+len(num)]:
                last = wordtodigit[num]
        if last:
            break
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

import re

wordtodigit = {
    '1': '1',
    '2': '2',
    '3': '3',
    '4': '4',
    '5': '5',
    '6': '6',
    '7': '7',
    '8': '8',
    '9': '9',
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

regex_pattern = re.compile('(?=(' + '|'.join(wordtodigit.keys()) + '))')

sum = 0
for line in lines:
    nums = regex_pattern.findall(line)
    sum += int(wordtodigit[nums[0]] + wordtodigit[nums[-1]])

print(sum)