
user_numbers = int(input("Enter 10 numbers: "))

list_odd_numbers = []
for number in user_numbers:
    divisibility_checker = number % 2
    if divisibility_checker != 0:
        list_odd_numbers.append(divisibility_checker)
print(max(list_odd_numbers))

