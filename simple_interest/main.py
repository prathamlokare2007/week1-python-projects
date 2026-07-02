# Simple Interest Calculator
principle=float(input("Enter principle amount"))                           # take principle amount from user
year=float(input("Enter for how many years or time in years "))            #for how many year do u want to keeep money
rate_of_intrest=float(input("Enter rate of intrest in %"))                 # rate of intrest anuually

simple_intrest=(principle*year*rate_of_intrest)/100                        #formula to calc what will be the intrest amount
total_amount=simple_intrest+principle                                      #total amount to repay u with intrest  

print("total intrest on principle amount:",simple_intrest)                 # op  of what is ur intrest amount
print("total amount:",total_amount)                                        #total amount u get
