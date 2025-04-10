# Inventory Management API

A RESTful API for inventory management built with Python, Flask, and SQLite.

## Features

- Create, read, update, and delete products in inventory
- Store product details including name, quantity, and price
- Data persistence with SQLite database
- Comprehensive error handling and validation

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/products` | Get all products |
| GET | `/products/<id>` | Get a specific product by ID |
| POST | `/products` | Add a new product |
| PUT | `/products/<id>` | Update an existing product |
| DELETE | `/products/<id>` | Delete a product |

## Running the Application

```bash
python main.py
