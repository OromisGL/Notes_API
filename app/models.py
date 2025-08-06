from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String, nullable=False)
    # SQLALCHEMY relationship ist hilfreich um später besser abfragen zu etstellen 
    notes = relationship("Notes", back_populates="user")

class Category(Base):
    __tablename__ = "category"
    id = Column(Integer, primary_key=True, index=True)
    description = Column(String, index=True)
    notes = relationship("Notes", back_populates="category_rel")

class Notes(Base):
    __tablename__ = "notes"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    text = Column(Text,index=True)
    created = Column(DateTime, server_default=func.now(), index=True)
    created_by = Column(Integer, ForeignKey("users.id"))
    category = Column(Integer, ForeignKey("category.id"))
    user = relationship("User", back_populates="notes")
    category_rel = relationship("Category", back_populates="notes")

