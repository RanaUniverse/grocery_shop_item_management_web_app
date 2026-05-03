"""
database_codes/models/category_model.py
Here i will store the information about the category of the products
"""

from typing import TYPE_CHECKING

from sqlmodel import (
    Field,
    SQLModel,
    Relationship,
)

if TYPE_CHECKING:
    from .product_model import ProductModel


class CategoryModel(SQLModel, table=True):
    """
    The relation between category and product are like
    one category can have many or no product at all"""

    __tablename__ = "category_data"  # type: ignore

    id_: int | None = Field(default=None, primary_key=True)

    name: str = Field(index=True)
    description: str | None = Field(default=None)

    products: list["ProductModel"] = Relationship(back_populates="category")
