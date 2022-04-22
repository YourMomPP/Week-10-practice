from db import *
from getname import random_name
from prettytable import PrettyTable


breeds = ["Ragdoll", "Scottish Fold", "Himalayan", "Siberian"]


def display_breed():
    print('''\nCat available breed''')
    for index, breed in enumerate(breeds):
        print(f"{index+1}. {breed}")


print("Welcome to Stray Cat Registration APP")
print("-------------------------------------\n")

# Missing get_cat() feature! 

menu_1 = '''Menu
1. Register Cat 😻
2. Listed Cat 🐈
3. Update Cat 😼
4. Remove Cat 🙀
5. Exit 🚪
'''

menu_2 = '''\nCat Name
1. Generate name
2. Enter name
'''
while True:
    print(menu_1)
    
    menu_one_input = input("Enter menu number 1 -> 5: ")

    if menu_one_input == "1":

        print(menu_2)
        
        register_name = input("Enter menu number 1 -> 2: ")
        
        # Random name generator
        if register_name == "1":
            cat_name = random_name('cat')
            print(f"Your generated cat name is: {cat_name}")

        elif register_name == "2":
            cat_name = input("\nEnter cat name: ")

        cat_gender = input("\nCat gender (m/f): ")

        display_breed()
        while True:
            try:
                register_breed = int(
                input(f"\nEnter menu number 1 -> {len(breeds)}: "))
                break
            except ValueError:
                print("Invalid Input!")
                continue
        cat_breed = ''

        cat_dob = input(
            f"\nEnter {'her' if cat_gender == 'f' else 'his'} date of birth (yyyy-mm-dd): ")

        cat_description = input("\nAnything to note for this cat: ")

        cat_info = (cat_name, cat_gender, cat_breed, cat_dob, cat_description)

        register_cat(cat_info)
    

    elif menu_one_input == "2":
        all_cat = get_cats()
        # TODO:
        # display all cat information in a table format using PrettyTable library
        table = PrettyTable()
        table.field_names = ["ID", "Name", "Gender", "Breed", "Dob", "Description"]
        table.add_rows(all_cat)
        print(table.get_string())

    # Missing feature!
    # elif menu_one_input == "3":
    #     while True:
    #         try:
    #             id = int(input("Enter cat ID: "))
    #             break
    #         except ValueError:
    #             print("invalid input")
    #             continue
    #     one_cat = get_cat(id)
    #     table = PrettyTable()
    #     table.field_names = ["ID", "Name", "Gender", "Breed", "Dob", "Description"]    
    #     table.add_row(one_cat)
    #     print(table.get_string())
    


    elif menu_one_input == "3":
        while True:
            try:
                update_cat_id = int(input("\nEnter cat ID for update: "))
                break
            except ValueError:
                print("Invalid Input!")
                continue
        id, name, gender, breed, dob, description = get_cat(update_cat_id)

        update_name = input(f"Update Name ({name}): ")
        if update_name == '':
            update_name = name

        update_gender = input(f"Update Gender ({gender}): ")
        if update_gender == '':
            update_gender = gender

        display_breed()
        while True:
            try:
                update_breed = int(
                input(f"\nEnter menu number 1 -> {len(breeds)} ({breed}): "))
                break
            except ValueError:
                print("Invalid Input!")
                continue
        if update_breed == '':
            update_breed = breed
        else:
            update_breed = breeds[update_breed - 1]

        update_dob = input(f"Update DOB ({dob}): ")
        if update_dob == '':
            update_dob = dob

        update_description = input(f"Update Description ({description}): ")
        if update_description == '':
            update_description = description

        cat_update_data = (update_cat_id, update_name, update_gender,
                        update_breed, update_dob, update_description)

        update_cat(cat_update_data)
    
    elif menu_one_input == "4":
        while True:
            try:
                remove_cat_id = int(input("\nCat ID to be remove: "))
                remove_cat(remove_cat_id)
                break
            except ValueError:
                print("Invalid Input!")
                continue
    elif menu_one_input == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid Input!")
        continue
