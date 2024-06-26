# Biscotti-Cafe-Service-Automation



## Overview

The Biscotti Cafe Management System is a simple Python-based application designed to manage orders at a cafe. It allows users to take orders, display the menu, add items to a table's order, and close orders to calculate the total bill.

## Features

- Display a menu with various items and their prices.
- Take orders for a specific table.
- Add items to a table's order with specified quantities.
- Display the current order with the total cost.
- Close an order and display the final bill.
- Manage multiple tables (up to 6 in this implementation).

## Classes

### MenuItem

Represents a single menu item.

- `__init__(self, name, price)`: Initializes the menu item with a name and price.
- `__repr__(self)`: Returns a string representation of the menu item in the format "name: $price".

### Menu

Represents the menu of the cafe.

- `__init__(self)`: Initializes the menu with predefined items.
- `display(self)`: Prints the menu items.
- `get_item(self, number)`: Retrieves a menu item by its number.

### Order

Represents an order for a table.

- `__init__(self)`: Initializes an empty order.
- `add_item(self, menu_item, quantity)`: Adds a specified quantity of a menu item to the order.
- `get_total(self)`: Calculates and returns the total cost of the order.
- `display(self)`: Prints the current order and the total cost.

### Table

Represents a table in the cafe.

- `__init__(self, table_number)`: Initializes a table with a table number and an active order.
- `add_to_order(self, menu_item, quantity)`: Adds a specified quantity of a menu item to the table's active order.
- `close_order(self)`: Displays the current order and the total bill, then resets the order.

### Cafe

Represents the cafe with multiple tables.

- `__init__(self, number_of_tables)`: Initializes the cafe with a menu and a specified number of tables.
- `take_order(self, table_number)`: Takes an order for a specified table.
- `close_order(self, table_number)`: Closes the order for a specified table and displays the total bill.
- `run(self)`: Runs the main loop of the cafe management system.

## How to Run

1. Ensure you have Python installed on your system.
2. Save the provided code to a file named `cafe.py`.
3. Open a terminal or command prompt and navigate to the directory containing `cafe.py`.
4. Run the script with the command: `python cafe.py`.

## Example Usage

1. When prompted, enter `1` to take an order.
2. Enter the table number (1-6) for which you want to take the order.
3. The menu will be displayed. Enter the number corresponding to the menu item you want to add to the order.
4. Enter the quantity for the selected item.
5. Repeat steps 3-4 to add more items to the order or type `done` to finish the order.
6. The current order and total cost will be displayed after each item is added.
7. When finished, enter `2` to close the order for a table and display the final bill.
8. Enter `3` to exit the program.

## Notes

- Ensure that the table number is between 1 and 6 when taking or closing orders.
- The menu is predefined and can be modified in the `Menu` class.
- The program runs in a loop until the user chooses to exit.

Enjoy managing your cafe with the Biscotti Cafe Management System!
