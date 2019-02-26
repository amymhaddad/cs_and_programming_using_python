

#monthly_payment is not passed into this function
def calculate_ending_balance(balance, annualInterestRate, monthly_payment):

    month = 1
    while month <= 12:
        unpaid_balance = balance - monthly_payment
        monthly_interest_rate = annualInterestRate / 12.0
        new_balance = unpaid_balance + (monthly_interest_rate * unpaid_balance)

        month += 1
        balance = new_balance

    ending_balance = round(balance, 2)
    final_output = "Remaining balance: " + str(ending_balance)
    return ending_balance


def debt_payoff(balance, annualInterestRate):

    ending_balance = balance
    monthly_payment = 0

    while ending_balance > 0:
        #calling the lower-level function inside this higher-level function in order find the total ending balance after 12 months.  
        #The order of incrementing the monthly payment and calling ending balance matter!
        #The way it is now, I increment the monthly payment, THEN call the function. Otherwise I call the function, which could get me the result I need, then I add 10 to it
        monthly_payment += 10 
        ending_balance = calculate_ending_balance(balance, annualInterestRate, monthly_payment)

    return monthly_payment

monthly_payment = debt_payoff(3329, .2)
print(monthly_payment)
