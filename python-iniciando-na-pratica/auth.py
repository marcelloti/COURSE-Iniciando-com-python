import getpass
import sys
import lib.model as model


def login():
    account_agency = input("Type your agency number: ")
    password_typed = getpass.getpass("Type your account password: ")

    validAccount = False
    currentAccount = {}
    for account in model.accounts_list:
        if account_agency == account['agency'] and password_typed == account['password']:
            validAccount = True
            currentAccount = account

    if not validAccount:
        sys.exit("\nInvalid account\n")

    return currentAccount
