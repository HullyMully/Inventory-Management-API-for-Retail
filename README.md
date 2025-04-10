# Inventory Management API for Retail

A RESTful API built with Flask for managing retail inventory. This API provides endpoints for creating, reading, updating, and deleting products in an inventory system.

## Features

- CRUD operations for products
- SQLite database for data persistence
- Input validation and error handling
- RESTful API design
- JSON response format

## API Endpoints

### Products

- `GET /products` - Get all products
- `GET /products/<id>` - Get a specific product
- `POST /products` - Create a new product
- `PUT /products/<id>` - Update an existing product
- `DELETE /products/<id>` - Delete a product

### Product Schema

```json
{
    "id": "integer",
    "name": "string",
    "quantity": "integer",
    "price": "float"
}
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/HullyMully/Inventory-Management-API-for-Retail.git
cd Inventory-Management-API-for-Retail
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python main.py
```

The API will be available at `http://localhost:5000`

## Environment Variables

- `SESSION_SECRET` - Secret key for the Flask application (default: "dev_secret_key")

## Error Handling

The API returns appropriate HTTP status codes and error messages in JSON format:

- 200: Success
- 201: Created
- 400: Bad Request
- 404: Not Found
- 405: Method Not Allowed
- 500: Internal Server Error

## Contributing

Feel free to submit issues and enhancement requests.

```bash
python main.py
