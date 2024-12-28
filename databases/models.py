from sqlalchemy import String, Integer, Column, ForeignKey, Date, create_engine, Text, Table, Float
from sqlalchemy.orm import relationship, sessionmaker, Mapped, mapped_column, DeclarativeBase
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker , AsyncAttrs


class Base(AsyncAttrs,DeclarativeBase):
    pass

class Product(Base):
    __tablename__ = "product"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(Text)
    price: Mapped[float] = mapped_column(Float, nullable=False)
    image: Mapped[str] = mapped_column(String(255))
    materials: Mapped[str] = mapped_column(Text)
    category: Mapped[str] = mapped_column(String(255))
    sub_category: Mapped[str] = mapped_column(String(255))
    url: Mapped[str] = mapped_column(String(255))


    carts = relationship("Cart", back_populates="product")


class Cart(Base):
    __tablename__ = "cart"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    product_id: Mapped[int] = mapped_column(Integer, ForeignKey("product.id"), nullable=False)
    quantity: Mapped[int] = mapped_column(Integer, nullable=False)
    price: Mapped[float] = mapped_column(Float, nullable=False)

    product = relationship("Product", back_populates="carts")



from config import MYSQL_URL
engine = create_async_engine(MYSQL_URL, echo=True)
async_session = async_sessionmaker(engine, expire_on_commit=False)

async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all) 