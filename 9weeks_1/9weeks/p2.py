lecture_num_1 = input("Lecture number of first lecture: ")
lecture_num_2 = input("Lecture number of second lecture: ")
lecture_day_1 = input("First lecture day: ")
lecture_day_2 = input("Second lecture day: ")
lecture_start_1 = int(input("First lecture start: "))
lecture_start_2 = int(input("Second lecture start: "))
lecture_cre_1 = int(input("First lecture credit: "))
lecture_cre_2 = int(input("Second lecture credit: "))

str_form = '{0: >9}{1: >4}{2: >6}{3: >4}{4: >7}{5: >6}'
print(str_form.format("LECTURE", "DAY", "START", "END", "CREDIT", "RATIO"))
print(str_form.format(lecture_num_1
                      , lecture_day_1
                      , lecture_start_1
                      , lecture_start_1 + lecture_cre_1 - 1
                      , lecture_cre_1
                      , "{:.2f}".format(
                          lecture_cre_1 / (lecture_cre_1 + lecture_cre_2))))

print(str_form.format(lecture_num_2
                      , lecture_day_2
                      , lecture_start_2
                      , lecture_start_2 + lecture_cre_2 - 1
                      , lecture_cre_2
                      , "{:.2f}".format(
                          lecture_cre_2 / (lecture_cre_1 + lecture_cre_2))))

