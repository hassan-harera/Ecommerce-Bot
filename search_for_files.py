import pandas as pd
import os


def find_files(filename, search_path):
    result = []

    for root, dir, files in os.walk(search_path):
        if filename in files:
            result.append(os.path.join(root, filename))
    return result[0]


products = pd.read_csv("products.csv")
for product in range(0, len(products)):
    print(products.iloc[product, 1])
    path = find_files(products.iloc[product, 1] + ".jfif", "C://Users//Harera//PycharmProjects//HyperPanda//data")
    print(path)
