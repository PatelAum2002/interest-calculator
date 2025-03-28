import math  

def calculate_simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

def calculate_compound_interest(principal, rate, time):
    return principal * (math.pow((1 + rate / 100), time)) - principal

def interest_calculator():
    while True:
        print("\nInterest Calculator")
        principal = float(input("Enter principal amount: "))
        rate = float(input("Enter annual interest rate (%): "))
        time = int(input("Enter time in years: "))

        print("Choose Interest Type:")
        print("1. Simple Interest")
        print("2. Compound Interest")
        choice = input("Enter 1 or 2: ")

        if choice == '1':
            interest = calculate_simple_interest(principal, rate, time)
            print(f"Simple Interest: ${interest:.2f}")
        elif choice == '2':
            interest = calculate_compound_interest(principal, rate, time)
            print(f"Compound Interest: ${interest:.2f}")
        else:
            print("Invalid choice. Please enter 1 or 2.")
            continue

        another = input("Do you want to calculate again? (yes/no): ").lower()
        if another != 'yes':
            print("Thank you for using the Interest Calculator!")
            break


interest_calculator()
