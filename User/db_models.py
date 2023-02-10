from sqlalchemy import Column, Integer, String, Date
from base import Base
from sqlalchemy import UniqueConstraint


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(30), nullable=False)
    last_name = Column(String(30), nullable=False)
    work_email = Column(String(60), nullable=False, unique=True)
    phone_number = Column(String(60), nullable=False, unique=True)
    topic = Column(String(600), nullable=False)
    date_of_birth = Column(Date, nullable=False)
    interest = Column(String(30), nullable=False)
    gender = Column(String(30), nullable=False)

    __table_args__ = (
        UniqueConstraint('work_email', 'phone_number', name='unique_email_phone_number'),
    )
