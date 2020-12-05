from helper import printComment

printComment("Math operations")
print(1)

printComment("Print 1")
x = 1
print(x)

printComment("Print 4")
print(x + 3)

printComment("Print 4")
print(2 * 2)

printComment("Print 5.0")
print(2 * 2.5)

printComment("Print 2.0 (division will always print a float)")
print(10 / 5)

printComment("Print 2 ('//' means 'print an int')")
print(10 // 5)

printComment("Print 5.5")
print(11 / 2)

printComment("Print 1 (the remainder of the operation)")
print(11 % 2)

printComment("Returns 8 ('**' means 2 power of 3)")
print(2 ** 3)

printComment("Breakline")
print("Hello\nWorld!")

printComment("Escape all string characters")
print(r"C:\number")

printComment("Concat string")
print("Marcello" + " " + "Costa")

printComment("Multiply an string")
print("Marcello Costa "*2)

printComment("Substring (slices)")
name = "Marcello Costa"
print(name[0:8])
print(name[:8])
print(name[9:])

printComment("Lists")
numbers = [0, 2, 4, 6, 8]
print(numbers)

printComment("Concat lists")
numbers2 = [10, 12, 14, 16, 18]

print(numbers + numbers2)

printComment("Slice list")
print(numbers[0:3])

printComment("Mix of types")
mix = [1, 4, "5", 6.3, [1, 3, 7]]
print(mix)

printComment("Print item of list inside list")
print(mix[4][2])

printComment("Adding item to the list")
numbers.append(12)
print(numbers)

printComment("Removing an item (the first occurrence of 8)")
numbers.remove(8)
print(numbers)

printComment("Removing an item by index")
del(numbers[1])
print(numbers)
