from flask import request, jsonify
import logging
from app import app, db
from models import Product

logger = logging.getLogger(__name__)

@app.route('/products', methods=['GET'])
def get_products():
    """
    Get all products from the inventory
    
    Returns:
        JSON response with all products or empty list
    """
    try:
        products = Product.query.all()
        return jsonify({
            'status': 'success',
            'data': [product.to_dict() for product in products],
            'count': len(products)
        }), 200
    except Exception as e:
        logger.error(f"Error retrieving products: {str(e)}")
        return jsonify({
            'status': 'error',
            'message': 'Unable to retrieve products',
            'error': str(e)
        }), 500

@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    """
    Get a specific product by its ID
    
    Args:
        product_id (int): The ID of the product to retrieve
        
    Returns:
        JSON response with product details or error
    """
    try:
        product = Product.query.get(product_id)
        if not product:
            return jsonify({
                'status': 'error',
                'message': f'Product with ID {product_id} not found'
            }), 404
            
        return jsonify({
            'status': 'success',
            'data': product.to_dict()
        }), 200
    except Exception as e:
        logger.error(f"Error retrieving product {product_id}: {str(e)}")
        return jsonify({
            'status': 'error',
            'message': 'Unable to retrieve product',
            'error': str(e)
        }), 500

@app.route('/products', methods=['POST'])
def add_product():
    """
    Add a new product to the inventory
    
    Request body should contain:
        name (str): Name of the product
        quantity (int): Quantity of the product
        price (float): Price of the product
        
    Returns:
        JSON response with the newly created product or error
    """
    try:
        data = request.json
        
        # Validate required fields
        if not all(key in data for key in ['name', 'quantity', 'price']):
            return jsonify({
                'status': 'error',
                'message': 'Missing required fields: name, quantity, and price are required'
            }), 400
            
        # Validate data types
        if not isinstance(data['name'], str) or not data['name']:
            return jsonify({
                'status': 'error',
                'message': 'Name must be a non-empty string'
            }), 400
            
        try:
            quantity = int(data['quantity'])
            if quantity < 0:
                return jsonify({
                    'status': 'error',
                    'message': 'Quantity must be a non-negative integer'
                }), 400
        except (ValueError, TypeError):
            return jsonify({
                'status': 'error',
                'message': 'Quantity must be a non-negative integer'
            }), 400
            
        try:
            price = float(data['price'])
            if price <= 0:
                return jsonify({
                    'status': 'error',
                    'message': 'Price must be a positive number'
                }), 400
        except (ValueError, TypeError):
            return jsonify({
                'status': 'error',
                'message': 'Price must be a positive number'
            }), 400
            
        # Create new product
        new_product = Product(
            name=data['name'],
            quantity=quantity,
            price=price
        )
        
        db.session.add(new_product)
        db.session.commit()
        
        return jsonify({
            'status': 'success',
            'message': 'Product added successfully',
            'data': new_product.to_dict()
        }), 201
        
    except Exception as e:
        db.session.rollback()
        logger.error(f"Error adding product: {str(e)}")
        return jsonify({
            'status': 'error',
            'message': 'Unable to add product',
            'error': str(e)
        }), 500

@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    """
    Update an existing product
    
    Args:
        product_id (int): The ID of the product to update
        
    Request body can contain:
        name (str, optional): New name for the product
        quantity (int, optional): New quantity for the product
        price (float, optional): New price for the product
        
    Returns:
        JSON response with the updated product or error
    """
    try:
        product = Product.query.get(product_id)
        if not product:
            return jsonify({
                'status': 'error',
                'message': f'Product with ID {product_id} not found'
            }), 404
            
        data = request.json
        
        # Update fields if provided
        if 'name' in data:
            if not isinstance(data['name'], str) or not data['name']:
                return jsonify({
                    'status': 'error',
                    'message': 'Name must be a non-empty string'
                }), 400
            product.name = data['name']
            
        if 'quantity' in data:
            try:
                quantity = int(data['quantity'])
                if quantity < 0:
                    return jsonify({
                        'status': 'error',
                        'message': 'Quantity must be a non-negative integer'
                    }), 400
                product.quantity = quantity
            except (ValueError, TypeError):
                return jsonify({
                    'status': 'error',
                    'message': 'Quantity must be a non-negative integer'
                }), 400
                
        if 'price' in data:
            try:
                price = float(data['price'])
                if price <= 0:
                    return jsonify({
                        'status': 'error',
                        'message': 'Price must be a positive number'
                    }), 400
                product.price = price
            except (ValueError, TypeError):
                return jsonify({
                    'status': 'error',
                    'message': 'Price must be a positive number'
                }), 400
                
        db.session.commit()
        
        return jsonify({
            'status': 'success',
            'message': 'Product updated successfully',
            'data': product.to_dict()
        }), 200
        
    except Exception as e:
        db.session.rollback()
        logger.error(f"Error updating product {product_id}: {str(e)}")
        return jsonify({
            'status': 'error',
            'message': 'Unable to update product',
            'error': str(e)
        }), 500

@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    """
    Delete a product from the inventory
    
    Args:
        product_id (int): The ID of the product to delete
        
    Returns:
        JSON response with success message or error
    """
    try:
        product = Product.query.get(product_id)
        if not product:
            return jsonify({
                'status': 'error',
                'message': f'Product with ID {product_id} not found'
            }), 404
            
        db.session.delete(product)
        db.session.commit()
        
        return jsonify({
            'status': 'success',
            'message': f'Product with ID {product_id} deleted successfully'
        }), 200
        
    except Exception as e:
        db.session.rollback()
        logger.error(f"Error deleting product {product_id}: {str(e)}")
        return jsonify({
            'status': 'error',
            'message': 'Unable to delete product',
            'error': str(e)
        }), 500

@app.route('/')
def index():
    """
    Root endpoint with API information
    
    Returns:
        JSON response with API information
    """
    return jsonify({
        'name': 'Inventory Management API',
        'version': '1.0',
        'endpoints': {
            'GET /products': 'Get all products',
            'GET /products/<id>': 'Get a specific product',
            'POST /products': 'Add a new product',
            'PUT /products/<id>': 'Update a product',
            'DELETE /products/<id>': 'Delete a product'
        }
    })

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({
        'status': 'error',
        'message': 'Resource not found'
    }), 404

@app.errorhandler(405)
def method_not_allowed(error):
    """Handle 405 errors"""
    return jsonify({
        'status': 'error',
        'message': 'Method not allowed'
    }), 405

@app.errorhandler(500)
def server_error(error):
    """Handle 500 errors"""
    return jsonify({
        'status': 'error',
        'message': 'Internal server error'
    }), 500
