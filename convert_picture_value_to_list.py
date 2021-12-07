import pandas as pd

df = pd.read_csv("products_out/products_out.csv",
                 names=["price", "title", "productId", "amount", "productPictureUrls", "unit", "categoryName"])

productPictureUrls = df["productPictureUrls"]
new_productPictureUrls = []
for url in range(0, len(df)):
    productPictureUrls[url] = [productPictureUrls[url]]

df["productPictureUrls"] = productPictureUrls

for property in df.columns:
    print(df[property])
    print("----------------------")

compression_opts = dict(method='zip', archive_name='products_out.csv')
df.to_csv('products_out.zip', index=False, compression=compression_opts)
