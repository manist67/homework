lecture_list = ['YNB_4876', 'PLS_3824', 'YDT_4892', 'DXC_5781', 'NKT_3877', 'IBZ_8016', 'TPK_3513', 'HHZ_2871', 'KQP_1484', 'RKR_3989']

grades = [
    int(input("Enter the grade: ")),
    int(input("Enter the grade: "))
]
grades.sort()

min_grade = grades[0]
max_grade = grades[1]

for item in lecture_list:
    item_grade = int(item[4])
    if min_grade <= item_grade and item_grade <= max_grade:
        print(item)
