import pandas as pd
import os

df = products = pd.read_csv("products.csv", names=["price", "title", "extra_price"])
df = products.drop("extra_price", axis=1)
products.to_csv("products_out.zip", index=False)

print(products.shape)

compression_opts = dict(method='zip',
                        archive_name='products_out.csv')
df.to_csv('products_out.zip', index=False,
          compression=compression_opts)
