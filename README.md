# Sales and Product Management CLI

## Overview
This is a Command-Line Interface (CLI) application built using Python and `Click` for managing products and sales. The application allows users to:
- Add, view, and delete products.
- Record and view sales transactions.
- Store and retrieve data from a database using SQLAlchemy.

## Features
### **Product Management:**
- Add new products with a name and price.
- View a list of all available products.
- Delete products by ID.

### **Sales Management:**
- Record a sale by specifying a product ID and quantity.
- View all recorded sales, including total price and sale date.
- Track sales history with timestamps for better business insights.

### **User-Friendly CLI:**
- Interactive menu for easy navigation.
- Clear prompts and input validation.
- Error handling to guide users through the process smoothly.

## Technologies Used
- **Python** (CLI Development)
- **Click** (Command-line interface library)
- **SQLAlchemy** (Database ORM)
- **SQLite** (Database for storing products and sales data)
- **Virtual Environments** (For dependency management)

## Installation
### Prerequisites
Ensure you have Python 3 installed on your system.

### Clone the Repository
```sh
 git clone https://github.com/Owiti95/cli-sales-management.git
 cd cli-sales-management
```

### Create a Virtual Environment (Recommended)
```sh
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Install Dependencies
```sh
pip install -r requirements.txt
```

## Usage
Run the application using the following command:
```sh
python main.py
```

### Main Menu
Once the CLI starts, you will see a menu with options:
```
1. Product Management
2. Sales Management
3. Exit
```
Enter the corresponding number to navigate through the options.

### Product Management
- **Add Product**: Enter product details when prompted.
- **View All Products**: Displays all available products.
- **Delete Product**: Remove a product by entering its ID.

### Sales Management
- **Add Sale**: Enter the product ID and quantity sold.
- **View All Sales**: Displays all recorded sales with timestamps.

## Database Schema
This CLI app uses SQLAlchemy to manage database interactions.

### **Product Table:**
| Column       | Type    | Constraints |
|-------------|--------|-------------|
| `id`        | Integer | Primary Key |
| `name`      | String  | Not Null    |
| `price`     | Float   | Not Null    |

### **Sales Table:**
| Column       | Type    | Constraints |
|-------------|--------|-------------|
| `id`        | Integer | Primary Key |
| `product_id`| Integer | Foreign Key referencing `Product.id` |
| `quantity`  | Integer | Not Null    |
| `total_price` | Float  | Not Null    |
| `date_created` | Timestamp | Defaults to current time |

## Future Enhancements
- Implement user authentication.
- Add support for exporting reports in CSV format.
- Enhance error handling and input validation.
- Introduce role-based access control for different user levels.
- Extend support for more database options (PostgreSQL, MySQL).
