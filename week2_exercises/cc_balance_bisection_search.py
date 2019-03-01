
import math


def calculate_end_balance(balance, annualInterestRate, monthly_payment):
    month = 1
    while month <= 12:
        monthly_interest_rate = (annualInterestRate) / 12.0
        monthly_unpaid_balance = balance - monthly_payment
        new_balance = (monthly_unpaid_balance) + (monthly_interest_rate * monthly_unpaid_balance)

        balance = new_balance
        month += 1

    return balance


def monthly_payment(balance, annualInterestRate):

    monthly_interest_rate = (annualInterestRate) / 12.0
    lowest_payment = balance / 12
    highest_payment = (balance * (1 + monthly_interest_rate) ** 12) / 12.0
    monthly_payment = (lowest_payment + highest_payment) // 2

    ending_balance = balance
     
    while lowest_payment <= highest_payment:
        ending_balance = calculate_end_balance(balance, annualInterestRate, monthly_payment)

        if monthly_payment * 12 == ending_balance:
            break

        else: 
            if monthly_payment * 12 < ending_balance:
                lowest_payment = monthly_payment
            elif monthly_payment * 12 > ending_balance:
                highest_payment = monthly_payment

        monthly_payment = (lowest_payment + highest_payment) // 2

    return monthly_payment

print(monthly_payment(32000, .2))



    # while lowest_payment <= highest_payment:
    #     #getting a neg here
    #     ending_balance = calculate_end_balance(balance, annualInterestRate, monthly_payment)
        
        
    #     if ending_balance <= 0:
    #         break
        
    #     else:
    #         if monthly_payment < ending_balance:
    #             lowest_payment = monthly_payment
    #         else:
    #             highest_payment = monthly_payment
    #     monthly_payment = (lowest_payment + highest_payment) // 2

    #     return monthly_payment



    # while lowest_payment <= highest_payment:
    #     calc_ending_balance = calculate_end_balance(balance, annualInterestRate, monthly_payment)
        
    #     if mid_payment == monthly_payment:
    #         break
        
    #     else:
    #         if mid_payment < monthly_payment:
    #             low = mid_payment
    #         else:
    #             high = mid_payment
        
    #     return monthly_payment

print(monthly_payment(320000, .2))


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
