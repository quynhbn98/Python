# working with xlsx real data
# Check tiki sample data set here https://drive.google.com/drive/u/0/folders/1Q9bdWfxi9j4jjqFAJ7vhYDSdq5SO-FjA
# Input file: "Áo Croptop Nữ.xlsx"
# Output:
# Ex2. Sum total price of all product in this category
# Ex3. Get product name, product_id is best sale in this category (largest number of sold items)
# Ex4. Get shop id is best seller (have largest number of sold items)
# EX5. Get shop id have largest money (total money of sold and remain items in shop)

import pandas as pd

FILEPATH = r'C:\Users\QUYNHBN2\Desktop\python\Thời trang - Phụ kiện\Áo Croptop Nữ.xlsx'

df = pd.read_excel (FILEPATH)
df['total_unit'] = df['unit_sold'] + df['unit_remain']
df['money'] = df['total_unit'] * df['price']
sum_by_prod = df.groupby(['shop_id','prod_id','name']).agg({'unit_sold':'sum','money':'sum','price':'mean'})

# EX2
total_price = sum_by_prod['price'].sum()
print('total_price:', total_price)

# EX3
max_sold_by_prod = sum_by_prod['unit_sold'].max()
best_sale_prod_id = sum_by_prod[sum_by_prod['unit_sold'] == max_sold_by_prod].index.values[0][1]
best_sale_prod_name = sum_by_prod[sum_by_prod['unit_sold'] == max_sold_by_prod].index.values[0][2]
# print(max_sold_by_prod)
print('best_sale_prod_id:', best_sale_prod_id)
print('best_sale_prod_name:', best_sale_prod_name)

#EX4, 5
sum_by_shop = sum_by_prod.groupby('shop_id').agg({'unit_sold':'sum','money':'sum'})
max_sold_by_shop = sum_by_shop['unit_sold'].max()
max_money_by_shop = sum_by_shop['money'].max()
best_sale_shop = sum_by_shop[sum_by_shop['unit_sold'] == max_sold_by_shop].index.values[0]
best_money_shop = sum_by_shop[sum_by_shop['money'] == max_money_by_shop].index.values[0]
print('best_sale_shop:', best_sale_shop)
print('best_money_shop:', best_money_shop)
# print(best_sale_shop)

# shop_unit_sold = df.groupby('shop_id').sum()
# shop_max_sold = shop_unit_sold['unit_sold'].max()
# best_shop = shop_unit_sold[shop_unit_sold['unit_sold'] == shop_max_sold].index.values[0]
# print(best_sale_shop_id)