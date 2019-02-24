

def debt_payoff(balance, annualInterestRate):
    months = 12
    
    for mon in range(months):
        monthly_payment = balance // 12
        monthly_payment_multiple_of_ten = (monthly_payment // 10) * 10
        monthly_unpaid_balance = balance - monthly_payment_multiple_of_ten

        monthly_interest_rate = (annualInterestRate) / 12.0
        new_balance = monthly_unpaid_balance + (monthly_interest_rate * monthly_unpaid_balance)
        
        balance = new_balance 


    # rounded_balance = round(balance, 2)
    # final_output = "Remaining balance: " + str(rounded_balance)
    return balance 

print(debt_payoff(3329, 0.2))


# Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)
# Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)

