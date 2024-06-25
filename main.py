class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f"{self.name}: ${self.price:.2f}"


class Menu:
    def __init__(self):
        self.items = {
            1: MenuItem('Coffee', 2.50),
            2: MenuItem('Tea', 2.00),
            3: MenuItem('Sandwich', 5.00),
            4: MenuItem('Burger', 7.50),
            5: MenuItem('Fries', 3.00),
            6: MenuItem('Cake', 4.00)
        }

    def display(self):
        print("Menu:")
        for number, item in self.items.items():
            print(f"{number}. {item}")
        print()

    def get_item(self, number):
        return self.items.get(number)


class Order:
    def __init__(self):
        self.items = {}

    def add_item(self, menu_item, quantity):
        if menu_item.name in self.items:
            self.items[menu_item.name]['quantity'] += quantity
        else:
            self.items[menu_item.name] = {'item': menu_item, 'quantity': quantity}

    def get_total(self):
        total = sum(item['item'].price * item['quantity'] for item in self.items.values())
        return total

    def display(self):
        print("Current Order:")
        for item in self.items.values():
            print(f"{item['quantity']} x {item['item'].name} @ ${item['item'].price:.2f} each")
        print(f"Total: ${self.get_total():.2f}\n")


class Table:
    def __init__(self, table_number):
        self.table_number = table_number
        self.active_order = Order()

    def add_to_order(self, menu_item, quantity):
        self.active_order.add_item(menu_item, quantity)

    def close_order(self):
        self.active_order.display()
        print(f"Closing order for Table {self.table_number}. Total bill: ${self.active_order.get_total():.2f}")
        self.active_order = Order()  # Reset order for the table


class Cafe:
    def __init__(self, number_of_tables):
        self.menu = Menu()
        self.tables = {i: Table(i) for i in range(1, number_of_tables + 1)}

    def take_order(self, table_number):
        if table_number not in self.tables:
            print("Invalid table number. Please choose a table between 1 and 6.")
            return

        table = self.tables[table_number]
        while True:
            self.menu.display()
            order_item = input("Enter the number of the food item (or type 'done' to finish): ")
            if order_item == 'done':
                break
            try:
                item_number = int(order_item)
                menu_item = self.menu.get_item(item_number)
                if not menu_item:
                    print("Invalid item number. Please choose a number from the menu.")
                    continue
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                continue

            try:
                quantity = int(input(f"Enter the quantity for {menu_item.name}: ").strip())
                if quantity <= 0:
                    raise ValueError
            except ValueError:
                print("Invalid quantity. Please enter a positive integer.")
                continue

            table.add_to_order(menu_item, quantity)
            table.active_order.display()

    def close_order(self, table_number):
        if table_number not in self.tables:
            print("Invalid table number. Please choose a table between 1 and 6.")
            return

        table = self.tables[table_number]
        table.close_order()

    def run(self):
        while True:
            print("Welcome to Biscotti Cafe\n1. Take Order\n2. Close Order\n3. Exit")
            choice = input("Enter your choice: ").strip()
            if choice == '1':
                try:
                    table_number = int(input("Enter the table number (1-6): ").strip())
                    self.take_order(table_number)
                except ValueError:
                    print("Invalid table number. Please enter a number between 1 and 6.")
            elif choice == '2':
                try:
                    table_number = int(input("Enter the table number (1-6): ").strip())
                    self.close_order(table_number)
                except ValueError:
                    print("Invalid table number. Please enter a number between 1 and 6.")
            elif choice == '3':
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    cafe = Cafe(number_of_tables=6)
    cafe.run()
