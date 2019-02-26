


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
    monthly_payment = 0
    ending_balance = balance

    while ending_balance >= 0:
        monthly_payment += 10
        ending_balance = calculate_end_balance(balance, annualInterestRate, monthly_payment)
    
    return monthly_payment

payment =  monthly_payment(3329, 0.2)
print(payment)
