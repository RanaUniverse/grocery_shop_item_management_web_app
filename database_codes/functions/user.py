"""
database_codes/functions/user.py
Here i will write the code related to user table
i will want to add update or delte user
"""

from sqlalchemy import Engine
from sqlmodel import Session

from ..models.user_model import UserModel

from utils.custom_logger import logger


def add_new_user_row(engine: Engine, user_obj: UserModel) -> UserModel | None:
    """
    i will try to insert new user row in the user table
    """

    with Session(engine) as session:
        try:
            session.add(user_obj)
            session.commit()
            session.refresh(user_obj)
            return user_obj

        except Exception as e:
            logger.warning(f"User row insert fails due to some error, {e}")
