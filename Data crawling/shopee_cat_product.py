import requests as re
import pandas as pd
import time
import random

OUTPUT_FILE = r'D:\quynhbn\Python\shopee_cat_product.csv'
API = 'https://shopee.vn/api/v4/search/search_items'
# # limit=100&category=10389&page=1'

shopee_cat = pd.read_csv('shopee_cat.csv')

def get_data(api, match_id, limit):
    params = {
        'by': 'relevancy',
        'limit': limit,
        'match_id': match_id
    }
    headers = {
        # '': 'authority:tiki.vn',
        # '': 'method:GET',
        # '': 'path:/api/personalish/v1/blocks/listings?limit=100&category=10389&page=1',
        # '': 'scheme:https',
        'accept': 'application/json',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'af-ac-enc-dat': 'AAUyLjEuMAAAAYAwMZYJAAAAAAI2AAAAAAAAAAD0QDTiApo7K9b1Yi6qzNTIsR2nEMbd+CSU3o1v3k+PcDDRkVHTMLvQhLGsv5yRcyEhF4Oa+0PGY81qnJbOwR1diYS9AwubYjooGNt/nB3zpyxMVkBMYvkTeckraLKIAyDSI7092SfGhXJadGJP91nidNYqrrDqMjmOsNifLGPDMZFjs4yw8pGWNnYQjtmnppYSS3CJCxVfHuOyc4FxDHHr48UdRhhbhIVgU+IFUyU01vsYaXtvIkt86xLca56jgoolAwchz2hp3UGCZPaQOWsgoEQSSK14GUVdTw2jtH9bbYWKsIHCPk4Kosz6l73FF2UR5+QqWsYDJ69sIDUI+MqjlEjEw9Ydq1zcMnGstvGdov5/Fc0jLua+QrrfDcvGmBPg43/xbQ/ylUBuGExCpgyGzeeiEX4wKeGzAITeglfAelSsueLmKhf+ihUrESbIpbeaGl0E6iSASK8uY258wCvok4w5Rk+rTYiCwgjMbeIk8oWKsIHCPk4Kosz6l73FF2XOP6/Gz8NFEsMCPUNctXUQkWOzjLDykZY2dhCO2aemlvehiJf6OllW/EgYrZ8LIcBs31SSvVP/kPthlvp+6TRTELeruvsCa78VxL9+LBAisp19woNaGimWAFXXqWvysMW8biT/bF2Qz3xOu02whZpd4kj5GWwL23RikVk6Uu7NHnq99eqbDyZsbg7QwMeUDHij/Zm2AkrMuFi1hf2Ifj+QqOdk2mvItkQwyQJac9YQx8i4sqPra+MfXXhKFMWah28=',
        'content-type': 'application/json',
        'cookie': '__LOCALE__null=VN; csrftoken=4bRiYkkvUryqlzgF1Utjv2HCBwpFkQqg; REC_T_ID=a66a6af6-bca2-11ec-a645-3c15fb3af0b5; SPC_F=t050lDuSRPHU8KDxmH23TEfW0m8MB6g2; SPC_IA=-1; SPC_EC=-; SPC_U=-; SPC_SI=qk88YgAAAAB5SzE5WlFkMvrAkQEAAAAAbXVMUlVYMmY=; _QPWSDCXHZQA=1550bbb4-980a-456b-a9fc-7036c9478d79; _gcl_au=1.1.1499439022.1650016761; _fbp=fb.1.1650016761635.763999754; _gid=GA1.2.1260041105.1650016762; _hjSessionUser_868286=eyJpZCI6IjZmYTVjZWUxLWRmOTUtNTY5ZS1hMDdhLTJiMDA0Y2FhN2RhNyIsImNyZWF0ZWQiOjE2NTAwMTY3NjI0MjEsImV4aXN0aW5nIjp0cnVlfQ==; SPC_T_IV="s7veW2Pk4NPhza+vCLv0fw=="; SPC_T_ID="oEu7Iiq+QhBZDNxAWOpqosl2muoW5fShbtM6Lgi5tr/NUf1inKktw+VM6Q3weuP5TE8MBMGx9De5vNzBMVHC6e8bjw+g8u9KnaWaUrzK/hU="; SPC_R_T_ID=oEu7Iiq+QhBZDNxAWOpqosl2muoW5fShbtM6Lgi5tr/NUf1inKktw+VM6Q3weuP5TE8MBMGx9De5vNzBMVHC6e8bjw+g8u9KnaWaUrzK/hU=; SPC_R_T_IV=s7veW2Pk4NPhza+vCLv0fw==; SPC_T_ID=oEu7Iiq+QhBZDNxAWOpqosl2muoW5fShbtM6Lgi5tr/NUf1inKktw+VM6Q3weuP5TE8MBMGx9De5vNzBMVHC6e8bjw+g8u9KnaWaUrzK/hU=; SPC_T_IV=s7veW2Pk4NPhza+vCLv0fw==; _ga_M32T05RVZT=GS1.1.1650075995.3.1.1650075997.58; _hjIncludedInPageviewSample=1; _hjSession_868286=eyJpZCI6ImQyZTBlYmQ5LTk2NGQtNDRlNS1iNjlmLTVjNDU5YzFiZWIyYiIsImNyZWF0ZWQiOjE2NTAwNzU5OTc5NDUsImluU2FtcGxlIjp0cnVlfQ==; _hjAbsoluteSessionInProgress=0; AMP_TOKEN=%24NOT_FOUND; _ga=GA1.2.451523404.1650016762; _dc_gtm_UA-61914164-6=1; cto_bundle=Z6TWiF9RZllCSWEyWXZHd1ppMVNZd2hmRHRSUjUzTE5UeXIzemJka0RlT0dYM0NjNzBabGlhcGozaldlcmRFVHJxczhIWHdzeVYlMkJ4Rk4lMkJLc1dza0d2d0tVT2oxdjRseCUyRjB1T0czcm14c1Q3czV4RnNnQmduM1hSSkdqeWRzenhnaGlTVURuYkU4bzRkSFNwWlRDWHE5dXhyUFElM0QlM0Q; shopee_webUnique_ccd=zQYWgdw9K%2FSbFz6lDShqNQ%3D%3D%7CYPfZvWZjnl7AoZsUm3MQiW2QpBK%2BezGDF%2FJ%2B7qqXRrw4CaY7h4BEENtjR8Pq%2FRJU6LYNH%2BCqBKea4J25CA17%7CTTs%2BaiGVBMyVxyVV%7C04%7C3',
        # 'referer': 'https://shopee.vn/Gi%C3%A0y-D%C3%A9p-N%E1%BB%AF-cat.11035825',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Microsoft Edge";v="100"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'sz-token': 'zQYWgdw9K/SbFz6lDShqNQ==|YPfZvWZjnl7AoZsUm3MQiW2QpBK+ezGDF/J+7qqXRrw4CaY7h4BEENtjR8Pq/RJU6LYNH+CqBKea4J25CA17|TTs+aiGVBMyVxyVV|04|3',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36 Edg/100.0.1185.39'
    }
    r = re.get(url = api, headers = headers, params = params)
    items = r.json()['items']
    
    null = ''
    false = False
    true = True
    
    match_ids = []
    by = []
    item_type = []
    foody_item = []
    name = []
    catid = []
    is_category_failed = []
    
    for item in items:
        match_ids.append(match_id)
        by.append('relevancy')
        item_type.append(item['item_type'])
        foody_item.append(item['foody_item'])
        name.append(item['item_basic']['name'])
        catid.append(item['item_basic']['catid'])
        is_category_failed.append(item['item_basic']['is_category_failed'])

    result = pd.DataFrame(list(zip(match_ids, by, item_type, foody_item, catid, is_category_failed, name)),
               columns =['match_ids', 'by', 'item_type', 'foody_item', 'catid', 'is_category_failed', 'name'])
    return result

for cat in shopee_cat.catid.to_list():
    time.sleep(random.randrange(5,20))
    df = get_data(API, cat, 100)
    # with open(OUTPUT_FILE, mode='a') as f:
    df.to_csv(OUTPUT_FILE, mode='a',header=0)
    print('ok', cat)

