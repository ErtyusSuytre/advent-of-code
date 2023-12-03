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