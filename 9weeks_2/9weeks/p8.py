lecture_list = ['YNB_4876', 'PLS_3824', 'YDT_4892', 'DXC_5781', 'NKT_3877', 'IBZ_8016', 'TPK_3513', 'HHZ_2871', 'KQP_1484', 'RKR_3989']
lecture_dict = {'YNB_4876': 'A', 'PLS_3824': 'A', 'YDT_4892': 'B', 'DXC_5781': 'C', 'NKT_3877': 'F', 'IBZ_8016': 'A', 'TPK_3513': 'B', 'HHZ_2871': 'C', 'KQP_1484': 'D', 'RKR_3989': 'A'}

grades = []

while True:
    grade = input("Enter the grade: ")
    if grade == "q":
        break
    grades.append(grade)

for item in lecture_list:
    for grade in grades:
        if lecture_dict[item] == grade:
            print("{}: {}".format(item, lecture_dict[item]))
