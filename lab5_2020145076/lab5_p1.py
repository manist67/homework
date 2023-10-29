# purpose: pick largest number

latest_num = -1
largest_number = 0

while latest_num != 0:
    # input number by float
    latest_num = float(input("Enter a number: "))
    
    # check negative number
    if latest_num < 0:
        print("No positive number was entered")
        continue
    
    # check largest number
    if latest_num > largest_number:
        largest_number = latest_num

# print the result
print("The largest number entered was {:.2f}".format(largest_number))
1