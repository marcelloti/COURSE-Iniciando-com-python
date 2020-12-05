import getpass
import sys

from helper import printComment

printComment("School of net - ATM Example")

account_typed = input("Type your agency number: ")
password_typed = getpass.getpass("Type your account password: ")

account_list = [
    {
        "agency": "0001-01",
        "password": "123456",
        "name": "John Doe",
        "balance": 1803.83
    },
    {
        "agency": "0002-02",
        "password": "123456",
        "name": "Jane Doe",
        "balance": 78.24
    }
]

validAccount = False
currentAccount = {}
for account in account_list:
    if account_typed == account['agency'] and password_typed == account['password']:
        validAccount = True
        currentAccount = account

if not validAccount:
    sys.exit("\nInvalid account\n")

printComment("Account options:")
print("1- Balance")
option_typed = input("\nType the option: ")

if option_typed == '1':
    balance = currentAccount['balance']
    # print("\nYour balance is: %s" % str(balance) + "\n")
    print("\nYour balance is: " + str(balance) + "\n")

else:
    sys.exit("\nInvalid option number\n")
