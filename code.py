import sys
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

if(len(sys.argv) != 5):
    print("Incorrect parameters.")
    exit()
else:
    parameter1_string = sys.argv[1]

    if "--type=" in parameter1_string:
        parameter1 = parameter1_string.replace("--type=", '')
        if parameter1 == "diff":
            parameter2_string = sys.argv[2]
            parameter3_string = sys.argv[3]
            parameter4_string = sys.argv[4]

            if "--principal=" in parameter2_string and "--periods=" in parameter3_string and "--interest=" in parameter4_string:
                parameter2 = int(parameter2_string.replace("--principal=", ''))
                parameter3 = int(parameter3_string.replace("--periods=", ''))
                parameter4 = float(parameter4_string.replace("--interest=", ''))

                calculate_diff(parameter2, parameter3, parameter4)
            else:
                print("Incorrect parameters.")
                exit()       
        elif parameter1 == "annuity":
            parameter2_string = sys.argv[2]
            parameter3_string = sys.argv[3]
            parameter4_string = sys.argv[4]

            if "--interest=" in parameter4_string:
                parameter4 = float(parameter4_string.replace("--interest=", ''))
            else:
                print("Incorrect parameters.")
                exit()

            if "--principal=" in parameter2_string and "--periods=" in parameter3_string:
                parameter2 = int(parameter2_string.replace("--principal=", ''))
                parameter3 = int(parameter3_string.replace("--periods=", ''))

                annuity_payment = annuity_payment(parameter2, parameter3, parameter4)
                overpayment = abs_value(annuity_payment * parameter3 - parameter2)

                print("Your annuity payment = %i!" % annuity_payment)
                print("Overpayment = " + str(overpayment))
            elif "--payment=" in parameter2_string and "--periods=" in parameter3_string:
                parameter2 = int(parameter2_string.replace("--payment=", ''))
                parameter3 = int(parameter3_string.replace("--periods=", ''))

                credit_principal = credit_principal(parameter2, parameter3, parameter4)

                overpayment = abs_value(parameter2 * parameter3 - credit_principal)

                print("Your credit principal = %i!" % credit_principal)
                print("Overpayment = " + str(overpayment))

            elif "--principal=" in parameter2_string and "--payment=" in parameter3_string:
                parameter2 = int(parameter2_string.replace("--principal=", ''))
                parameter3 = int(parameter3_string.replace("--payment=", ''))

                n = count_of_periods(parameter2, parameter3, parameter4)
                overpayment = parameter3 * n - parameter2

                print_date(n)

                print("Overpayment = %i" % overpayment)
            else:
                print("Incorrect parameters.")
                exit()
    else:
        print("Incorrect parameters.")
        exit()
