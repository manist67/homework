# author : Seung Min Lee
# since : 2023-03-25
# purpose : age in seconds 
import datetime

person_1 = {
    "month": 0,
    "year": 0,
    "day": 0
} # person 1 dictionary

person_2 = {
    "month": 0,
    "year": 0,
    "day": 0
} # person 2 dictionary

# input person 1 information
person_1["month"] = int(input("Person 1: Enter month born (1-12): "))
person_1["day"] = int(input("Person 1: Enter day born (1-31): "))
person_1["year"] = int(input("Person 1: Enter year born (4-digit): "))

# input person 2 information
person_2["month"] = int(input("Person 2: Enter month born (1-12): "))
person_2["day"] = int(input("Person 2: Enter day born (1-31): "))
person_2["year"] = int(input("Person 2: Enter year born (4-digit): "))


current_time = {
    "month": datetime.date.today().month,
    "year": datetime.date.today().year,
    "day": datetime.date.today().day
} # current datetime

numsecs_day = 24 * 60 * 60
numsecs_year = 365 * numsecs_day

avg_numsecs_year = (( 4 * numsecs_year) + numsecs_day) // 4
avg_numsecs_month = avg_numsecs_year // 12


# calculate 1900 to birth seconds
person_1_numsecs_1900_dob = ((person_1['year'] - 1900) * avg_numsecs_year) + \
                            ((person_1['month'] - 1) * avg_numsecs_month) + \
                            (person_1['day'] * numsecs_day)
        
person_2_numsecs_1900_dob = ((person_2['year'] - 1900) * avg_numsecs_year) + \
                            ((person_2['month'] - 1) * avg_numsecs_month) + \
                            (person_2['day'] * numsecs_day)
# calculate 1900 to today
numsecs_1900_today = ((current_time['year'] - 1900) * avg_numsecs_year) + \
                    ((current_time['month'] - 1) * avg_numsecs_month) + \
                    (current_time['day'] * numsecs_day)
        
# calcuate each age in seconds
person_1_age_in_secs = numsecs_1900_today - person_1_numsecs_1900_dob
person_2_age_in_secs = numsecs_1900_today - person_2_numsecs_1900_dob

# calculate age difference in seconds
diff = abs(person_1_age_in_secs - person_2_age_in_secs)

print("Age difference in seconds: {}".format(diff)) 
