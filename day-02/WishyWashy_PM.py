
import random


# 1. Generate random machine usage time
def generate_minutes():
    minutes = random.randint(30, 180)
    return minutes


# 2. Calculate amount before VAT
def calc_amount(machine_type, minutes):

    hours = minutes / 60

    if machine_type == "A":
        initial_cost = 50.00
        hourly_rate = 30.00

    elif machine_type == "B":
        initial_cost = 62.50
        hourly_rate = 36.25

    elif machine_type == "C":
        initial_cost = 74.87
        hourly_rate = 40.50

    amount = initial_cost + (hourly_rate * hours)

    return amount


# 3. Calculate VAT and total payable
def calc_total_amount(amount):

    vat = amount * 0.14
    total_payable = amount + vat

    return vat, total_payable


# 4. Display daily payment summary
def display_summary(payments):

    number_customers = len(payments)

    total_payments = sum(payments)

    average_payment = total_payments / number_customers

    highest_payment = max(payments)

    lowest_payment = min(payments)

    print("\n========== DAILY SUMMARY ==========")

    print("Customers processed:", number_customers)

    print(f"Combined payments: R{total_payments:.2f}")

    print(f"Average payment: R{average_payment:.2f}")

    print(f"Highest payment: R{highest_payment:.2f}")

    print(f"Lowest payment: R{lowest_payment:.2f}")

    print("===================================")


# 5. Process customer payments
def process_payments():

    payments = []

    number_customers = int(input("Enter number of customers: "))

    for count in range(number_customers):

        print("\n========== CUSTOMER", count + 1, "==========")

        customer_name = input("Enter customer name: ")

        machine_type = input("Enter machine type (A/B/C): ").upper()

        minutes = generate_minutes()

        amount = calc_amount(machine_type, minutes)

        vat, total_payable = calc_total_amount(amount)

        payments.append(total_payable)

        print("\n------------- INVOICE -------------")

        print("Customer name:", customer_name)

        print("Machine type:", machine_type)

        print("Minutes used:", minutes)

        print(f"Amount before VAT: R{amount:.2f}")

        print(f"VAT amount: R{vat:.2f}")

        print(f"Total payable: R{total_payable:.2f}")

        print("-----------------------------------")

    display_summary(payments)


# Start the program
process_payments()
