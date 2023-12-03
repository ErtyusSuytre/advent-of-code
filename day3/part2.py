with open("input.txt") as f:
    lines = f.readlines()
    
NEIGHBORS = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),           (0, 1),
    (1, -1),  (1, 0),  (1, 1)
]

def get_num (grid, row, col):
    # Get first digit
    while col - 1 >= 0 and grid[row][col - 1].isdecimal():
        col -= 1
        
    # Get line before the start of number
    start_row = grid[row][:col]
    
    # Get number
    num_str = ''
    while col < len(grid[row]) and grid[row][col].isdecimal():
        num_str += grid[row][col]
        col += 1

    # Get line after the end of number
    end_row = grid[row][col:]
    
    # Replace number with periods
    grid[row] = start_row + '.'*len(num_str) + end_row
    
    return int(num_str)

total_sum = 0

for row, line in enumerate(lines):
    line = line.rstrip()
    for col, char in enumerate(line):
        if char == '*':
            num_numbers = []
            # Check 8 neighbors for numbers and record them
            for dx, dy in NEIGHBORS:
                if 0 <= row + dx < len(lines) and 0 <= col + dy < len(line) and lines[row + dx][col + dy].isdecimal():
                    num = get_num(lines, row + dx, col + dy)
                    num_numbers.append(num)
            # If 2 numbers were found, multiply them, and add them to the total
            if len(num_numbers) == 2:
                total_sum += num_numbers[0] * num_numbers[1]

print(total_sum)