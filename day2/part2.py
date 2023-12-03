with open('input.txt') as f:
    lines = f.readlines()

sum = 0
for line in lines:
    line = line.rstrip()
    max_red, max_blue, max_green = 0, 0, 0
    game, colors = line.split(':')
    colors = [color.split(',') for color in colors.split(';')]
    for color_section in colors:
        for color_num in color_section:
            _, num, color = color_num.split(' ')
            if color == "red":
                max_red = max(max_red, int(num))
            elif color == "blue":
                max_blue = max(max_blue, int(num))
            elif color == "green":
                max_green = max(max_green, int(num))
    sum += max_red * max_green * max_blue
    
print(sum)

from functools import reduce
import re

red_regex_pattern = re.compile(r'(\d+) red')
green_regex_pattern = re.compile(r'(\d+) green')
blue_regex_pattern = re.compile(r'(\d+) blue')

sum = 0
for line in lines:
    max_red = max(map(int, red_regex_pattern.findall(line)))
    max_green = max(map(int, green_regex_pattern.findall(line)))
    max_blue = max(map(int, blue_regex_pattern.findall(line)))
    sum += max_red * max_green * max_blue

print(sum)

# One liner (not counting imports) xd
print(reduce(lambda sum, line: sum + (max(map(int, re.findall(r'(\d+) red', line))) * max(map(int, re.findall(r'(\d+) green',line))) * max(map(int, re.findall(r'(\d+) blue',line)))), [0, *lines]))