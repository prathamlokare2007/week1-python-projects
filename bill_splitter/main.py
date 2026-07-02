# Restaurant Bill Splitter
total_bill = float(input("Enter your total bill:"))
total_people = int(input("Enter total number of person:"))
tip_amount =float(input("enter amount of tip for waiter in %:"))

bill_with_tip = total_bill + (total_bill*tip_amount)/100
each_person_contro = (bill_with_tip)/total_people
tip = bill_with_tip - total_bill
print("each person contro must be:",each_person_contro)
print("THANKYOU for service  this is ur tip:",tip)
