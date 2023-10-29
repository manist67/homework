day_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

h_sum = 0
for day in day_of_week:
    h_sum += int(input("{} lecture time: ".format(day)))

print("The average time is {:0.2f} hours".format(h_sum / len(day_of_week)))
