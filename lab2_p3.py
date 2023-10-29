import math

city_count = int(input("How many cities? "))
print("For {} cities, there are {} possible routes".format(city_count, math.factorial(city_count)))
