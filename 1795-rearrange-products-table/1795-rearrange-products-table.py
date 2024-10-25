import pandas as pd

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    # use melt bc changing what the rows represnt
    products = products.melt(
        id_vars=['product_id'],
        value_vars=["store1", "store2", "store3"], 
        var_name="store", 
        value_name = "price"
    )
    # delete null rows 
    return products.dropna(axis=0)
    # return products
    