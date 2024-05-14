import os
from my_functions import *

def menu(user):
    while True:
        try:
            print(f"=====[Options]=====\n")
            print(f"1. List Products")
            print(f"2. Buy Products")
            print(f"3. Register Products")
            print(f"4. Update Products")
            print(f"5. Remove Products")
            print(f"6. Exit\n")

            menu_opt = int(input("Select: "))
            print(f"===================")

            if menu_opt == 1:
                os.system("cls")
                list_products()

                products = list_products()

                for product in products:
                    print(f"===================")
                    print(f"Id: {product[0]}")
                    print(f"Name: {product[1]}")
                    print(f"Stripe: {product[2]}")
                    print(f"Price: R${product[3]}")
                    print(f"Quantity: {product[4]}\n")

                input("Press Enter to Continue...")
                os.system("cls")
            elif menu_opt == 2:
                os.system("cls")

                list_products()

                products = list_products()

                for product in products:
                    print(f"===================")
                    print(f"Id: {product[0]}")
                    print(f"Name: {product[1]}")
                    print(f"Stripe: {product[2]}")
                    print(f"Price: R${product[3]}")
                    print(f"Quantity: {product[4]}\n")
                
                e_select_id = int(input("Product Id: "))
                e_quantity = int(input("Quantity: "))
                print(f"")

                if e_quantity <= 0:
                    print(f"Invalid Quantity. Type Again.")
                    print(f"==============================\n")
                    input(f"Press Enter to Continue...")
                    os.system("cls")
                else:
                    buy_products(e_select_id, e_quantity)
                    print(f"Product(s) Purchased Successfully!")
                    print(f"==================================\n")
                    input("Press Enter to Continue...")
                    os.system("cls")
            elif menu_opt == 3:
                os.system("cls")

                print(f"===================")
                new_p_name = input("Name: ")
                new_p_stripe = input("Stripe: ")
                new_p_price = float(input("Price: R$"))
                new_p_quantity = int(input("Quantity: "))
                print(f"===================\n")

                register_products(new_p_name, new_p_stripe, new_p_price, new_p_quantity)
                print(f"Product Registered Sucessfully!")
                input("Press Enter to Continue...")
                os.system("cls")
            elif menu_opt == 4:
                os.system("cls")

                list_products()

                products = list_products()

                for product in products:
                    print(f"===================")
                    print(f"Id: {product[0]}")
                    print(f"Name: {product[1]}\n")

                product_id = int(input("Product Id: "))
                print(f"===================\n")

                print(f"===================")
                product_name = input("Name: ")
                product_stripe = input("Stripe: ")
                product_price = float(input("Price: R$"))
                product_quantity = int(input("Quantity: "))
                print(f"===================\n")

                update_products(product_id, product_name, product_stripe, product_price, product_quantity)
                print(f"Product Updated Sucessfully!")
                input("Press Enter to Continue...")
                os.system("cls")
            elif menu_opt == 5:
                list_products()

                products = list_products()

                for product in products:
                    print(f"===================")
                    print(f"Id: {product[0]}")
                    print(f"Name: {product[1]}")
                    print(f"Stripe: {product[2]}")
                    print(f"Price: R${product[3]}")
                    print(f"Quantity: {product[4]}\n")
                choose_id = int(input("Id: "))
                print(f"===================")

                remove_products(choose_id)

                print(f"Product Removed Sucessfully!")
                input("Press Enter to Continue...")
                os.system("cls")
            elif menu_opt == 6:
                print(f"Exiting...")
                input("Press Enter to Continue...")
                os.system("cls")
                break
            else:
                print(f"Invalid Option.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            print(f"===================")
            input("Press Enter to Continue...")
            os.system("cls")