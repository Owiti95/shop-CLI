# products_service.py

# Import the Product model and the Session class from SQLAlchemy ORM
from models import Product
from sqlalchemy.orm import Session

# Function to create a new product in the database
def create_product(session: Session, name: str, price: float):
    """
    Adds a new product to the database with the given name and price.
    
    Args:
        session (Session): SQLAlchemy session for interacting with the database.
        name (str): Name of the product.
        price (float): Price of the product.
    """
    # Create a new Product instance
    new_product = Product(name=name, price=price)
    
    # Add the new product to the session (staging for the database)
    session.add(new_product)
    
    # Commit the transaction to save the product in the database
    session.commit()

# Function to retrieve all products from the database
def get_all_products(session: Session):
    """
    Retrieves all products from the database.
    
    Args:
        session (Session): SQLAlchemy session for interacting with the database.
    
    Returns:
        list: A list of all Product objects from the database.
    """
    # Query the Product table and return all records
    return session.query(Product).all()

# Function to delete a product from the database
def delete_product(session: Session, product_id: int):
    """
    Deletes a product from the database by its ID.
    
    Args:
        session (Session): SQLAlchemy session for interacting with the database.
        product_id (int): The ID of the product to be deleted.
    
    Raises:
        ValueError: If the product with the given ID is not found.
    """
    # Query the Product table to find the product with the given ID
    product = session.query(Product).filter(Product.id == product_id).first()
    
    # If the product exists, delete it and commit the change
    if product:
        session.delete(product)
        session.commit()
    else:
        # If the product does not exist, raise an error
        raise ValueError("Product not found")
