from app import db

class Product(db.Model):
    """
    Product model for inventory management
    
    Attributes:
        id (int): Unique identifier for the product
        name (str): Name of the product
        quantity (int): Quantity of the product in inventory
        price (float): Price of the product
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False, default=0)
    price = db.Column(db.Float, nullable=False)
    
    def __repr__(self):
        return f"Product(id={self.id}, name='{self.name}', quantity={self.quantity}, price={self.price})"
    
    def to_dict(self):
        """
        Convert the product object to a dictionary
        
        Returns:
            dict: Dictionary representation of the product
        """
        return {
            'id': self.id,
            'name': self.name,
            'quantity': self.quantity,
            'price': self.price
        }
