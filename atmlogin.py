atm = {'balance': 10000, 'transaction': [], 'n': 1}

def withdraw(atm):
    if atm['n']<=2:
        amount = float(input("Enter amount to be withdrawn:"))
        if amount <= atm['balance']:
            atm['n'] += 1
            atm['balance']-= amount
            print(f"Available balance: {atm['balance']}")
            atm['transaction'].append(f"Withdrawn: ${amount}")
        else:
            print("Insufficient funds")
    else:
        print("Transaction limit exceeded")

def balance(atm):
    return atm['balance']
choices = {'1': withdraw, '2': balance}
def acess():
    while True:
        print("1. Withdraw")
        print("2. Balance")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == '3':
            print("Exited successfully")
            break
        elif choice == '1':
            choices[choice](atm)
        elif choice == '2':
            print("Current balance:", choices[choice](atm))
        else:
            print("Invalid choice")

details={'email':{}}
email={"abcd":"1234","pqrs":"5678","xyz":"9087"}
user_email=input("enter email")
user_password=input("enter password")
if(user_email in email and email[user_email]==user_password):
    print("login succesfull")
    acess()
else:
    print("invalid credentials")