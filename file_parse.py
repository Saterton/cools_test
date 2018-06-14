import os
from xml.etree import ElementTree

import settings
from database import Session, engine
from models import Product, Base
from utils import get_attr_text

Base.metadata.create_all(engine)


class FileParse:
    def __init__(self, filename, delimiter='|'):
        self.filename = filename
        self.delimiter = delimiter
        self.session = Session()
        self.data = dict()
        self.products = list()

    @property
    def file_extension(self):
        return os.path.splitext(self.filename)[1]

    def __clear_data(self):
        self.data = dict()

    def __clear_products(self):
        self.products = list()

    def __session_commit(self):
        self.session.bulk_save_objects(self.products)
        self.session.commit()

    def __default_parse(self):
        with open(self.filename) as file:
            for line in file:
                if line.startswith('HDR') or line.startswith('TRL'):
                    continue
                lst = line.split(self.delimiter)
                item_data = {key: value for key, value in zip(settings.TXT_PARAMS, lst)}
                self.data[item_data.get('id')] = item_data

        self.update_products()

    def __xml_parse(self):
        tree = ElementTree.parse(self.filename)
        root = tree.getroot()
        for item_data_parse in root.findall('item_data'):
            item_data = dict()
            item_basic_data = item_data_parse.find('item_basic_data')
            for key, value in settings.XML_PARAMS:
                item_data[key] = get_attr_text(item_basic_data, value)
            self.data[item_data.get('id')] = item_data
        self.update_products()

    def update_products(self):
        self.products = self.session.query(Product).filter(Product.id.in_(self.data.keys())).all()
        for product in self.products:
            item_data = self.data.pop(product.id)
            for key, value in item_data.items():
                setattr(product, key, value)
        for value in self.data.values():
            product = Product(**value)
            self.products.append(product)

    def parse(self):
        self.__clear_data()
        self.__clear_products()
        if self.file_extension == '.xml':
            self.__xml_parse()
        else:
            self.__default_parse()
        self.__session_commit()
