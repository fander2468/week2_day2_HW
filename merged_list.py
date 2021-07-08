# Write a function that takes in two lists and returns the two lists merged together and sorted
# Hint: You can use the .sort() method
my_first_list = [1,3,55,33,22,74,24]
my_second_list = [3,2,5,9,32,11,24,26]


def merged_list(first, second):
     new_list = first + second
     return sorted(new_list)

print(merged_list(my_first_list, my_second_list))