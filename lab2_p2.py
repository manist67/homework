digits = ""
digits += input("Enter leftmost digit: ")
while len(digits) < 4:
    digits += input("Enter the next digit: ")

print("the value is {}".format(int(digits, 2)))
