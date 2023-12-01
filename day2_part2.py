with open("day1/input.txt") as f:
    lines = f.readlines()

sum = 0
number_translate = {'zero' : 0,
                    'one' : 1,
                    'two' : 2,
                    'three': 3,
                    'four' : 4,
                    'five' : 5,
                    'six' : 6,
                    'seven' : 7,
                    'eight' : 8,
                    'nine' : 9,
                    '0' : 0,
                    '1' : 1,
                    '2' : 2,
                    '3' : 3,
                    '4' : 4,
                    '5' : 5,
                    '6' : 6,
                    '7' : 7,
                    '8' : 8,
                    '9' : 9,
                    }

for line in lines: 
    first_num = -1
    last_num = -1
    for i in range(len(line)):
        if line[i] in number_translate:
            if first_num == -1:
                first_num = number_translate[line[i]]
            last_num = number_translate[line[i]]
        
        elif line[i:i+3] in number_translate:
            if first_num == -1:
                first_num = number_translate[line[i:i+3]]
            last_num = number_translate[line[i:i+3]]

        elif line[i:i+4] in number_translate:
            if first_num == -1:
                first_num = number_translate[line[i:i+4]]
            last_num = number_translate[line[i:i+4]]

        elif line[i:i+5] in number_translate:
            if first_num == -1:
                first_num = number_translate[line[i:i+5]]
            last_num = number_translate[line[i:i+5]]


    sum += first_num * 10 + last_num

print(sum)