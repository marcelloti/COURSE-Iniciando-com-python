from helper import printComment


def call_numbers():
    for number in range(0, 10):
        print(number)


def call_numbers_with_limit(limit):
    for number in range(limit):
        print(number)


def calculator(x=2, y=1):
    return x/y


printComment("call_numbers function")
call_numbers()

printComment("call_numbers_with_limit function")
call_numbers_with_limit(5)


printComment("calculator function")
print(calculator(10, 5))

printComment("calculator function with parameters order")
print(calculator(y=10, x=5))

printComment("calculator function without parameters (default values)")
print(calculator())

printComment("calculator function to variable")
result = calculator(8, 8)
print("Result is:", result)
