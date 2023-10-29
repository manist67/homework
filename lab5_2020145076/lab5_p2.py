# check vowels
sentence = input("Enter a sentence: ").lower() 
# lower for check vowels

count = 0
count += sentence.count("a") # check a
count += sentence.count("e") # check e
count += sentence.count("i") # check i
count += sentence.count("o") # check o
count += sentence.count("u") # check u

if count == 1:
    print("Your sentence contains 1 vowel.")
else:
    print("Your sentence contains {} vowels.".format(count))
