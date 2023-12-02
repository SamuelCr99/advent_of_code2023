with open("day2/input.txt") as f:
    lines = f.readlines()


s = 0
for line in lines: 
    game_num = int(line.split(":")[0].split(" ")[-1])
    rolls = line.split(":")[1]
    rounds = rolls.split(";")
    invalid_found = False

    max_red = 0
    max_blue = 0
    max_green = 0

    for round in rounds: 
        colors = round.split(",")
        for color in colors: 

            number = int(color.lstrip(" ").split(" ")[0])
            if "red" in color and number > max_red:
                max_red = number
            
            if "blue" in color and number > max_blue:
                max_blue = number

            if "green" in color and number > max_green:
                max_green = number

    power = max_red * max_blue * max_green
    s += power

print(s)