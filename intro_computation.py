


# Need to use the split here bc in next function we need to look at each item, not the string as a whole.
def number_generator():
    return input("Enter 10 numbers separated by a space: ").split()

user_numbers = number_generator()

#First, need to go through each number and change the type from string to int
def largest_odd_number(user_numbers):
    user_numbers_as_ints =[int(number) for number in user_numbers] 
    return max([number for number in user_numbers_as_ints if number % 2 != 0])
 

x = largest_odd_number(user_numbers)
print(x)
    
