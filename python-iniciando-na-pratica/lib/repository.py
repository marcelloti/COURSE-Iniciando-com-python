import os
import json
import lib.model as model

BASE_PATH = os.path.dirname(os.path.abspath(__file__))


def loadDatabaseData():
    model.accounts_list = loadDbData('accounts_list')
    model.money_slips = loadDbData('money_slips')


def writeDbData(data, file):
    with open(BASE_PATH + '/../db/' + file + '.json', 'w') as fp:
        json.dump(data, fp, indent=4)


def loadDbData(file):
    with open(BASE_PATH + '/../db/' + file + '.json', 'r') as fp:
        data = json.load(fp)
        return data
