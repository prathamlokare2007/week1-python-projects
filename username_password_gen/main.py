#username_password_gen
name =input("Enter your name")                         #taking user name
day = input("Enter your birth day ")             # user  birth date
month = input("Enter your birth month")          # user birth month
year = input("Enter your birth year ")           # user birth year

username = name + "_" + year                      # simple pattern for username (u can chnage the poattern acc to u)
password = name[0:3] + day + month                # password pattern

print("username is:",username)                     # username  op 
print("password is:",password)                     # password op 
