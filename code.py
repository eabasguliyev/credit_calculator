import sys
import argparse
from math import log

def abs_value(value):
    if value - int(value) == 0:
        return int(value)
    else:
        return int(value + 1)

def calculate_diff(principal, n, interest):
    i = interest / (12 * 100)
    monthly_payment = []
    total_payment = 0
    for j in range(1, n + 1):
        D = principal / n + i * (principal - (principal * (j - 1)) / n)
        
        monthly_payment.append(abs_value(D))
    
    for j in range(n):
        print("Month {}: paid out {}".format(j + 1, monthly_payment[j]))
        total_payment += monthly_payment[j]
    
    overpayment = abs_value(total_payment - principal)

    print("\nOverpayment = " + str(overpayment))

def annuity_payment(principal, n, interest):
    i = interest / (12 * 100)
    annuity_payment = (principal * i * pow(1 + i, n) / (pow(1 + i, n) - 1))

    if annuity_payment - round(annuity_payment) == 0:
        return annuity_payment
    else:
        return round(annuity_payment + 1)

def credit_principal(payment, count_of_periods, interest):
    i = interest / (12 * 100)
    credit_principal = payment / ((i * pow(i + 1, count_of_periods)) / (pow(i + 1, count_of_periods) - 1))
    return credit_principal

def count_of_periods(principal, payment, interest):
    i = interest / (12 * 100)
    n = log(payment / (payment - (i * principal)), i + 1)
    return round(n)

def print_date(n):
    print(n)
    years = n // 12
    months = n % 12

    if years == 0:
        if months == 1:
            print("{} month to repay this credit!".format(months))
        else:
            print("{} months to repay this credit!".format(months))
    elif months == 0:
        if years == 1:
            print("{} year to repay this credit!".format(years))
        else:
            print("{} years to repay this credit!".format(years))
    else:
        if months == 1 and years == 1:
            print("{} year and {} month to repay this credit!".format(years, months))
        elif months == 1:
            print("{} years and {} month to repay this credit!".format(years, months))
        elif years == 1:
            print("{} year and {} months to repay this credit!".format(years, months))
        else:
            print("{} years and {} months to repay this credit!".format(years, months))

def incorrect_message():
    print("Incorrect parameters.")
    exit()


parser = argparse.ArgumentParser()
parser.add_argument('--type', type=str)
parser.add_argument('--principal', type=int)
parser.add_argument('--payment', type = int)
parser.add_argument('--periods', type=int)
parser.add_argument('--interest', type=float)

args = parser.parse_args()

if(len(sys.argv) != 5):
    incorrect_message()

if args.type == "diff":
    if args.principal and args.periods and args.interest:
        calculate_diff(args.principal, args.periods, args.interest)
    else:
        incorrect_message()     
elif args.type == "annuity":
    if not args.interest:
        incorrect_message()
        
    if args.principal and args.periods:
        annuity_payment = annuity_payment(args.principal, args.periods, args.interest)
        overpayment = abs_value(annuity_payment * args.periods - args.principal)

        print("Your annuity payment = %i!" % annuity_payment)
        print("Overpayment = " + str(overpayment))
    elif args.payment and args.periods:
        credit_principal = credit_principal(args.payment, args.periods, args.interest)

        overpayment = abs_value(args.payment * args.periods - credit_principal)

        print("Your credit principal = %i!" % credit_principal)
        print("Overpayment = " + str(overpayment))

    elif args.principal and args.payment:

        n = count_of_periods(args.principal, args.payment, args.interest)
        overpayment = args.payment * n - args.principal

        print_date(n)

        print("Overpayment = %i" % overpayment)
    else:
        incorrect_message()
else:
    incorrect_message()
