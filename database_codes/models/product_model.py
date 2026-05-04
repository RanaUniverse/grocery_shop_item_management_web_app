"""
database_codes/models/product_model.py
Here i will write the code to make the product table
"""

from typing import (
    Optional,
    TYPE_CHECKING,
)

from sqlmodel import (
    Field,
    SQLModel,
    Relationship,
)

if TYPE_CHECKING:
    from .category_model import CategoryModel


from utils.general_utils import generate_hex_uuid4


class ProductModel(SQLModel, table=True):
    """
    I make product will depends on the category table,
    many product can be from one category
    maybe some products are not any part of category
    """

    __tablename__ = "product_data"  # type: ignore

    # id_: int | None = Field(default=None, primary_key=True)
    id_: str | None = Field(
        default_factory=generate_hex_uuid4,
        primary_key=True,
    )

    name: str = Field(index=True)
    description: str | None

    quantity: int = Field(default=0)

    mrp_price: float | None
    purchase_price: float | None
    sell_price: float | None

    category_id: int | None = Field(default=None, foreign_key="category_data.id_")
    category: Optional["CategoryModel"] = Relationship(back_populates="products")
