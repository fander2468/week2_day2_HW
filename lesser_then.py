# Given a list as a parameter,write a function that returns a list of numbers that are less than ten
# For example: Say your input parameter to the function is [1,11,14,5,8,9]...Your output should [1,5,8,9]

my_list = [1,2,12,14,5,6,77,8,22,3,10,13]

def lesser_than_ten(numbers):
    new_list = []
    for number in numbers:
        if number < 10:
            new_list.append(number)
    return new_list    

print(lesser_than_ten(my_list))
