with open("input.txt") as f:
    lines = f.readlines()

def is_symbol(char):
    return not char.isdecimal() and not char == "."

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
            if row-1>=0 and col-1>=0 and is_symbol(lines[row-1][col-1]):
                is_count = True
            if row-1>=0 and is_symbol(lines[row-1][col]):
                is_count = True
            if row-1>=0 and col+1<len(line) and is_symbol(lines[row-1][col+1]):
                is_count = True
            if col-1>=0 and is_symbol(lines[row][col-1]):
                is_count = True
            if col+1<len(line) and is_symbol(lines[row][col+1]):
                is_count = True
            if row+1<len(lines) and col-1>=0 and is_symbol(lines[row+1][col-1]):
                is_count = True
            if row+1<len(lines) and is_symbol(lines[row+1][col]):
                is_count = True
            if row+1<len(lines) and col+1<len(line) and is_symbol(lines[row+1][col+1]):
                is_count = True
        if is_num and not char.isdecimal():
            if is_count:
                sum += int(num_str)
                is_count = False
            is_num = False
            num_str = ''

print(sum)