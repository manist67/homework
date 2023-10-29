# draw a triangle n * 2n-1
n = int(input("Enter an integer: "))
i = 0

while i < n:
    j = 0

    # print blanks
    while j < i:
        print(" ", end="")
        j+=1
    
    # nested loop to draw widths
    while (j+i) < (2 * n - 1):
        print("*", end="")
        j+=1

    # print new line
    print("")
    i+=1
