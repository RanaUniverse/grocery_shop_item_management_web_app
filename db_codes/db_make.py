"""
db_codes/db_make.py
Here i will make the database by calling this function
from here and then i will use this in the main main.py
"""

from sqlmodel import (
    SQLModel,
    create_engine,
)

sqlite_file_name = "zzz_database.db"
DATABASE_URL = f"sqlite:///{sqlite_file_name}"


# DB_USERNAME = "rana"
# DB_PASSWORD = "abc"
# DB_HOST = "localhost"
# DB_PORT = "5432"
# DB_NAME = "grocery_db"

# DATABASE_URL = (
#     f"postgresql://{DB_USERNAME}:{DB_PASSWORD}" f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
# )


engine = create_engine(url=DATABASE_URL)


def create_db_and_tables():
    SQLModel.metadata.create_all(bind=engine)
