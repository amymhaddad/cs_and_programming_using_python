
total = ''
s = '1.23, 2.4, 3.123'

number = int(s[:])
print(number)

new_string = ''
s = '1.23,2.4,3.123'
ints = 0
space = " "

for num in s:
    if num == ',':
        new_string += " "
    if num != ',':
        new_string += num

number_1 = float(new_string[:4])
number_2 = float(new_string[4:8])
number_3 = float(new_string[8:])

total = number_1 + number_2 + number_3
print(total)