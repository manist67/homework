lec_num = input("Lecture number: ")
lec_start = int(input("Lecture start: "))
lec_credit = int(input("Lecture credit: "))

print("{}: {:02d}:00~{:02d}:00"
      .format(lec_num, 8+lec_start, 8+lec_start+lec_credit))
