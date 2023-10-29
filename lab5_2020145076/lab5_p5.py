# purpose : count letter 'a'
names = []

# run the loop until input is q
while True:
    input_name = input("Enter a name (q to quit): ")

    if input_name == 'q':
        break

    names.append(input_name)

# count a in name list
count_a = 0
for name in names:
    # check a and captial A
    count_a += name.lower().count("a")

print("Appearance of letter 'a': {}".format(count_a))
