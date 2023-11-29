# One Stop Insurance Company
# Colby Ash
# Thu Nov 23

import datetime

# Default values
next_policy_number = 1944
basic_premium = 869.00
discount_for_additional_cars = 0.25
cost_extra_liability_coverage = 130.00
cost_glass_coverage = 86.00
cost_loaner_car_coverage = 58.00
hst_rate = 0.15
processing_fee_monthly = 39.99

# FormatValues library
def format_values(value):
    # Add your custom formatting here
    return value

# Function to get customer information
def get_customer_info():
    first_name = input("Enter first name: ").title()
    last_name = input("Enter last name: ").title()
    address = input("Enter address: ")
    city = input("Enter city: ").title()
    provinces = ["ON", "QC", "BC", "AB", "MB", "SK", "NS", "NB", "NL", "PE", "NT", "NU", "YT"]
    province = input("Enter province (valid options: {}): ".format(", ".join(provinces))).upper()
    while province not in provinces:
        province = input("Invalid province. Enter a valid province: ").upper()
    postal_code = input("Enter postal code: ")
    phone_number = input("Enter phone number: ")

    cars_insured = int(input("Enter the number of cars being insured: "))
    extra_liability = input("Extra liability coverage (Y or N): ").upper()
    glass_coverage = input("Glass coverage (Y or N): ").upper()
    loaner_car_coverage = input("Loaner car coverage (Y or N): ").upper()
    payment_method = input("Payment method (Full, Monthly, or Down Pay): ").title()

    if payment_method == "Down Pay":
        down_payment = float(input("Enter the amount of the down payment: "))
    else:
        down_payment = 0.0

    return (
        first_name, last_name, address, city, province, postal_code, phone_number,
        cars_insured, extra_liability, glass_coverage, loaner_car_coverage,
        payment_method, down_payment
    )

# Function to calculate insurance premium
def calculate_premium(cars_insured, down_payment):
    total_extra_costs = cars_insured * (
        cost_extra_liability_coverage +
        cost_glass_coverage +
        cost_loaner_car_coverage
    )

    total_premium = basic_premium + (cars_insured - 1) * basic_premium * discount_for_additional_cars
    total_premium += total_extra_costs

    hst = total_premium * hst_rate
    total_cost = total_premium + hst

    if down_payment > 0:
        total_cost -= down_payment

    monthly_payment = (total_cost + processing_fee_monthly) / 8

    return total_premium, hst, total_cost, monthly_payment

# Function to display receipt
def display_receipt(customer_info, premium_info, claims):
    print("\n-------- Receipt --------")
    print("Policy Number:", next_policy_number)
    print("Date:", datetime.datetime.now().strftime("%Y-%m-%d"))

    print("\nCustomer Information:")
    print("Name:", customer_info[0], customer_info[1])
    print("Address:", customer_info[2])
    print("City:", customer_info[3])
    print("Province:", customer_info[4])
    print("Postal Code:", customer_info[5])
    print("Phone Number:", customer_info[6])

    print("\nInsurance Information:")
    print("Number of Cars Insured:", customer_info[7])
    print("Extra Liability Coverage:", customer_info[8])
    print("Glass Coverage:", customer_info[9])
    print("Loaner Car Coverage:", customer_info[10])
    print("Payment Method:", customer_info[11])

    print("\nPremium Information:")
    print("Total Premium:", format_values(premium_info[0]))
    print("HST:", format_values(premium_info[1]))
    print("Total Cost:", format_values(premium_info[2]))
    print("Monthly Payment:", format_values(premium_info[3]))

    print("\nPrevious Claims:")
    print("  Claim #  Claim Date        Amount")
    print("  ---------------------------------")
    for i, claim in enumerate(claims, start=1):
        print(f"{i}. {claim['date']} ${claim['amount']:.2f}")

# Main program
customer_info = get_customer_info()
premium_info = calculate_premium(customer_info[7], customer_info[12] if customer_info[11] == "Down Pay" else 0)
claims = [
    {"date": "2022-01-15", "amount": 500.00},
    {"date": "2022-05-20", "amount": 750.00},
    {"date": "2022-09-10", "amount": 1200.00},
]

display_receipt(customer_info, premium_info, claims)