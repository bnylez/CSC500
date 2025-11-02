class ItemToPurchase:
    """
    A class to represent an item that can be purchased.
    Contains item name, price, quantity, and description information.
    """
    
    def __init__(self, item_name="none", item_price=0.0, item_quantity=0, item_description="none"):
        """
        Initialize an ItemToPurchase object.
        
        Parameters:
        item_name (str): Name of the item (default: "none")
        item_price (float): Price of the item (default: 0.0)
        item_quantity (int): Quantity of the item (default: 0)
        item_description (str): Description of the item (default: "none")
        """
        self.item_name = item_name                    # Store the item name
        self.item_price = item_price                  # Store the item price
        self.item_quantity = item_quantity            # Store the item quantity
        self.item_description = item_description      # Store the item description

    def print_item_cost(self):
        """
        Calculate the total cost for this item (price * quantity) and print it.
        Output format: "ItemName Quantity @ $Price = $TotalCost"
        """
        total_cost = self.item_price * self.item_quantity  # Calculate total cost
        # Print formatted output with item details and total cost
        print(f"{self.item_name} {self.item_quantity} @ ${int(self.item_price)} = ${int(total_cost)}")

    def print_item_description(self):
        """
        Print the item's name and description.
        Output format: "ItemName: Description"
        """
        print(f"{self.item_name}: {self.item_description}")


class ShoppingCart:
    """
    A class to represent a shopping cart for online shopping.
    Manages a collection of items and provides cart operations.
    """
    
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        """
        Initialize a ShoppingCart object.
        
        Parameters:
        customer_name (str): Name of the customer (default: "none")
        current_date (str): Current date (default: "January 1, 2020")
        """
        self.customer_name = customer_name  # Store customer name
        self.current_date = current_date    # Store current date
        self.cart_items = []               # Initialize empty list for cart items
    
    def add_item(self, item_to_purchase):
        """
        Adds an item to cart_items list.
        
        Parameters:
        item_to_purchase (ItemToPurchase): The item to add to the cart
        """
        self.cart_items.append(item_to_purchase)  # Add item to the cart
    
    def remove_item(self, item_name):
        """
        Removes item from cart_items list by name.
        
        Parameters:
        item_name (str): Name of the item to remove
        
        Returns:
        None - Prints error message if item not found
        """
        # Search through cart items to find matching name
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)  # Remove the item
                return
        # If item not found, print error message
        print("Item not found in cart. Nothing removed.")
    
    def modify_item(self, item_to_purchase):
        """
        Modifies an item's description, price, and/or quantity.
        
        Parameters:
        item_to_purchase (ItemToPurchase): Item with updated attributes
        
        Returns:
        None - Prints error message if item not found
        """
        # Search through cart items to find matching name
        for item in self.cart_items:
            if item.item_name == item_to_purchase.item_name:
                # Update attributes if they're not default values
                if item_to_purchase.item_description != "none":
                    item.item_description = item_to_purchase.item_description
                if item_to_purchase.item_price != 0.0:
                    item.item_price = item_to_purchase.item_price
                if item_to_purchase.item_quantity != 0:
                    item.item_quantity = item_to_purchase.item_quantity
                return
        # If item not found, print error message
        print("Item not found in cart. Nothing modified.")
    
    def get_num_items_in_cart(self):
        """
        Returns total quantity of all items in cart.
        
        Returns:
        int: Total quantity of all items
        """
        total_quantity = 0
        # Sum up quantities of all items in cart
        for item in self.cart_items:
            total_quantity += item.item_quantity
        return total_quantity
    
    def get_cost_of_cart(self):
        """
        Determines and returns the total cost of all items in cart.
        
        Returns:
        float: Total cost of all items
        """
        total_cost = 0
        # Calculate total cost by multiplying price * quantity for each item
        for item in self.cart_items:
            total_cost += item.item_price * item.item_quantity
        return total_cost
    
    def print_total(self):
        """
        Outputs the shopping cart summary with item costs and total.
        Shows "SHOPPING CART IS EMPTY" if no items in cart.
        """
        if len(self.cart_items) == 0:
            print("SHOPPING CART IS EMPTY")  # Handle empty cart case
        else:
            # Print cart header with customer name and date
            print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
            print(f"Number of Items: {self.get_num_items_in_cart()}")
            # Print each item's cost details
            for item in self.cart_items:
                item.print_item_cost()
            # Print the total cost
            print(f"Total: ${int(self.get_cost_of_cart())}")
    
    def print_descriptions(self):
        """
        Outputs each item's description in the cart.
        """
        # Print cart header with customer name and date
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")
        # Print description for each item
        for item in self.cart_items:
            item.print_item_description()


def print_menu(shopping_cart):
    """
    Outputs a menu of options to manipulate the shopping cart.
    
    Parameters:
    shopping_cart (ShoppingCart): The shopping cart object (unused but kept for compatibility)
    
    Returns:
    str: User's menu choice
    """
    print("\nMENU")                           # Print menu header
    print("a - Add item to cart")            # Option to add items
    print("r - Remove item from cart")       # Option to remove items
    print("c - Change item quantity")        # Option to modify quantities
    print("i - Output items' descriptions")  # Option to show descriptions
    print("o - Output shopping cart")        # Option to show cart summary
    print("q - Quit")                        # Option to exit program
    print("Choose an option:")
    return input().strip()                   # Return user's choice


def main():
    """
    Main function to run the shopping cart program.
    Handles user input, creates shopping cart, and manages menu interactions.
    """
    # === INITIAL SETUP ===
    print("Enter customer's name:")          # Get customer name
    customer_name = input()
    print("Enter today's date:")             # Get current date
    current_date = input()
    
    # Output the name and date
    print(f"Customer name: {customer_name}")
    print(f"Today's date: {current_date}")
    
    # Create shopping cart instance
    cart = ShoppingCart(customer_name, current_date)
    
    # === MAIN PROGRAM LOOP ===
    while True:
        choice = print_menu(cart)            # Display menu and get user choice
        
        # Handle menu options
        if choice == 'q':
            print("Goodbye!")                # Exit message
            break                           # Exit the program loop
            
        elif choice == 'a':
            # === ADD ITEM TO CART ===
            print("\nADD ITEM TO CART")
            print("Enter the item name:")
            item_name = input()             # Get item name
            print("Enter the item description:")
            item_description = input()      # Get item description
            print("Enter the item price:")
            item_price = float(input())     # Get item price
            print("Enter the item quantity:")
            item_quantity = int(input())    # Get item quantity
            
            # Create new item and add to cart
            item = ItemToPurchase(item_name, item_price, item_quantity, item_description)
            cart.add_item(item)
            print()
            
        elif choice == 'r':
            # === REMOVE ITEM FROM CART ===
            print("\nREMOVE ITEM FROM CART")
            print("Enter name of item to remove:")
            item_name = input()             # Get item name to remove
            cart.remove_item(item_name)     # Remove item from cart
            print()
            
        elif choice == 'c':
            # === CHANGE ITEM QUANTITY ===
            print("\nCHANGE ITEM QUANTITY")
            print("Enter the item name:")
            item_name = input()             # Get item name
            print("Enter the new quantity:")
            new_quantity = int(input())     # Get new quantity
            
            # Create temporary item with updated quantity for modification
            temp_item = ItemToPurchase(item_name, 0.0, new_quantity, "none")
            cart.modify_item(temp_item)     # Modify the item in cart
            print()
            
        elif choice == 'i':
            # === OUTPUT ITEM DESCRIPTIONS ===
            print("\nOUTPUT ITEMS' DESCRIPTIONS")
            cart.print_descriptions()       # Print all item descriptions
            print()
            
        elif choice == 'o':
            # === OUTPUT SHOPPING CART ===
            print("\nOUTPUT SHOPPING CART")
            cart.print_total()              # Print cart summary and totals
            print()
            
        else:
            # === INVALID OPTION ===
            print("Invalid option. Please try again.")
            print()


if __name__ == "__main__":
    main()
