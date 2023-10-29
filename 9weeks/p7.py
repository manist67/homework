lecture_list = ['YNB_4876', 'PLS_3824', 'YDT_4892', 'DXC_5781', 'NKT_3877', 'IBZ_8016', 'TPK_3513', 'HHZ_2871', 'KQP_1484', 'RKR_3989']
lecture_dict = {'YNB_4876': 'THU', 'PLS_3824': 'WED', 'YDT_4892': 'TUE', 'DXC_5781': 'WED', 'NKT_3877': 'WED', 'IBZ_8016': 'FRI', 'TPK_3513': 'MON', 'HHZ_2871': 'FRI', 'KQP_1484': 'MON', 'RKR_3989': 'MON'}

day = input("Enter the day: ").upper()
for item in lecture_list:
    if lecture_dict[item] == day:
        print(item)
