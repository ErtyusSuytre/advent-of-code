with open('input.txt') as f:
    lines = f.readlines()

sum = 0
for line in lines:
    line = line.rstrip()
    max_red, max_blue, max_green = 0, 0, 0
    game, colors = line.split(':')
    game_num = int(game.split(' ')[1])
    colors = colors.split(';')
    colors = [color.split(',') for color in colors]
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