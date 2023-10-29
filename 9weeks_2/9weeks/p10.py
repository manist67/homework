time_string = input("Enter the time: ")

hour, minu = int(time_string[0:2]), int(time_string[3:5])

for i in range(0, 5):
    degree = hour * 30 + minu * 0.5 - minu * 6
    if degree > 180:
        degree = 360 - degree
    elif degree < 0:
        degree *= -1

    print("{:02d}:{:02d} makes {:.02f} degree".format(hour, minu, degree))
    minu += 15
    if minu >= 60:
        hour += 1
        if hour > 12:
            hour -= 12
        minu -= 60
