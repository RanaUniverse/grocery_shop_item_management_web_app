"""
db_codes/models/__init__.py
Here i make it as a package as i will write the models here in this place
I will write the models ie the tables my database will need in this package
"""

from .category_model import CategoryModel
from .product_model import ProductModel
from .user_model import UserModel

__all__ = [
    "CategoryModel",
    "ProductModel",
    "UserModel",
]
