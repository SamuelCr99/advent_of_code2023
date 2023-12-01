with open("day1/input.txt") as f:
    lines = f.readlines()

sum = 0
numbers = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
for line in lines: 
    first_num = -1
    last_num = -1
    for c in line: 
        if c in numbers:
            if first_num == -1: 
                first_num = int(c)
            last_num = int(c)
    sum += first_num * 10 + last_num

print(sum)