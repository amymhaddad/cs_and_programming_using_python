def debt_payoff(balance, annualInterestRate, monthlyPaymentRate):
    month = 1
    
    while month <= 12 :
        monthly_payment = balance * monthlyPaymentRate
        unpaid_balance = balance - monthly_payment
        interest_on_unpaid_balance = (annualInterestRate / 12.0) * unpaid_balance
        new_balance = unpaid_balance + interest_on_unpaid_balance

        month += 1
        balance = new_balance

    rounded_balance = round(balance, 2)
    final_output = "Remaining balance: " + str(rounded_balance)
    return final_output

