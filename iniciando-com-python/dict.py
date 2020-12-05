from helper import printComment

cars = {}
cars['corola'] = "red"
cars['fit'] = "green"
cars['320'] = "black"

printComment("Dictionary keys")
print(cars.keys())

printComment("Dictionary values")
print(cars.values())

printComment("Print one value")
print(cars['corola'])

printComment("Type 1 of register an Dictionary")
people = dict(John='Father', Sarah='Mother', Maria='Baby')
print(people)

if ("John" in people):
    print(people['John'])

printComment("Type 2 of register an Dictionary")
people2 = {
    'John': 'Father',
    'Sarah': 'Mother',
    'Maria': 'Baby'
}
print(people2)

printComment("Iterate Dictionary items")
for key, value in people2.items():
    print(key + " = " + value)
