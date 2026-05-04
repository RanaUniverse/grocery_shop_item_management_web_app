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

from utils.custom_logger import logger


def add_new_product_row(
    engine: Engine,
    product_obj: ProductModel,
) -> ProductModel | None:
    """
    Here i will want to call this function
    to add new data in the product table
    upon success it will return the row or none
    """
    with Session(engine) as session:
        try:
            session.add(product_obj)
            session.commit()
            session.refresh(product_obj)
            return product_obj

        except Exception as e:
            logger.warning(
                f"Somethings wrong when try to insert into the product row, {e}"
            )
            return None
