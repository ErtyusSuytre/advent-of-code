with open("input.txt") as f:
    lines = f.readlines()

def is_symbol(char):
    return not char.isdecimal() and not char == "."

NEIGHBORS = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),           (0, 1),
    (1, -1),  (1, 0),  (1, 1)
]

sum = 0
is_num = False
is_count = False
num_str = ''
for row, line in enumerate(lines):
    line = line.rstrip()
    for col, char in enumerate(line):
        if char.isdecimal():
            is_num = True
        if is_num and char.isdecimal():
            num_str += char
            # Check neighbors for special symbols (not . or digits)
            for dx, dy in NEIGHBORS:
                if 0 <= row + dx < len(lines) and 0 <= col + dy < len(line) and is_symbol(lines[row + dx][col + dy]):
                    is_count = True
                    break
        if is_num and not char.isdecimal():
            if is_count:
                sum += int(num_str)
                is_count = False
            is_num = False
            num_str = ''

print(sum)