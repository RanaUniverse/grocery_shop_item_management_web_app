"""
database_codes/functions/product.py
Here i will work the product related python code
i will here write the code which will help to add, update or delete the products
so i will need this module
"""

from sqlalchemy import Engine

from sqlmodel import Session

from ..models import (
    ProductModel,
)


def add_new_product_row(
    database_engine: Engine,
    name: str,
    description: str | None,
    quantity: int,
    mrp_price: float | None,
    purchase_price: float | None,
    sell_price: float | None,
):
    """
    Here i will want i will pass some args so that
    it will try to add those in the product table
    and upon success it will return the row or none
    """
    with Session(database_engine) as session:
        product_obj = ProductModel(
            name=name,
            description=description,
            quantity=quantity,
            mrp_price=mrp_price,
            purchase_price=purchase_price,
            sell_price=sell_price,
        )
        try:
            session.add(product_obj)
            session.commit()
            session.refresh(product_obj)
            return product_obj
        except Exception as e:
            print(f"Something wrong happens here regarding the product add, {e}")
            return None
