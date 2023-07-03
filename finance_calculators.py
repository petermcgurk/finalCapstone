import math

print("investment\t - to calculate the amount of interest you'll earn on your investment")
print("bond\t\t - to calculate the amount you'll have to pay on a home loan\n")

product_type = input("Enter either 'investment' or 'bond' from the menu above to proceed:\n").lower()
# This ensures that the inputted variable is not affected by differences in case

if product_type == "investment":
    print("\nYou entered 'investment'\n")
    
    deposit_amount = int(input("Enter the amount of money in GBP you wish to deposit, e.g. 50:\n"))
    print(f"\nYou entered GBP {deposit_amount:.2f}")  
    # This is to display as a currency amount, I got this from https://java2blog.com/format-a-float-to-two-decimal-places/
   
    interest_rate = int(input("\nEnter the percent of yearly interest you would like, leaving out the '%' sign, e.g. type '5' for '5%':\n"))
    print(f"\nYou entered an interest rate of {interest_rate}%\n")
    interest_rate = (interest_rate / 100)
   
    number_of_years = int(input("Enter number of years you are planning on investing:\n"))
    print(f"You entered {number_of_years} years\n")
   
    interest = input('Would you like "simple" or "compound" interest?\n').lower()
    print(f"\nYou entered '{interest}'\n")

    if interest == "simple":
        total = (deposit_amount*(1 + interest_rate*number_of_years))
        print(f"Your total amount with interest will be GBP {total:.2f}. Thank you.")

    elif interest == "compound":
        total = (deposit_amount * math.pow((1+interest_rate),number_of_years))
        print(f"Your total amount with interest will be GBP {total:.2f}.")

    else:
        print("Error")

elif product_type == "bond":
    print(f"\nYou entered '{product_type}'\n")

    value_of_house = int(input("Enter the value of your house in GBP:\n"))
    print(f"You entered the value of your house as GBP {value_of_house:.2f}\n")

    interest_rate = int(input("Enter yearly interest rate without '%' sign:\n"))
    print(f"You entered {interest_rate}% yearly interest\n")
    interest_rate = interest_rate / 100
    monthly_interest_rate = interest_rate / 12

    repayment_months = int(input("Enter the number of months you plan to repay the bond, e.g. 120:\n"))
    print(f"\nYou entered {repayment_months} months for repayment\n")

    repayment = (interest_rate * value_of_house)/(1 - (1 + monthly_interest_rate)**(-repayment_months))
    print(f"Your total payment including interest will be GBP {repayment:.2f}.")

else:
    print("\nInput not recognised. You should enter either 'investment' or 'bond'")