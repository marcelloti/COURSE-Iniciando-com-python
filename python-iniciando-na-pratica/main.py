import lib.repository as repository
import lib.model as model
from lib.helper import printComment
from account import accountOperations
from auth import login

printComment("School of net - ATM Example")
repository.loadDatabaseData()

model.currentAccount = login()

accountOperations()
