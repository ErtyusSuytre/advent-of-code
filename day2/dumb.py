import re
print(sum([int(re.search(r'Game (\d+):', line).group(1)) if max(map(int, re.findall(r'(\d+) red',line))) <= 12 and max(map(int, re.findall(r'(\d+) green',line))) <= 13 and max(map(int, re.findall(r'(\d+) blue',line))) <= 14 else 0 for line in open('input.txt').readlines()]))