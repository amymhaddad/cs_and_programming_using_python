
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
     
    while True:
        payment = (lowest_payment + highest_payment) // 2
        ending_balance = calculate_end_balance(balance, annualInterestRate, payment)
        print(ending_balance)

        if ending_balance <= 0:
           
            return payment
        else:
            if ending_balance > 0:
                lowest_payment = payment
            else:
                highest_payment = payment

monthly_payment(320000, .2)