import sys
import store
import products

# setup initial stock of inventory
product_list = [ products.Product("MacBook Air M2", price=1450, quantity=100),
                 products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 products.Product("Google Pixel 7", price=500, quantity=250)
               ]
best_buy = store.Store(product_list)


def start(store_instance: store.Store) -> None:
    """user interface for store interaction"""
    while True:
        print("--- Store Menu ---")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = int(input("Enter your choice: "))
        if choice == 1:
            print("------------")
            available_active_products = store_instance.get_all_products()
            for i, product in enumerate(available_active_products, start=1):
                print(f"{i}. ", end="")
                product.show()
            print("------------\n")
        elif choice == 2:
            print(f"Total of {store_instance.get_total_quantity()} items in store")
        elif choice == 3:
            still_ordering = True
            order_list = []
            while still_ordering:
                print("------------")
                available_active_products = store_instance.get_all_products()
                for i, product in enumerate(available_active_products, start=1):
                    print(f"{i}. ", end="")
                    product.show()
                print("------------")
                print("When you want to finish order, enter empty text.")
                product_num_input = input("Which product # do you want? ")
                product_amount_input = input("What amount do you want? ")
                if product_num_input == "":
                    still_ordering = False
                else:

                    try:
                        article_index = int(product_num_input) - 1
                        article_amount = int(product_amount_input)
                    except ValueError:
                        print("Error adding product!")
                        continue
                    try:
                        found_product = available_active_products[article_index]
                        order_list.append((found_product, article_amount))
                    except IndexError:
                        print("Error adding product!")
                        continue
            total_price = 0
            try:
                total_price = store_instance.order(order_list)
            except ValueError:
                print("Error while making order! Quantity larger than what exists!")
            if total_price != 0:
                print("*********")
                print(f"Order made! Total payment: {total_price}")
        elif choice == 4:
            print("Thank you for choosing our store. Goodbye!")
            sys.exit()
        else:
            print("Please enter a valid choice.")


def main():
    """programm entry point"""
    start(best_buy)


if __name__ == "__main__":
    main()
