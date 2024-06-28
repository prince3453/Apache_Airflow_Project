from airflow.hooks.base import BaseHook
import requests
import json
<<<<<<< HEAD
from minio import Minio
from io import BytesIO

=======
>>>>>>> 14223c4bdebb44c0219a19f80c468222a1fce92e
def _get_stock_prices(url, symbol):
    url = f'{url}{symbol}?metrics=high?&interval=1d&range=3y'
    api = BaseHook.get_connection('stock_api')
    response = requests.get(url, headers=api.extra_dejson['headers'])
<<<<<<< HEAD
    return json.dumps(response.json()['chart']['result'][0])

def _store_prices(stock):
    minio = BaseHook.get_connection('minio')
    client = Minio(
        endpoint = minio.extra_dejson['endpoint_url'].split('//')[1],
        access_key = minio.login,
        secret_key = minio.password,
        secure =False
    )
    bucket_name = 'stock-market'
    if not client.bucket_exists(bucket_name):
        client.make_bucket(bucket_name)
    stock = json.loads(stock)
    symbol = stock['meta']['symbol']

    data = json.dumps(stock, ensure_ascii=False).encode('utf-8')

    objwrite = client.put_object(
        bucket_name = bucket_name,
        object_name = f'{symbol}/prices.json',
        data = BytesIO(data),
        length = len(data)
    )

    return f'{objwrite.bucket_name}/{symbol}'
=======
    return json.dumps(response.json()['chart']['result'][0])
>>>>>>> 14223c4bdebb44c0219a19f80c468222a1fce92e
