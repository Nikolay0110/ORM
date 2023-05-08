import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base() # Создание класса из библиотеки SQLAlchemy



# Создаем класс издателей
class Publisher(Base):
    __tablename__ = 'publisher'

    id = Column(Integer, primary_key=True)
    name = Column(String(length=60), unique=True, nullable=False)



# Создаем класс книг
class Book(Base):
    __tablename__ = 'book'

    id = Column(Integer, primary_key=True)
    title = Column(String(length=60), unique=True, nullable=False)
    publisher_id = Column(Integer, ForeignKey('publisher.id'))

    publisher = relationship(Publisher, backref='book')



# Создаем класс магазинов
class Shop(Base):
    __tablename__ = 'shop'

    id = Column(Integer, primery_key=True)
    shop_name = Column(String(length=60), nullable=False)



# Создаем класс Товарного запаса
class Stock(Base):
    __tablename__ = 'stock'

    id = Column(Integer, primery_key=True)
    book_id = Column(Integer, ForeignKey('book.id'))
    shop_id = Column(Integer, ForeignKey('shop.id'))
    count = Column(Integer, nullable=False)

    book = relationship(Book, backref='stock')
    shop = relationship(Shop, backref='stock')



# Создаем класс продаж
class Sale(Base):
    __tablename__ = 'sale'

    id = Column(Integer, primery_key=True)
    price = Column(Integer, nullable=False)
    date_sale = Column(DateTime, nullable=False)
    stock_id = Column(Integer, ForeignKey('stock.id'))
    count_sale = Column(Integer, nullable=False)

    stock = relationship(Stock, backref='sale')


# Создаем функцию
def create_tables(engine):
    Base.metadata.cteate_all(engine) # Так же можно удалить все - Base.metadata.drop_all(engine)

DSN = 'postgresql://postgres:1604@localhost:5432/orm'
engine = sqlalchemy.create_engine(DSN)

Session = sessionmaker(bind=engine)
session = Session()

session.close()

