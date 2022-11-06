import os
import requests


BEARER_TOKEN = os.environ.get("COVALENT_BEARER_TOKEN")
API_URL = os.environ.get("COVALENT_API_URL")
BASE_PATH = os.environ.get("BASE_PATH")

header = {
    "accept": "*/*",
    "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
    "authorization":f"Bearer {BEARER_TOKEN}",
    "content-type": "text/plain;charset=UTF-8",
    "sec-ch-ua": "\"Google Chrome\";v=\"107\", \"Chromium\";v=\"107\", \"Not=A?Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site"
  }


def fetch_query(query):
    r = requests.post(API_URL,
            json={'query': query,'date_aggregation': 'daily',
        'date_range': 'this_month',
        'chain_filter': [],
        'query_id': '5565513579795864-8618575045876991'},
        headers=header,
            cookies={},
            auth=(),
        )
    d = r.json()
    df = pd.DataFrame(d.get("data").get("data").get("data"))
    return df



def fetch_all_nfts(block_end = 15907431):
    while True:
        block_start = block_end - 500000
        query = f"""
        SELECT hex(tx_hash) AS th, hex(from) AS f ,hex(to)  AS t ,token_id AS tid ,hex(collection_address) AS ca, nft_token_price_usd  AS usd,gas_eth AS gas,block_height as ts                                               
                FROM reports.nft_sales_all_chains
                WHERE chain_name = 'eth_mainnet' AND block_height <= {block_end}
                AND block_height > {block_start}
                ORDER BY block_height DESC
        LIMIT 10000
        """
        df = fetch_query(query)
        if len(df) == 0:
            block_end - 100
            continue
        dff = df[df["th"]==last_hash].index
        if len(dff)>0:
        df = df[dff.max() + 1:]
        df.to_parquet(f"{BASE_PATH}/block_{block_end}.parquet")
        block_end = df["ts"].astype(int).min() + 1
        last_hash = df["th"].iloc[-1]
        print(block_end,len(df))