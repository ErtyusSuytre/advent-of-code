with open("input.txt") as f:
    lines = f.readlines()

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
            # Check neighbors for digits
            if row-1 >= 0 and col-1 >= 0 and lines[row-1][col-1].isdecimal():
                line, num = get_num(lines[row-1], col-1)
                lines[row-1] = line
                num_numbers.append(num)
            if row-1 >= 0 and lines[row-1][col].isdecimal():
                line, num = get_num(lines[row-1], col)
                lines[row-1] = line
                num_numbers.append(num)
            if row-1 >= 0 and col+1 < len(line) and lines[row-1][col+1].isdecimal():
                line, num = get_num(lines[row-1], col+1)
                lines[row-1] = line
                num_numbers.append(num)
            if col-1 >= 0 and lines[row][col-1].isdecimal():
                line, num = get_num(lines[row], col-1)
                lines[row] = line
                num_numbers.append(num)
            if col+1 < len(line) and lines[row][col+1].isdecimal():
                line, num = get_num(lines[row], col+1)
                lines[row] = line
                num_numbers.append(num)
            if row+1 < len(lines) and col-1 >= 0 and lines[row+1][col-1].isdecimal():
                line, num = get_num(lines[row+1], col-1)
                lines[row+1] = line
                num_numbers.append(num)
            if row+1 < len(lines) and lines[row+1][col].isdecimal():
                line, num = get_num(lines[row+1], col)
                lines[row+1] = line
                num_numbers.append(num)
            if row+1 < len(lines) and col+1 < len(line) and lines[row+1][col+1].isdecimal():
                line, num = get_num(lines[row+1], col+1)
                lines[row+1] = line
                num_numbers.append(num)
            
            if len(num_numbers) == 2:
                total_sum += num_numbers[0] * num_numbers[1]

print(total_sum)