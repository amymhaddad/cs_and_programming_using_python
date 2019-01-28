
def user_numbers():
    integers = input("Enter 10 integers: ").split()
    return [int(number) for number in integers]
    
numbers = user_numbers()

odd_numbers = list(filter(lambda x: (x % 2 != 0) , numbers))
print(max(odd_numbers))
