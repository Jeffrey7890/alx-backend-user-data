#!/usr/bin/env python3

"""DB module
"""

from sqlalchemy import create_engine, update
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError


from user import Base
from user import User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """ Adds user to database """
        user_ = User(email=email, hashed_password=hashed_password)
        self._session.add(user_)
        self._session.commit()
        return user_

    def find_user_by(self, **kwargs) -> User:
        """ Finds user from database """
        try:
            our_user = self._session.query(User).filter_by(**kwargs).first()
            if our_user is None:
                raise NoResultFound('Not found')
            return our_user
        except NoResultFound as e:
            raise NoResultFound(str(e))
        except InvalidRequestError as e:
            raise InvalidRequestError(e)

    def update_user(self, user_id: int, **kwargs) -> None:
        """ update user data
        """
        found_usr = self.find_user_by(id=user_id)
        valid_keys = [column.name for column in User.__table__.columns]
        for k, v in kwargs.items():
            if k not in valid_keys:
                raise ValueError
            setattr(found_usr, k, v)
        self._session.commit()

        return None
