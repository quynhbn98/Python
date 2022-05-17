from googleapiclient.discovery import build
from google.oauth2 import service_account
import requests as res
import jaydebeapi
import random
import time

# set up google api
#------------------------------------------------------------------
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = 'my_service_account_key.json'
SPREADSHEET_ID = 'my_sheet_id'

creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
service = build('sheets', 'v4', credentials=creds)
sheet = service.spreadsheets()

# set up trino connection
#------------------------------------------------------------------
conn = jaydebeapi.connect(
    "io.trino.jdbc.TrinoDriver",
    "jdbc:trino://trino.ghtk.vn:443/hive?&user=&password=&SSL=true",
    {},
    'D:/trino-jdbc-361.jar'
    )
curs = conn.cursor()

# read google sheet, get list shops having right suggest rate >= 95% to exclude from new data input
# ------------------------------------------------------------------
old_shop_range = 'old_shop!A:A'
result_shop = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                            range=old_shop_range).execute()
value_shop = result_shop.get('values', [])
exclude_shop = ''.join(i[0].join(', ') for i in value_shop[1:])

# read google sheet, get list product already labeled to exclude from new data input
# ------------------------------------------------------------------
product_range = 'products!C:C'
result_product = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                            range=product_range).execute()
value_product = result.get('values', [])
exclude_product = ''.join(i[0].join(', ') for i in value_product[1:])

# query to get new products, each shop get <= 20 products 
#------------------------------------------------------------------
curs.execute('''
    select * from (
        select *,
            row_number() over (partition by shop_order order by shop_order) rn
        from test.product_for_label_data 
        where shop_order not in (0{})
        and product_id not in (0{})
        ) t where rn <= 20
    order by shop_order
    limit 800
    '''.format(exclude_shop, exclude_product)
    )
print('done execute query')
data = curs.fetchall()
print('done fetchdata, record count:', len(data))
append_data = []

# call api suggest category for each product, write in google sheet (each batch 20 rows)
#------------------------------------------------------------------
for r, row in enumerate(data):
    apicall = res.get(
        url = r'http://domain/api/get_labels', 
        params = {
            'token' : 'my_token',
            'name' : row[3], 
            'top_label' : 5,
            'top_k_text' : 15,
            'top_k_word' : 1
        },
        headers = {'accept': 'application/json'}
    )
    suggest = apicall.json()

    if len(suggest) >0: suggest_name = [i["label"] for i in suggest['labels']]
    else: suggest_name = []
    
    while len(suggest_name) <5: suggest_name.append('')
    
    append_row = [
        row[0], #shop_order
        row[1], #shop_name
        row[2], #product_id
        row[3], #product_name
        suggest_name[0], #suggest_top_1
        suggest_name[1], #suggest_top_2
        suggest_name[2], #suggest_top_3
        suggest_name[3], #suggest_top_4
        suggest_name[4], #suggest_top_5
    ]
    
    append_data.append(append_row)

    if r % 20 == 19:
        request = sheet.values().update(
            spreadsheetId=SPREADSHEET_ID, 
            range = 'Data products!A{}'.format(r-19+2),
            valueInputOption = 'USER_ENTERED',
            body = {'values':append_data}
        )
        response = request.execute()
        append_data = []
        print(r)
        time.sleep(random.randrange(1,3))  


# read data
# result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
#                             range='Data ghtk!A1:A7').execute()
# values = result.get('values', [])
# print(values)

# update data
# request = sheet.values().update(
#     spreadsheetId=SPREADSHEET_ID, 
#     range = 'Nháp!A1',
#     valueInputOption = 'USER_ENTERED',
#     body = {'values':[['a','b'],['c']]}
#     )
# response = request.execute()

