while True:
    lec_num = input("Lecture number: ")
    if lec_num == "q":
        break
    lec_start = int(input("Lecture start: "))
    lec_credit = int(input("Lecture credit: "))

    print("{}: {:02d}:00~{:02d}:00"
          .format(lec_num, 8+lec_start, 8+lec_start+lec_credit))
