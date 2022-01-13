import pandas as pd
import requests
import time
import random

OUTPUT_FILE = "crawl_tiki_output.csv"
URL = 'https://tiki.vn/api/personalish/v1/blocks/listings'

def get_data(api, category, page):
    params = {
        'limit': 100,
        'category': category,
        'page': page
    }
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'max-age=0',
        'sec-ch-ua': '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
    }
    r = requests.get(url = api, headers = headers, params = params)
    
    data = r.json()["data"]
    result = []
    for i in range(len(data)):
        data_item = {}
        options = data[i]["option_color"]
        data_item["name"] = data[i]["name"]
        data_item["category"] = 'Áo croptop nữ'
        data_item["brand"] = data[i]["brand_name"]
        data_item["price"] = data[i]["price"]
        if data[i]["quantity_sold"] is None:
            data_item["unit_sold"] = data[i]["quantity_sold"]
        else:
            data_item["unit_sold"] = ""
        data_item["unit_remain"] = data[i]["stock_item"]["qty"]
        data_item["prod_id"] = data[i]["id"]
        data_item["variation"] = []
        if len(options) >0:
            for j in options:
                data_item["variation"].append(j["display_name"])
        result.append(data_item)
    
    return result

final_data = []
for i in range(1,100):
    a = get_data(URL, 10389,i)
    final_data = [*final_data, *a]
    df = pd.DataFrame(final_data)
    if i == 0: df.to_csv(OUTPUT_FILE, index=True)
    else: df.to_csv(OUTPUT_FILE, mode = 'a', header=False)
    print('ok', i)
    time.sleep(random.randrange(5,20))

