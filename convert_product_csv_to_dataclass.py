from dataclasses import dataclass
from dataclass_csv import DataclassReader
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import storage
from google.cloud import storage
import json
import dataclasses


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


cred = credentials.Certificate('private_key.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

with open("products_out/products_out.csv", encoding="utf8") as products:
    reader = DataclassReader(products, Product)
    for product in reader:
        product.productPictureUrls = [product.productPictureUrls]
        # print(json.dumps(dataclasses.asdict(product)))
        doc_ref = db.collection("Products").document(product.productId).set({
            "price": product.price,
            "title": product.title,
            "productId": product.productId,
            "productPictureUrls": product.productPictureUrls,
            "amount": product.amount,
            "unit": product.unit,
            "categoryName": product.categoryName,
        })
