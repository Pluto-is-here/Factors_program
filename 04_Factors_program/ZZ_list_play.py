import random

my_list = []

for item in range (0, 4):

    random_num =random.randint(1, 10)

    my_list.append(random_num)

print(my_list)

my_list.sort()

my_list_len = len(my_list)

print()
print(my_list)
print("The list has {} items".format(my_list_len))
print()