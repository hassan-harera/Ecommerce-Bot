from firebase import Firebase
import pyrebase
import pandas as pd
import os
import urllib.request as req
from dataclasses import dataclass
from dataclass_csv import DataclassReader
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import storage
from google.cloud import storage
import json
import dataclasses

config = {
    "apiKey": "AIzaSyD067FAA98I17gvHxINUNmjo4GeObS2DSQ",
    "authDomain": "ecommerce-55b58.firebaseapp.com",
    "databaseURL": "https://ecommerce-55b58.firebaseio.com",
    "projectId": "ecommerce-55b58",
    "storageBucket": "ecommerce-55b58.appspot.com",
    "messagingSenderId": "261802668850",
    "appId": "1:261802668850:web:9498c1b1cfcea546b0dd2b",
    "measurementId": "G-S9R28RVJS9"
}

app = pyrebase.initialize_app(config)
storage = app.storage()

cred = credentials.Certificate('private_key.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

products = pd.read_csv("products.csv")
print(len(products))
productId = 130000
exts = [".jfif", ".jpg", ".jpeg", ".png"]

id = 130001
for i in range(0, 315):
    doc_ref = db.collection("Products").document((productId - 1).__str__()).update({
        "productPictureUrls":
            [
                f"https://firebasestorage.googleapis.com/v0/b/ecommerce-55b58.appspot.com/o/Products%2F{productId}%2F{productId}{ext}?alt=media&token=a18ed230-0c54-41e0-a2a6-a695ad3515d2"]
    }
    )

while (True):
    for ext in exts:
        path = find_files(f"{productId}{ext}",
                          "C://Users//Harera//Downloads//hyper//")
        if (len(path) > 0):
            doc_ref = db.collection("Products").document((productId - 1).__str__()).update({
                "productPictureUrls":
                    [
                        f"https://firebasestorage.googleapis.com/v0/b/ecommerce-55b58.appspot.com/o/Products%2F{productId}%2F{productId}{ext}?alt=media&token=a18ed230-0c54-41e0-a2a6-a695ad3515d2"]
            }
            )
            print(
                productId
                # f"https://console.firebase.google.com/u/0/project/ecommerce-55b58/storage/ecommerce-55b58.appspot.com/files/~2FProducts~2F{productId}"
            )

            # storage.child("Products") \
            #     .delete(str(productId)) \
            #     .child(str(productId) + ext) \
            #     .put(path[0])
            #
            # storage.child("Products") \
            #     .child(str(productId)) \
            #     .child(str(productId) + ext) \
            #     .put(path[0])

    productId += 1
