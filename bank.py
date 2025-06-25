def createAccount(name, balance,accts): 
    accts[name]= balance
def closeAccount(name, accts): 
    if name in accts.keys(): 
        accts.pop(name)
    else: 
        print("That is not a valid account meme")
def withdraw(name, amount, accts): 
    if name in accts.keys(): 
        if amount > accts[name]: 
            print("amount exceeds account balance")
            return False
        else: 
            accts[name]= accts[name] - amount
            return True
    else: 
        print("That is not a valid account meme")   
        return False 
def deposit(name, amount, accts): 
    if name in accts.keys(): 
        accts[name]= accts[name] + amount
    else: 
        print("That is not a valid account meme")   
def transfer(acct1, acct2, amount, accts): 

    if acct1 in accts.keys() and acct2 in accts.keys(): 
        if withdraw(acct1, amount, accts) == True:
            deposit(acct2, amount, accts)
    else: 
        print("One of those accounts is not a valid account")
        print("Accounts not updated")

def printAccounts(accts): 
    print("----Accounts----")
    for name in accts: 
        print(f"Account name: {name} Balance: {accts[name]}")


def main(): 
    accounts= {"John Pork": 500}
    check = True 
    while check == True: 
        print("Welcome to the bank!")
        print("1. Create account")
        print("2. Close Account")
        print("3. Withdraw")
        print("4. Deposit")
        print("5. Transfer")
        print("6. Quit")
        option= (input("Enter your option from the list above: "))
        if option.isnumeric() == True: 
            if int(option) == 1: 
                printAccounts(accounts)
                acctname= input("Enter the name of your account: ").strip()
                balance= float(input("Enter your balance: "))
                createAccount(acctname, balance, accounts)
                printAccounts(accounts)
            elif int(option) == 2: 
                printAccounts(accounts)
                acctname= input("Enter the name of account you wish to close: ").strip()
                closeAccount(acctname, accounts)
                printAccounts(accounts)
            elif int(option) == 3: 
                printAccounts(accounts)
                acctname= input("Enter the account name you would wish to withdraw from: ").strip()
                amt= float(input("Enter the amount you would like to withdraw: "))
                withdraw(acctname, amt, accounts)
                printAccounts(accounts)
            elif int(option) == 4: 
                printAccounts(accounts)
                acctname= input("Enter the account name you would like to deposit to: ").strip()
                amt = float(input("Enter the amount you wish to deposit: "))
                deposit(acctname, amt, accounts)
                printAccounts(accounts)
            elif int(option) == 5: 
                printAccounts(accounts)
                acct1= input("Enter the account name you would like to transfer from: ").strip()
                acct2= input("Enter the account name you would like to transfer to: ").strip()
                amt= float(input("Enter the amount you would like to transfer: "))
                transfer(acct1, acct2, amt, accounts)
                printAccounts(accounts)
            elif int(option) == 6: 
                print("Thanks for visiting!")
                check = False
        else: 
            print("Invalid input")

main()