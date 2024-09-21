# Import necessary modules and functions
import click  # For creating command-line interfaces
from database import SessionLocal  # Importing the database session from the database module
from products_service import create_product, get_all_products, delete_product  # Product-related services
from sales_service import add_sale, get_sales  # Sales-related services for managing sales

# CLI function to run the main program
@click.command()  # Marks this function as a Click command for CLI usage
def run():
    """Run the CLI application."""
    session = SessionLocal()  # Create a new session for interacting with the database

    # Main loop to display the menu and get user input for choosing an option
    while True:
        click.echo("1. Product Management")  # Displays option for product management
        click.echo("2. Sales Management")  # Displays option for sales management
        click.echo("3. Exit")  # Displays option to exit the program
        choice = click.prompt("Enter your choice", type=int)  # Prompts user for an input (an integer) to select a menu option

        # Conditional logic to navigate to the appropriate management function based on user's choice
        if choice == 1:
            manage_products(session)  # Calls the product management function
        elif choice == 2:
            manage_sales(session)  # Calls the sales management function
        elif choice == 3:
            break  # Breaks out of the loop and exits the program

# Product management menu
def manage_products(session):
    """Handle product management tasks."""
    # Loop to display product management options and get user input
    while True:
        click.echo("1. Add Product")  # Displays option to add a new product
        click.echo("2. View All Products")  # Displays option to view all products
        click.echo("3. Delete Product")  # Displays option to delete a product
        click.echo("4. Back to Main Menu")  # Displays option to go back to the main menu
        choice = click.prompt("Enter your choice", type=int)  # Prompts user for input (an integer) to select a product-related option

        # Conditional logic to handle different product management options
        if choice == 1:
            # Adding a product
            name = click.prompt("Enter product name")  # Prompts for the product's name
            price = click.prompt("Enter product price", type=float)  # Prompts for the product's price (float)
            try:
                create_product(session, name, price)  # Calls the function to create a new product
                click.echo(f"Product '{name}' added successfully.")  # Displays a success message
            except ValueError as e:
                click.echo(f"Error: {e}")  # Displays an error message if product creation fails
        elif choice == 2:
            # Viewing all products
            products = get_all_products(session)  # Retrieves a list of all products
            for product in products:
                click.echo(f"{product.id}. {product.name} - ${product.price}")  # Loops through and displays each product with its ID, name, and price
        elif choice == 3:
            # Deleting a product
            product_id = click.prompt("Enter product ID to delete", type=int)  # Prompts user for the product ID to delete
            try:
                delete_product(session, product_id)  # Calls the function to delete the product
                click.echo(f"Product with ID {product_id} deleted successfully.")  # Displays a success message for deletion
            except ValueError as e:
                click.echo(f"Error: {e}")  # Displays an error message if product deletion fails
        elif choice == 4:
            break  # Breaks out of the product management loop and goes back to the main menu

# Sales management menu
def manage_sales(session):
    """Handle sales management tasks."""
    # Loop to display sales management options and get user input
    while True:
        click.echo("1. Add Sale")  # Displays option to add a new sale
        click.echo("2. View All Sales")  # Displays option to view all sales
        click.echo("3. Back to Main Menu")  # Displays option to go back to the main menu
        choice = click.prompt("Enter your choice", type=int)  # Prompts user for input (an integer) to select a sales-related option

        # Conditional logic to handle different sales management options
        if choice == 1:
            # Adding a sale
            product_id = click.prompt("Enter product ID", type=int)  # Prompts for the product ID
            quantity = click.prompt("Enter quantity sold", type=int)  # Prompts for the quantity sold
            try:
                add_sale(session, product_id, quantity)  # Calls the function to add the sale
                click.echo("Sale added successfully.")  # Displays a success message for sale addition
            except ValueError as e:
                click.echo(f"Error: {e}")  # Displays an error message if sale addition fails
        elif choice == 2:
            # Viewing all sales
            sales = get_sales(session)  # Retrieves a list of all sales
            for sale in sales:
                click.echo(f"Sale ID: {sale.id}, Product ID: {sale.product_id}, "
                           f"Quantity: {sale.quantity}, Total Price: ${sale.total_price}, "
                           f"Date: {sale.date_created}")  # Loops through and displays each sale with its details
        elif choice == 3:
            break  # Breaks out of the sales management loop and goes back to the main menu

# If the script is executed directly, run the CLI application
if __name__ == "__main__":
    run()  # Calls the run function to start the CLI program
