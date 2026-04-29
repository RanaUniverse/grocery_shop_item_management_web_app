"""
db_codes/models.py
This is the place where i will write the code of the database's table's model
These are the tables i will write here
"""

import time


from sqlmodel import (
    Field,
    Relationship,
    SQLModel,
)


def get_current_unix_time() -> int:
    """
    This will return the Epoch timestamp or posix time
    The time is from the 1st January 1970 utc
    """
    current_time = time.time()
    return int(current_time)


class CategoryModel(SQLModel, table=True):
    """
    This will represent the category the products are in which category
    category is the one part, as many product will belongs to one category
    """

    __tablename__ = "category_data"  # type: ignore

    id_: int | None = Field(default=None, primary_key=True)
    name: str

    products: list["ProductModel"] = Relationship(back_populates="category")


class ProductModel(SQLModel, table=True):
    """
    This is represent a row of the product details
    product is the many part, as one category can has many product
    """

    __tablename__ = "product_data"  # type: ignore

    id_: int | None = Field(default=None, primary_key=True)

    name: str = Field(index=True)
    description: str | None

    purchase_price: float | None
    selling_price: float | None
    mrp_price: float | None

    stock_count: int = Field(default=0)

    # i add this updated at newly now
    # updated_at: datetime = Field(
    #     sa_column=Column(DateTime(timezone=True)),
    #     default_factory=get_current_utc_time,
    # )
    updated_at: int = Field(
        default_factory=get_current_unix_time,
    )

    category_id: int | None = Field(default=None, foreign_key="category_data.id_")
    category: CategoryModel | None = Relationship(back_populates="products")
