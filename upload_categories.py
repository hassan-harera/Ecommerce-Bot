from dataclasses import dataclass
from dataclass_csv import DataclassReader
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import storage
from google.cloud import storage
import json
import dataclasses
import pandas as pd
import numpy as np
import urllib
import requests


#
# import urllib.request
# local_filename, headers = urllib.request.urlretrieve('http://python.org/')
# html = open(local_filename)
# html.close()

class EnhancedJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if dataclasses.is_dataclass(o):
            return dataclasses.asdict(o)
        return super().default(o)


@dataclass
class Product:
    price: float
    title: str
    productId: str
    amount: float
    productPictureUrls: str
    unit: str
    categoryName: str = ""


@dataclass
class Category:
    categoryName: str
    categoryImagerUrl: str


cred = credentials.Certificate('private_key.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

start = 1
products = db.collection("Products").get()
for product in products:
    img_data = requests.get(product.get("productPictureUrls")[0]).content
    with open(f'{start}.jpg', 'wb') as handler:
        handler.write(img_data)
    start += 1
# with open("categories_out.csv", encoding="utf8") as categories_out:
#     reader = DataclassReader(categories_out, Category)
#     for cat in reader:
#         doc_ref = db.collection("categories").document(cat.categoryName).set({
#             "categoryName": cat.categoryName,
#             "categoryImagerUrl": cat.categoryImagerUrl,
#         })

# categories_out = pd.read_csv("categories_out.csv", names=["categoryName", "categoryImagerUrl"], encoding="utf8")
# categories = pd.read_csv("products_out/products_out.csv").iloc[:, 6]
# categories = (set(categories))
# print(categories_out.iloc[:,0])

# compression_opts = dict(method='zip',
#                         archive_name='categories_out.csv')
# pd.DataFrame(categories_out).to_csv('categories_out.zip', index=False,
#           compression=compression_opts)
#
# reader = DataclassReader(categories_out, Category)
# for cat in reader:
#     doc_ref = db.collection("categories").document(cat.categoryName).set({
#         "categoryName": cat.categoryName,
#         "categoryImagerUrl": cat.categoryImagerUrl,
#     })

# with open("products_out/products_out.csv", encoding="utf8") as products:
#     reader = DataclassReader(products, Product)
#     for product in reader:
#         product.productPictureUrls = [product.productPictureUrls]
#         # print(json.dumps(dataclasses.asdict(product)))
#         doc_ref = db.collection("Products").document(product.productId).set({
#             "price": product.price,
#             "title": product.title,
#             "productId": product.productId,
#             "productPictureUrls": product.productPictureUrls,
#             "amount": product.amount,
#             "unit": product.unit,
#             "categoryName": product.categoryName,
#         })
