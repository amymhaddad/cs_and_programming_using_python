
month = 1
balance = 5000
annual_interest_rate = .18
minimum_monthly_payment_rate = .02

while month <= 12 :
    monthly_payment = balance * minimum_monthly_payment_rate
    unpaid_balance = balance - monthly_payment
    interest_on_unpaid_balance = (annual_interest_rate / 12.0) * unpaid_balance
    new_balance = unpaid_balance + interest_on_unpaid_balance    

    month += 1
    balance = new_balance


balance = 4691.107871735441
print(round(balance, 2))
    

