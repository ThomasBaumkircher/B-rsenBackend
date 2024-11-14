from datetime import datetime
from typing import List
from sqlalchemy import Integer, String, DateTime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Boolean

from db.session import engine

Base = declarative_base()


class Products(Base):
    __tablename__ = "bookings"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    current_price: Mapped[float] = mapped_column(Integer, nullable=False)
    in_stock: Mapped[bool] = mapped_column(Boolean, default=True)

    history: Mapped[List["ProductHistory"]] = relationship("ProductHistory", back_populates="product")
    sales: Mapped[List["ProductSales"]] = relationship("ProductSales", back_populates="product")


class ProductHistory(Base):
    __tablename__ = "product_history"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    product_id: Mapped[int] = mapped_column(Integer, ForeignKey("products.id"))
    timestamp: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    price: Mapped[float] = mapped_column(Integer, nullable=False)

    product: Mapped[Products] = relationship(back_populates="history")


class ProductSales(Base):
    __tablename__ = "product_sales"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    product_id: Mapped[int] = mapped_column(Integer, ForeignKey("products.id"))
    sales_id: Mapped[int] = mapped_column(Integer, ForeignKey("sales.id"))

    product: Mapped[Products] = relationship("Products")
    sale: Mapped[Sales] = relationship("Sales")


class Sales(Base):
    __tablename__ = "sales"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    timestamp: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    price: Mapped[float] = mapped_column(Integer, nullable=False)
    amount: Mapped[int] = mapped_column(Integer, nullable=False)

    product_sale: Mapped[List["ProductSales"]] = relationship("ProductSales", back_populates="sale")


Base.metadata.create_all(engine)
