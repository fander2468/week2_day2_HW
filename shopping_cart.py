
# 1) Build a Shopping Cart
# You can use either lists or dictionaries. The program should have the following capabilities:

# 1) Takes in input
# 2) Stores user input into a dictionary or list
# 3) The User can add or delete items
# 4) The User can see current shopping list
# 5) The program Loops until user 'quits'
# 6) Upon quiting the program, print out all items in the user's list

#empty dictionary
shopping_dict = {}



#fuction used to display user choices
def show_clothing_options():
    return "Clothing Choices:\n 1-shoes\n 2-shirts\n 3-shorts\n 4-pants\n 5-under_garments\n 6-hats\n 7-accessories\n 8-dresses\n 9-leggings\n 10-boots\n 11-jackets\n 12-coats"



#fuction to delete the value the user chooses
def user_delete(delete_clothing):
    del shopping_dict[delete_clothing]



#fuction to add the key value pair to the dictionary at the user descretion
def user_add(add_clothing):
    if add_clothing == 1:
        shopping_dict[1] = 'shoes'
    elif add_clothing == 2:
        shopping_dict[2] = 'shirts'
    elif add_clothing == 3:
        shopping_dict[3] = 'shorts'
    elif add_clothing == 4:
        shopping_dict[4] = 'pants'
    elif add_clothing == 5:
        shopping_dict[5] = 'under garments'
    elif add_clothing == 6:
        shopping_dict[6] = 'hats'
    elif add_clothing == 7:
        shopping_dict[7] = 'accessories'
    elif add_clothing == 8:
        shopping_dict[8] = 'dresses'
    elif add_clothing == 10:
        shopping_dict[10] = 'leggings'
    elif add_clothing == 10:
        shopping_dict[10] = 'boots'
    elif add_clothing == 11:
        shopping_dict[11] = 'jackets'
    elif add_clothing == 12:
        shopping_dict[12] = 'coats'




# The program Loops through options until user 'quits'
while True:
    do_something = input("Do you want to 'add', delete or 'edit' press 'q' to quit")


    if str(do_something) == 'q' or str(do_something) == 'quit':
            break


    elif do_something == 'add' or do_something == 'delete':
        add_delete = input("Choose 'add' or 'delete'")
        if add_delete == 'add':
            clothing = int(input("Enter a 'number' for clothing choices:"))
            if clothing >= 1 and clothing <= 12:
                user_add(clothing)
        elif add_delete == 'delete':
            clothing_removal = int(input('Which item number do you wish to remove:'))
            if clothing_removal >= 1 or clothing_removal <= 12:
                user_delete(clothing_removal)


    elif do_something == 'edit':
        do_something_else = input("Enter 'list' to show list, or 'show' to show clothing choices")
        
        if str(do_something_else) == 'list' or str(do_something_else) == 'List':
            shopping_list = shopping_dict.items()
            for items in shopping_list:
                print(items)
        
        elif str(do_something_else) == 'show' or str(do_something_else) == 'Show':
            print(show_clothing_options())

   

    else:
        print("Please only enter correct input; clothing 'number' for clothing choices, 'show' to show choices, 'delete' to remove items, 'list' to view items in list or 'q' to quit.")


# print out all items in the user's list
shopping_list = shopping_dict.items()
for items in shopping_list:
    print(items)




    #