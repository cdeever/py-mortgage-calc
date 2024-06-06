from datetime import datetime
from dateutil.relativedelta import relativedelta

def mortgage_amortization(principal, interest_rate, term, extra_payment=1, start_date=None):
    # calculate the monthly interest rate
    monthly_rate = interest_rate / 12
    # calculate the number of payments
    num_payments = term * 12
    # calculate the monthly payment without extra_payment
    monthly_payment = (principal * monthly_rate) / (1 - (1 + monthly_rate)**(-num_payments))
    # initialize variables for total interest paid,remaining balance and savings
    total_interest_paid = 0
    total_interest_paid_without_extra = 0
    remaining_balance = principal
    remaining_balance_without_extra = principal
    total_principal_paid = 0;
    total_savings = 0
    i = 0
    principal_paid = 0
    savings = 0
    total_savings = 0
    interest = remaining_balance * monthly_rate

    if start_date:
        payment_date = datetime.strptime(start_date, "%Y-%m")

    # print the table header
    print("Month\tPayment\tInterest\tPrincipal\tTotal Interest\tRemaining Balance\tSavings\tTotal Savings")
    print(f"{i}\t{monthly_payment + extra_payment:.2f}\t{interest:.2f}\t{principal_paid:.2f}{total_principal_paid:.2f}\t{total_interest_paid:.2f}\t{remaining_balance:.2f}\t{savings:.2f}\t{total_savings:.2f}")    
   
    # loop through the number of payments
    for i in range(1, num_payments + 1):

        if remaining_balance >= 0:
            # calculate the interest for this month
            interest = remaining_balance * monthly_rate
            principal_paid = monthly_payment + extra_payment - interest
        else:
            interest = 0
            principal_paid = 0

        interest_without_extra = remaining_balance_without_extra * monthly_rate
        # calculate the principal for this month

        principal_paid_without_extra = monthly_payment - interest_without_extra
        # calculate the savings from the extra payment
        savings = interest_without_extra - interest
        total_savings += savings
        # update the remaining balance
        remaining_balance -= principal_paid
        remaining_balance_without_extra -= principal_paid_without_extra
        # update the total interest paid
        total_interest_paid += interest
        total_interest_paid_without_extra += interest_without_extra
        total_principal_paid += principal_paid

        if start_date:

        else:



# print the current month's information
        print(f"{i}\t{monthly_payment + extra_payment:.2f}\t{interest:.2f}\t{principal_paid:.2f}{total_principal_paid:.2f}\t{total_interest_paid:.2f}\t{remaining_balance:.2f}\t{savings:.2f}\t{total_savings:.2f}")
    print(f"Total savings: {total_savings:.2f}")


# test the function
mortgage_amortization(171500, 0.0274, 15, 500, "2020-12")
