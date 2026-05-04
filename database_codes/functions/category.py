"""
database_codes/functions/category.py
Here i will write the functions related to the category table to add
new data, update or delete data like this
"""

from sqlalchemy import Engine

from sqlmodel import Session

from ..models import (
    CategoryModel,
)

from utils.custom_logger import logger


def add_new_category_row(
    engine: Engine, category_obj: CategoryModel
) -> CategoryModel | None:
    """
    Here i will try to insert one category row if fails return none else the category obj
    """
    with Session(engine) as session:
        try:
            session.add(category_obj)
            session.commit()
            session.refresh(category_obj)
            return category_obj

        except Exception as e:
            logger.warning(f"Somethigns went wrong on category row insert, {e}")
            return None
