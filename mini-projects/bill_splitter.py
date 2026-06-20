running_total = 0
num_of_friends = 4
appetizers = 37.89
main_course = 57.34
desserts = 39.39
drinks = 64.21
tip = running_total*0.25
running_total += appetizers + main_course + desserts + drinks + tip
final_amount = running_total/num_of_friends
each_person_pays = round(final_amount, 2)
print('Each person pays:', each_person_pays)
