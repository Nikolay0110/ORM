import json

import sqlalchemy
from sqlalchemy.orm import sessionmaker

from models import create_table, Publisher, Shop, Book, Stock, Sale

DSN = 'postgresql://postgres:1604@localhost:5432/orm'
engine = sqlalchemy.create_engine(DSN)
create_table(engine)

Session = sessionmaker(bind=engine)
session = Session()


def record_database():
    with open('tests_data.json', 'r') as fd:
        data = json.load(fd)

    for record in data:
        model = {
            'publisher': Publisher,
            'shop': Shop,
            'book': Book,
            'stock': Stock,
            'sale': Sale,
        }[record.get('model')]
        session.add(model(id=record.get('pk'), **record.get('fields')))
    session.commit()
