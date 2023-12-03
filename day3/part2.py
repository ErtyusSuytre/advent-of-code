with open("input.txt") as f:
    lines = f.readlines()
    
NEIGHBORS = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),           (0, 1),
    (1, -1),  (1, 0),  (1, 1)
]

def get_num (line, col):
    # Get first digit
    while col - 1 >= 0 and line[col - 1].isdecimal():
        col -= 1
    num_str = ''
    while col < len(line) and line[col].isdecimal():
        num_str += line[col]
        line = line[:col] + '.' + line[col+1:]
        col += 1
    return line, int(num_str)

total_sum = 0

for row, line in enumerate(lines):
    line = line.rstrip()
    for col, char in enumerate(line):
        if char == '*':
            num_numbers = []
            # Check 8 neighbors for digits
            for dx, dy in NEIGHBORS:
                if 0 <= row + dx < len(lines) and 0 <= col + dy < len(line) and lines[row + dx][col + dy].isdecimal():
                    line, num = get_num(lines[row + dx], col + dy)
                    lines[row + dx] = line
                    num_numbers.append(num)
            
            if len(num_numbers) == 2:
                total_sum += num_numbers[0] * num_numbers[1]

print(total_sum)