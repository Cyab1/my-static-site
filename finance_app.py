# math function
import math

print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond - to calculate the amount you'll have to pay on a home loan")
# prompts the user to select an option from the above choices.
user_invest_type = input("Enter either 'investment' or 'bond' from menu above: ").lower()

# checks user selection and executes the function selected accordingly.
# investment calculation should user select 'investment'
if user_invest_type == 'investment':
    deposit_amount = float(input("Enter the amount you are depositing: "))
    interest_rate = float(input("Enter the interest rate in percentage: "))
    years = int(input("enter the number of years you want to invest: "))
    interest = input("Do you want 'simple' or 'compound' interest: ").lower()

    # Calculation of user selection based on interest selected.
    if interest == 'simple':
        r = interest_rate / 100
        total_amount = deposit_amount * (1 + r * years)
    elif interest == 'compound':
        r = interest_rate / 100
        total_amount = deposit_amount * math.pow((1 + r), years)
    else:
        print("Invalid option selected.please ensure you selected 'compound' or 'simple'.")
        exit()
    # Print the total amount after interest
    print(f"The total amount after {years} at {interest_rate}% interest will be be {total_amount}. ")            

# Calculation of 'bond' should user select bond  
elif user_invest_type == 'bond':
    current_amount = float(input("please enter present value of item: "))
    current_interest = float(input("please enter annual interest rate: "))
    months = int(input("please enter the number of months you will pay: "))
    
    # Calculation of the interest for the repayment time
    i = (current_interest / 100) / 12
    repayment = (i * current_amount) / (1 - math.pow((1 + i), - months))
    
    # print monthly repayment of the bond.
    print(f"the mounthly repayment will be {repayment}.")
else:
    print("please ensure you entered a valid input")
    exit()

   