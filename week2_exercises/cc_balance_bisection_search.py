
import math


def calculate_end_balance(balance, annualInterestRate, payment):
    month = 1
    while month <= 12:
        monthly_interest_rate = (annualInterestRate) / 12.0
        monthly_unpaid_balance = balance - payment
        new_balance = (monthly_unpaid_balance) + (monthly_interest_rate * monthly_unpaid_balance)

        balance = new_balance
        month += 1

    return balance

# print(calculate_end_balance(200, .2, 100))

def monthly_payment(balance, annualInterestRate):

    monthly_interest_rate = annualInterestRate / 12.0
    lowest_payment = balance / 12
    highest_payment = (balance * (1 + monthly_interest_rate) ** 12) / 12.0

    ending_balance = balance
     
    #Use while True, which keeps the loop running. THis is a better option than while ending_balance >= 0 b/c t
    #It's repetitive with the condition below: ending_balance <= 0
    while True:
        payment = (lowest_payment + highest_payment) // 2
        ending_balance = calculate_end_balance(balance, annualInterestRate, payment)
        print(ending_balance)

        if ending_balance <= 0:
            # return payment
            return payment
        else:
            if ending_balance > 0:
                lowest_payment = payment
            else:
                highest_payment = payment

monthly_payment(320000, .2)

#Why isn't 2nd function iterating through each ending_balance?

29157.09

# low = 0
# high = 10
# mid = (low + high) // 2

# num = 7

# while low <= high:
#    if mid == num:
#       print(mid)
#       break
#    elif mid < num:
#       low = mid
#    else:
#       high = mid
#    mid = (low + high) // 2


#Option
# while lowest_payment <= highest_payment:
#         ending_balance = calculate_end_balance(balance, annualInterestRate, monthly_payment)

#         if monthly_payment * 12 == ending_balance:
#             break

#         else: 
#             if monthly_payment * 12 < ending_balance:
#                 lowest_payment = monthly_payment
#             elif monthly_payment * 12 > ending_balance:
#                 highest_payment = monthly_payment

#         monthly_payment = (lowest_payment + highest_payment) // 2

#     return monthly_payment