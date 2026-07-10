# Bank Account System
name=input("enter yor name")            
start_balance=int(input("enter your current balance"))       
print("what do you want to do")     
print("1. Deposit money")
print("2. Withdraw money")
print("3. Check balance")
choice=int(input("enter  the number (1/2/3):"))

if choice==1:
  deposit_amoumt=int(input("enter your amount to deposit"))
  start_balance=start_balance +   deposit_amoumt
  print("amount has been succesfully deposited")
  print("your new bank balance is:", start_balance)

if choice==2:
   with_draw= int(input("enter amount to withdraw"))
  if(with_draw>start_balance):
    print("Insufficient balance")
else:
    start_balance= start_balance-with_draw
    print("amount after withdrwal is:",start_balance)

if choice == 3:
