# Importing Sale and Product models from models.py, and Session class from SQLAlchemy ORM
from models import Sale, Product  # Ensure Product is imported
from sqlalchemy.orm import Session

# Function to add a sale record to the database
def add_sale(session: Session, product_id: int, quantity: int):
    """
    Adds a sale record to the database and removes the sold product from the inventory.
    
    Args:
        session (Session): SQLAlchemy session for database interaction.
        product_id (int): ID of the product being sold.
        quantity (int): Quantity of the product sold.
    
    Raises:
        ValueError: If there's an issue during the sale process.
    """
    try:
        # Calculate the total price for the sale based on product price and quantity
        total_price = calculate_total_price(session, product_id, quantity)
        
        # Create a new Sale instance with product_id, quantity, and total price
        sale = Sale(product_id=product_id, quantity=quantity, total_price=total_price)
        session.add(sale)  # Add the sale to the session (staging it for the database)
        
        # Find the product in the database by its ID
        product = session.query(Product).filter(Product.id == product_id).first()
        
        # If product exists, remove it from the inventory (delete it)
        if product:
            session.delete(product)
        else:
            # Raise an error if the product is not found
            raise ValueError(f"Product with ID {product_id} not found.")
        
        # Commit the transaction to save the sale and remove the product
        session.commit()
        return sale  # Return the created sale object
    except Exception as e:
        # Rollback the session in case of an error during the transaction
        session.rollback()
        raise ValueError(f"Error adding sale: {e}")

# Function to retrieve all sales from the database
def get_sales(session: Session):
    """
    Retrieves all sales records from the database.
    
    Args:
        session (Session): SQLAlchemy session for database interaction.
    
    Returns:
        list: A list of all Sale objects from the database.
    """
    return session.query(Sale).all()  # Query the Sale table and return all records

# Function to calculate the total price of a sale
def calculate_total_price(session: Session, product_id: int, quantity: int):
    """
    Calculates the total price for the given product and quantity.
    
    Args:
        session (Session): SQLAlchemy session for database interaction.
        product_id (int): ID of the product being sold.
        quantity (int): Number of units sold.
    
    Returns:
        float: The total price for the sale.
    
    Raises:
        ValueError: If the product is not found in the database.
    """
    # Query the database to find the product by its ID
    product = session.query(Product).filter(Product.id == product_id).first()
    
    # Raise an error if the product is not found
    if not product:
        raise ValueError(f"Product with ID {product_id} not found.")
    
    # Return the total price by multiplying product price by the quantity sold
    return product.price * quantity
