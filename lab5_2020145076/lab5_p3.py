# store integer in list

input_list = []

while True:
    integer_input = int(input("Enter an integer: "))
    
    if integer_input == 0: 
        break # if input is 0, break the loop.
    
    # append by conditions
    if integer_input > 100:
        input_list.append('over')
    elif integer_input < -100:
        input_list.append('under')
    else:
        input_list.append(integer_input)

print(input_list)
