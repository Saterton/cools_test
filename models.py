from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Product(Base):
    __tablename__ = 'product'

    id = Column(String, primary_key=True)
    title = Column(String)
    sku_number = Column(String)
    url = Column(String)
    image_url = Column(String)
    buy_url = Column(String)
    description = Column(String)
    discount = Column(String)
    discount_type = Column(String)
    currency = Column(String)
    retail_price = Column(String)
    sale_price = Column(String)
    brand = Column(String)
    manufacture = Column(String)
    shipping = Column(String)
    availability = Column(String)
    sizes = Column(String)
    materials = Column(String)
    colors = Column(String)
    style = Column(String)
    gender_group = Column(String)
    age_group = Column(String)

    def __str__(self):
        return self.id
