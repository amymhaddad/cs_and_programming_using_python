
import math

# def debt_payoff(balance, annualInterestRate):

balance = 3329
annualInterestRate = 0.2



def debt_payoff(balance, annualInterestRate):
    month = 1
    monthly_payment = balance / 12
    if monthly_payment % 2 != 0:
        monthly_payment_multiple_of_ten = (monthly_payment // 10) * 10 + 10
    else:
        monthly_payment_multiple_of_ten = monthly_payment
    
    
    for month in range(13):
        monthly_unpaid_balance = balance - monthly_payment_multiple_of_ten    
        monthly_interest_rate = (annualInterestRate) / 12.0
        
        new_balance = monthly_unpaid_balance + (monthly_interest_rate * monthly_unpaid_balance)   
        balance = new_balance
        month += 1

        if balance <= 0:
            break
    if balance > 0:
        remaining_balance = (monthly_payment_multiple_of_ten + balance) / 12
        print(remaining_balance)
        #     monthly_payment_multiple_of_ten = monthly_payment_multiple_of_ten + remaining_balance


#HERE for updating the remaining balance and adding this balance to the monthly payment, make this monthly payment a multiple of 10 and see when balance is 0 (break)
 
    return monthly_payment_multiple_of_ten

print(debt_payoff(balance, annualInterestRate))


# print(debt_payoff(3329, 0.2))
#lowest payment = 310


# Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)

