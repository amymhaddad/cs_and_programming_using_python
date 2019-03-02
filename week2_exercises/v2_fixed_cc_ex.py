
def calculate_end_balance(balance, annualInterestRate, monthly_payment):
    month = 1
    while month <= 12:
        monthly_interest_rate = annualInterestRate / 12.0
        monthly_unpaid_balance = balance - monthly_payment
        new_balance = (monthly_unpaid_balance) + (monthly_interest_rate * monthly_unpaid_balance)

        balance = new_balance
        month += 1

    return balance

def monthly_payment(balance, annualInterestRate):
    monthly_payment = 0

    while True:
        monthly_payment += 10
        ending_balance = calculate_end_balance(balance, annualInterestRate, monthly_payment)
        if ending_balance <= 0:
            return monthly_payment

print(monthly_payment(320000, .2))
