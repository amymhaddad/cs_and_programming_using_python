
import math


# def calculate_end_balance(balance, annualInterestRate, monthly_payment):
#     month = 1
#     while month <= 12:
#         monthly_interest_rate = (annualInterestRate) / 12.0
#         monthly_unpaid_balance = balance - monthly_payment
#         new_balance = (monthly_unpaid_balance) + (monthly_interest_rate * monthly_unpaid_balance)

#         balance = new_balance
#         month += 1

#     return balance

balance = 320000
annualInterestRate = .2

monthly_interest_rate = (annualInterestRate) / 12.0

lowest_payment = (balance / 12)
highest_payment = balance * (1 + math.pow(monthly_interest_rate, 12)) / 12.0
highest_payment = balance * (1 + monthly_interest_rate ** 12) / 12.0

print(balance * (1 + (monthly_interest_rate ** 12)) / 12.0)

# Monthly payment upper bound = (Balance x (1 + Monthly inter est rate)12) / 12.0



# def monthly_payment(balance, annualInterestRate):
#     monthly_interest_rate = annualInterestRate / 12.0

 
    
#     lowest_payment = (balance / 12)
#     highest_payment = balance * (1 + math.pow(monthly_interest_rate, 12)) / 12.0
#     mid_payment = (lowest_payment + highest_payment) // 2

#     ending_balance = balance

#     while ending_balance >= 0:
#         ending_balance = calculate_end_balance(balance, annualInterestRate, monthly_payment)

#         if ending_balance > 0:
#             lowest_payment = mid_payment
#         else:   
#             highest_payment = mid_payment
        
#     return monthly_payment(annualInterestRate, balance[lowest_payment:highest_payment])
#     # return ending_balance



# payment =  monthly_payment(320000, .2)
# print(payment)

#29157.09
