from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, func, event, Date
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()


class Contact(Base):
    __tablename__ = "contacts"
    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    surname = Column(String)
    email = Column(String, unique=True, index=True)
    phone = Column(String, default="None", nullable=False)
    birthday = Column(Date, default=None, nullable=True)
    additional = Column(String, default="None", nullable=False)
    created_at = Column(DateTime, default=func.now())  
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())