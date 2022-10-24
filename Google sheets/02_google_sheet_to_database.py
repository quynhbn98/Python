import requests as res
import jaydebeapi
import random
import time
import pandas as pd
from tqdm import tqdm
import gg_func_google as gg
from datetime import datetime

def coalesce(*values):
    return next((v for v in values if v is not None and v != ''), '')

# Setup impala connection
conn = jaydebeapi.connect(
    "com.cloudera.impala.jdbc41.Driver",
    "jdbc:impala://host:port/;AuthMech=1;KrbRealm=;KrbHostFQDN=impala-proxy;KrbServiceName=impala;REQUEST_POOL='root.tmp'",
    {},
    'D:/ImpalaJDBC41.jar'
    )
curs = conn.cursor()
print('done connect impala')

# Read record tracking file
record_log = pd.read_csv(r'label_record_tracking.csv')
last_row = record_log.last_row.to_list()[-1] 
print('last row:', last_row)

# Read verified data from google sheet
FILE_READ_ID = 'my_sheet_id' 
RANGE_READ = 'Data!A{}:AD'
data = gg.google_sheet_read(FILE_READ_ID, RANGE_READ.format(last_row+1))

# upsert data in batch, 100 records each
print(data[0])
rows_insert = "{}"
for r, row in enumerate(tqdm(data, desc = 'Upsert sp  ', ascii=False, ncols=75)):
    while len(row) <25: row.append('')
    id              = int(row[9])
    shop_order      = int(row[1])
    shop_name       = row[11]
    product_id      = int(row[2])
    product_name    = row[12].replace('{','').replace('}','')
    suggest_top_1   = row[18].lower()
    suggest_top_2   = row[21].lower()
    suggest_top_3   = row[22].lower()
    suggest_top_4   = row[23].lower()
    suggest_top_5   = row[24].lower()
    suggest_top_6  = row[13].lower() if row[14] == 'TRUE' else ''
    suggest_top_7  = row[15].lower() if row[16] == 'TRUE' else ''
    picked_label   = coalesce(suggest_top_1, suggest_top_2, suggest_top_3, suggest_top_4, suggest_top_5, suggest_top_6, suggest_top_7)
    assign         = row[10]

    value = (id, shop_order, shop_name, product_id, product_name, picked_label, suggest_top_1, suggest_top_2, suggest_top_3, suggest_top_4, suggest_top_5, suggest_top_6, suggest_top_7, assign)
    
    if r % 100 != 99:
        rows_insert = rows_insert.format(value) + ',' + '{}'
    if r % 100 == 99 or r == len(data)-1:
        rows_insert = rows_insert.format(value)
        curs.execute("""
            upsert into table test.product_label_data_verified values {}""".format(rows_insert)
        )
        rows_insert = "{}"
        time.sleep(random.randrange(1,3))  