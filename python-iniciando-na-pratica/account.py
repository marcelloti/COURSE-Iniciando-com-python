from lib.helper import printComment
from lib.helper import clearTerminal
from lib.helper import pauseUntilEnter
import lib.model as model
import lib.repository as repository


def pressEnterToBackToOperationsMenu():
    pauseUntilEnter()
    accountOperations()


def showBalance():
    balance = model.currentAccount['balance']
    # print("\nYour balance is: %s" % str(balance) + "\n")
    print("\nYour balance is: " + str(balance) + "\n")
    pressEnterToBackToOperationsMenu()


def canAmountBeWithdrawWithCellType(amount, cellType):
    return (amount // int(cellType)) > 0


def ATMHaveEnoughOfThisCellTypes(amount, cellType):
    return ((amount // int(cellType) <= model.money_slips[cellType]))


def setCellsToWithdraw(amount):
    for cellType in model.money_slips:
        if (amount == 0):
            break
        if (amount > 0 and canAmountBeWithdrawWithCellType(amount, cellType)):
            if (ATMHaveEnoughOfThisCellTypes(amount, cellType)):
                model.money_slips_user[cellType] = amount // int(cellType)
                amount = (amount - amount // int(cellType) * int(cellType))

    if (amount > 0):
        print('The ATM does not have money cells available for this amount')
        pauseUntilEnter()
        accountOperations()


def removeAmountFromAccountAndATMDatabase(amount):
    repository.writeDbData(model.money_slips, 'money_slips')

    for index, account in enumerate(model.accounts_list):
        if model.currentAccount['agency'] == account['agency']:
            if (model.accounts_list[index]['balance'] >= int(amount)):
                model.accounts_list[index]['balance'] = int(
                    model.accounts_list[index]['balance']) - int(amount)
                repository.writeDbData(model.accounts_list, 'accounts_list')
            else:
                print("\nInsufficient funds\n")
                pressEnterToBackToOperationsMenu()

            break


def withdraw():
    amount = input('Enter the amount to be withdrawn: ')

    setCellsToWithdraw(int(amount))

    for moneyCellType in model.money_slips_user:
        model.money_slips[moneyCellType] -= model.money_slips_user[
            moneyCellType]

    removeAmountFromAccountAndATMDatabase(amount)

    print('Take the money:')
    print(model.money_slips_user)
    pauseUntilEnter()
    model.money_slips_user = {}
    accountOperations()


def restockATM():
    amount_typed = input('Enter the number of money cells: ')
    money_bill_typed = input('Enter the money cell to be included: ')
    if (money_bill_typed not in model.money_slips):
        print("\nInvalid money cell\n")
        pressEnterToBackToOperationsMenu()

    model.money_slips[money_bill_typed] += int(amount_typed)
    repository.writeDbData(model.money_slips, "money_slips")
    print("ATM restocked:")
    print(model.money_slips)
    pressEnterToBackToOperationsMenu()


def accountOperations():
    clearTerminal()
    printComment("Account: " + model.currentAccount['agency'] +
                 " | Account operations:")
    print("1- Balance")
    print("2- Withdraw")
    print("3- Exit")
    if model.currentAccount['admin']:
        print("10 - Restock money cells")

    option_typed = input("\nType the option: ")

    if option_typed == '1':
        showBalance()

    elif option_typed == '2':
        withdraw()

    elif option_typed == '3':
        printComment("Thank you for using our services")
        exit()

    elif option_typed == '10' and model.currentAccount['admin']:
        restockATM()
        pressEnterToBackToOperationsMenu()

    else:
        print("\nInvalid option number\n")
        pressEnterToBackToOperationsMenu()
