


def debt_payoff(balance, annualInterestRate, montly_payment):
    month = 1
    
    while month <= 12:
        monthly_interest_rate = (annualInterestRate) / 12.0
        unpaid_balance = balance - fixed_montly_payment
        new_balance = (unpaid_balance) + (monthly_interest_rate * unpaid_balance)
        balance = new_balance
        month += 1

    ending_balance = round(balance, 2)
    final_output = "Remaining balance: " + str(ending_balance)
    return ending_balance

def find_monthly_payment(balance, annualInterestRate):
    ending_balance = balance
    monthly_payment = 0
    
    while ending_balance >= 0:
        monthly_payment += 10
        ending_balance = debt_payoff_calculation(balance, annualInterestRate, monthly_payment)
    
    return monthly_payment

fixed_montly_payment = find_monthly_payment(balance)
   
print(find_monthly_payment(3329, .2)

