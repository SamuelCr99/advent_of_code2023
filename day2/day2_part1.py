with open("day2/input.txt") as f:
    lines = f.readlines()


s = 0
for line in lines: 
    game_num = int(line.split(":")[0].split(" ")[-1])
    rolls = line.split(":")[1]
    rounds = rolls.split(";")
    invalid_found = False
    for round in rounds: 
        colors = round.split(",")
        for color in colors: 

            number = int(color.lstrip(" ").split(" ")[0])
            if number > 12 and "red" in color:
                invalid_found = True
                break
            
            if number > 13 and "green" in color:
                invalid_found = True
                break

            if number > 14 and "blue" in color:
                invalid_found = True
                break

        if invalid_found:
            break

    if not invalid_found:
        s += game_num 

print(s)