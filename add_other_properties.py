import pandas as pd
import os
import numpy as np

df = products = pd.read_csv("products_out.csv", names=["price", "title", "productId", "amount"])

productsUrls = []
for i in range(130001, 130001 + len(products)):
    productsUrls.append(
        "https://firebasestorage.googleapis.com/v0/b/ecommerce-55b58.appspot.com/" + "o/Products%2F" + str(
            i) + "%2F" + str(i) + ".jfif?alt=media&token=d8e32727-6c2f-42d6-acc0-df967d04bf0c"
    )

print(productsUrls[5])

df["productId"] = np.array([productId for productId in range(130000, 130000 + len(products))])
df["amount"] = np.full((len(products), 1), 1)
df["productPictureUrls"] = np.array(productsUrls)
df["unit"] = np.full((len(products), 1), "كيلو")

cats = []
for i in range(0, len(products)):
    print(products.iloc[i, 1])
    print(list(set(cats)))
    cat = input()
    cats.append(cat)

df["categoryName"] = np.array(cats)
compression_opts = dict(method='zip', archive_name='products_out.csv')
df.to_csv('products_out.zip', index=False, compression=compression_opts)
