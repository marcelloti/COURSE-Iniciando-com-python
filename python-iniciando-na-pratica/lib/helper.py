import os


def printComment(comment):
    commentLenght = len(comment)

    print("\n")
    print(("-"*commentLenght)+("-")*10)
    print("    # " + comment)
    print(("-"*commentLenght)+("-")*10)


def clearTerminal():
    clear = 'cls' if os.name == 'nt' else 'clear'
    os.system(clear)


def pauseUntilEnter():
    input('Press <ENTER> to continue...')
    clearTerminal()
