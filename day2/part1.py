with open('input.txt') as f:
    lines = f.readlines()
    
LIMIT_RED, LIMIT_GREEN, LIMIT_BLUE = 12, 13, 14

sum = 0
for line in lines:
    line = line.rstrip()
    max_red, max_blue, max_green = 0, 0, 0
    game, colors = line.split(':')
    game_num = int(game.split(' ')[1])
    colors = [color.split(',') for color in colors.split(';')]
    is_possible = True
    for color_section in colors:
        for color_num in color_section:
            _, num, color = color_num.split(' ')
            if color == "red":
                if int(num) > LIMIT_RED:
                    is_possible = False
                    break
            elif color == "green":
                if int(num) > LIMIT_GREEN:
                    is_possible = False
                    break
            elif color == "blue":
                if int(num) > LIMIT_BLUE:
                    is_possible = False
                    break
    if is_possible:
        sum += game_num

print(sum)

from functools import reduce
import re

game_regex_pattern = re.compile(r'Game (\d+):')
red_regex_pattern = re.compile(r'(\d+) red')
green_regex_pattern = re.compile(r'(\d+) green')
blue_regex_pattern = re.compile(r'(\d+) blue')

sum = 0
for line in lines:
    game_num = int(game_regex_pattern.search(line).group(1))
    max_reds = max(map(int, red_regex_pattern.findall(line)))
    max_greens = max(map(int, green_regex_pattern.findall(line)))
    max_blues = max(map(int, blue_regex_pattern.findall(line)))
    if max_reds <= LIMIT_RED and max_greens <= LIMIT_GREEN and max_blues <= LIMIT_BLUE:
        sum += game_num

print(sum)

# One liner (not counting imports) xd
print(reduce(lambda game1, game2: game1 + game2, [int(re.search(r'Game (\d+):', line).group(1)) if max(map(int, re.findall(r'(\d+) red',line))) <= 12 and max(map(int, re.findall(r'(\d+) green',line))) <= 13 and max(map(int, re.findall(r'(\d+) blue',line))) <= 14 else 0 for line in lines]))