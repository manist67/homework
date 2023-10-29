# author : Seung Min Lee
# since : 2023-03-25
# purpose : transfer UPC to EAN

EAN = input("Enter the first 12 digits of an EAN: ")

first_sum = 0
second_sum = 0

for i in range(0, len(EAN)):
    if i % 2 == 1: # the second, fourth, sixth, eighth, tenth, and twelfth digits
        first_sum += int(EAN[i])
        
    if i % 2 == 0: # the first, third, fifth, seventh, ninth, and eleventh digits.
        second_sum += int(EAN[i])

calculated_number = first_sum * 3 + second_sum - 1 # first_sum * 3 + second_sum - 1
check_digit = 9 - calculated_number % 10 # The remainder upon dividing by 10 then subtract 9.

print("Check digit: {}".format(check_digit)) # result
