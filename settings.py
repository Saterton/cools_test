import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')

TXT_PARAMS = [
    "id",
    "title",
    "sku_number",
    "url",
    "image_url",
    "buy_url",
    "description",
    "discount",
    "discount_type",
    "currency",
    "retail_price",
    "sale_price",
    "brand",
    "manufacture",
    "shipping",
    "availability",
    "sizes",
    "materials",
    "colors",
    "style",
    "gender_group",
    "age_group"
]

XML_PARAMS = {
    'id': 'item_unique_id',
    'title': 'item_title',
    'sku_number': 'item_sku',
    'url': 'item_page_url',
    'image_url': 'item_image_url',
    'sale_price': 'item_price',
    'brand': 'item_brand'
}
