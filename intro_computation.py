def user_numbers():
    integers = input("Enter 10 integers: ").split()
    return [int(number) for number in integers]
    
numbers = user_numbers()


def calculation(numbers):
    odd_numbers = [number for number in numbers if number % 2 != 0]
    return max(odd_numbers)

x = calculation(numbers)
print(x)
