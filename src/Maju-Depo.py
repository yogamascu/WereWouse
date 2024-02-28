from tabulate import tabulate
import os
from termcolor import colored
from pyfiglet import Figlet



# database
data_warehouse = [
    {'ItemIDX': 'PR1', 'Product': 'Table', 'Material': 'Wood', 'Qty': 70, 'Price': 150000},
    {'ItemIDX': 'PR2', 'Product': 'Chair', 'Material': 'Plastic', 'Qty': 100, 'Price': 120000},
    {'ItemIDX': 'PR3', 'Product': 'Rug', 'Material': 'Wool', 'Qty': 35, 'Price': 2000000},
    {'ItemIDX': 'PR4', 'Product': 'Stool', 'Material': 'Wood', 'Qty': 49, 'Price': 300000},
    {'ItemIDX': 'PR5', 'Product': 'Blind', 'Material': 'Polyester', 'Qty': 89, 'Price': 250000}
]
# Celar screen so it wont get polluted with too many texts (coutersey of Mas Nabil)
def clear_screen():
    """
    A function to clean the user interface
    """
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For macOS and Linux
    else:
        _ = os.system('clear')


# def int_validation(prompt):
#     while True:
#         try:
#             num = float(input(prompt))
#             if num < 0:
#                 print('No negative numbers!')
#                 continue
#             else:
#                 break
#         except ValueError:
#             print('Only Numbers!')
#             continue

#     return int(num)
# def str_validation(prompt):
#     while True:
#         sentence = input(prompt)
#         if sentence.isalpha():
#             break
#         else:
#             print('You can only input string!')
#             continue
#     return sentence

def display_all():
    clear_screen()
    if data_warehouse:
        print("\nCurrent inventories of Maju-Depo:\n")
        total_qty = sum(item['Qty'] for item in data_warehouse)
        total_price = sum(item['Qty'] * item['Price'] for item in data_warehouse)
        table = data_warehouse.copy()
        table.append({'ItemIDX': 'Total', 'Product': '', 'Material': '', 'Qty': total_qty, 'Price': total_price})
        print(tabulate(table, headers="keys", tablefmt="fancy_grid"))
    else:
        print("\nUnfortunately, no data exists within the main database.")
        return

def show_specific_item():
    clear_screen()
    item_idx = input("Enter the ItemIDX to search: ")
    found = False
    for item in data_warehouse:
        if item['ItemIDX'] == item_idx.upper():
            print(tabulate([item], headers="keys", tablefmt="fancy_grid"))
            found = True
            break
    if not found:
        print("\nUnfortunately, no data exists within the main database.")

def insert_new_product():
    clear_screen()
    item_idx = input("Enter the ItemIDX: ").upper()
    for item in data_warehouse:
        if item['ItemIDX'] == item_idx.upper():
            print("\nData already exists within the database.")
            return

    product = input("Enter the product name: ")
    material = input("Enter the material: ")
    qty = input("Enter the quantity: ")
    price = input("Enter the price: \n")
    print("Would you like to save it into the database? \n")
    choice = input("Do you want to save the data? ")
    if choice == "1":
        new_product = {'ItemIDX': item_idx, 'Product': product.capitalize(), 'Material': material.capitalize(), 'Qty': qty, 'Price': price}
        data_warehouse.append(new_product)
        print("\nData Successfully saved.")
    else:
        print("\nNewly inserted data abandoned.")


def adjust_current_database():
    clear_screen()
    item_idx = input("Enter the ItemIDX to edit: ")
    for item in data_warehouse:
        if item['ItemIDX'] == item_idx.upper():
            print(tabulate([item], headers="keys", tablefmt="fancy_grid"))
            field = input("Enter the field to edit (Product/Material/Qty/Price): ").capitalize()
            if field in item:
                new_value = input(f"Enter the new value for {field}: ")
                if field == 'Qty' or field == 'Price':
                    new_value = int(new_value)
                item[field] = new_value
                print("Data Successfully Updated.")
            else:
                print("Invalid field.")
            return
    print("\nUnfortunately, the data you are looking for does not exist within the main database.")

def delete_item():
    clear_screen()
    item_idx = input("Enter the ItemIDX to delete: ")
    for item in data_warehouse:
        if item['ItemIDX'] == item_idx:
            choice = input("\nAre you sure you want to delete this item? (yes/no): ")
            if choice.lower() == 'yes':
                data_warehouse.remove(item)
                print("\nData successfully deleted.")
            return
    print("\nSorry, data you looking for does not exist within the main database.")

def main():
    while True:
        clear_screen()
        f = Figlet(font= 'standard')
        print(colored(f.renderText('Welcome to Maju-Depot Inventory System \n'),'light_red'))
       
        print("1. Display and Search")
        print("2. Insert New Product")
        print("3. Adjust Current Database")
        print("4. Delete Product")
        print("5. Exit the App\n")

        choice = input("Enter your choice: ")

        if choice == '1':
            clear_screen()
            while True:
                print("\nDisplay and Search:")
                print("\n1. View All Database")
                print("2. Show Specific Item")
                print("3. Return to Main Menu")

                sub_choice = input("\nEnter your choice: ")

                if sub_choice == '1':
                    display_all()
                elif sub_choice == '2':
                    show_specific_item()
                elif sub_choice == '3':
                    clear_screen()
                    break
                else:
                    print("Invalid input, choose only 1 or 2.")

        elif choice == '2':
            clear_screen()
            while True:
                print("\nInsert New Product:")
                print("1. Add a Product")
                print("2. Return to Main Menu")

                sub_choice = input("Enter your choice: ")

                if sub_choice == '1':
                    insert_new_product()
                elif sub_choice == '2':
                    clear_screen()
                    break
                else:
                    print("Invalid input choose 1 or 2!.")

        elif choice == '3':
            clear_screen()
            while True:
                print("\nAdjust Current Database:")
                print("1. Edit a Product")
                print("2. Return to Main Menu")

                sub_choice = input("Enter your choice: ")

                if sub_choice == '1':
                    adjust_current_database()
                elif sub_choice == '2':
                    clear_screen()
                    break
                else:
                    print("Invalid input, choose 1 or 2!.")

        elif choice == '4':
            clear_screen()
            while True:
                print("\nDelete Product:")
                print("1. Delete Item")
                print("2. Return to Main Menu")

                sub_choice = input("\nEnter your choice: ")

                if sub_choice == '1':
                    delete_item()
                elif sub_choice == '2':
                    clear_screen()
                    break
                else:
                    print("\nInvalid input, choose 1 or 2!")

        elif choice == '5':
            clear_screen()
            f2 = Figlet(font= 'larry3d')
            print(colored(f2.renderText('Thank you for using \n'),'yellow'))
            print("WereWouse app 0.1.0")
            break

        else:
            clear_screen()
            print("Invalid choice. Please enter a number between 1 and 5.")
            

if __name__ == "__main__":
    clear_screen()
    main()