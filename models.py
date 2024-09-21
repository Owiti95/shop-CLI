# Import necessary modules and functions from SQLAlchemy for defining the database models
from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.sql import func

# Create a base class for declarative class definitions (used for mapping tables in the database)
Base = declarative_base()

# Define the Product class, which represents the 'products' table in the database
class Product(Base):
    __tablename__ = 'products'  # Set the table name to 'products'
    
    # Define the columns for the 'products' table
    id = Column(Integer, primary_key=True)  # The primary key column, auto-incrementing integer
    name = Column(String, nullable=False)  # A string column for the product name, cannot be null
    price = Column(Float, nullable=False)  # A float column for the product price, cannot be null
    
    # Define a relationship to the 'sales' table
    sales = relationship('Sale', back_populates='product', cascade="all, delete")
    """
    - This establishes a one-to-many relationship between products and sales.
    - The 'back_populates' argument sets up bidirectional relationship handling with the 'Sale' model.
    - The 'cascade="all, delete"' ensures that if a product is deleted, all its associated sales records
      in the 'sales' table are also deleted automatically.
    """

# Define the Sale class, which represents the 'sales' table in the database
class Sale(Base):
    __tablename__ = 'sales'  # Set the table name to 'sales'
    
    # Define the columns for the 'sales' table
    id = Column(Integer, primary_key=True)  # The primary key column, auto-incrementing integer
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)  
    """
    - This defines a foreign key column linking to the 'products' table.
    - It references the 'id' column in the 'products' table.
    - The ForeignKey ensures the 'product_id' corresponds to an existing product.
    - This column cannot be null, ensuring every sale is associated with a valid product.
    """
    quantity = Column(Integer, nullable=False)  # An integer column for the quantity sold, cannot be null
    total_price = Column(Float, nullable=False)  # A float column for the total price of the sale, cannot be null
    
    # Define a column for the date and time when the sale was created, automatically set on creation
    date_created = Column(DateTime(timezone=True), server_default=func.now())
    """
    - This column stores the date and time when a sale is recorded.
    - 'server_default=func.now()' ensures that the timestamp is automatically set to the current time when a new record is created.
    """
    
    # Define a relationship back to the 'Product' class
    product = relationship('Product', back_populates='sales')
    """
    - This sets up the other side of the relationship between the 'Sale' and 'Product' models.
    - 'back_populates' ensures that both models are aware of their relationship and can access each other.
    - A sale is linked to a product through this relationship.
    """
