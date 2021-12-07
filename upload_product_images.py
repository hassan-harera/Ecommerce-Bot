from firebase import Firebase
import pyrebase
import pandas as pd
import os

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


def find_files(filename, search_path):
    result = []

    for root, dir, files in os.walk(search_path):
        if filename in files:
            result.append(os.path.join(root, filename))
    return result[0]


products = pd.read_csv("products.csv")
print(len(products))
productId = 130002

for product in range(1, 315):
    try:
        # print(products.iloc[product, 1])

        path = find_files("1300 (" + product.__str__() +")" + ".jfif", "C://Users//Harera//PycharmProjects//HyperPanda//data")
        print("/data/", str(products.iloc[product, 1]) + ".jfif")

        storage.child("Products") \
            .child(str(productId)) \
            .child(str(productId) + ".jfif") \
            .put(path)

        print(productId)
    except:
        continue
    finally:
        productId += 1
