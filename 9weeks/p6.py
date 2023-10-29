import random
lecture_list = ['YNB_4876', 'PLS_3824', 'YDT_4892', 'DXC_5781', 'NKT_3877', 'IBZ_8016', 'TPK_3513', 'HHZ_2871', 'KQP_1484', 'RKR_3989']
lecture_dict = {'YNB_4876': 'THU', 'PLS_3824': 'WED', 'YDT_4892': 'TUE', 'DXC_5781': 'WED', 'NKT_3877': 'WED', 'IBZ_8016': 'FRI', 'TPK_3513': 'MON', 'HHZ_2871': 'FRI', 'KQP_1484': 'MON', 'RKR_3989': 'MON'}

random.seed(int(input('Enter the seed: ')))
# 채점을 용이하기 하기 위해 생성되는 랜덤 시퀀스가 고정되도록 하는 부분입니다.
# 무시하셔도 되고, 실행 시 Enter the seed: 부분에 0을 입력하시기 바랍니다.

idx = random.randint(0, len(lecture_list)-1)
print("The selected lecture is {} ({})"
      .format(lecture_list[idx], lecture_dict[lecture_list[idx]]))
