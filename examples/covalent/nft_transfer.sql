SELECT from,to,token_id,collection_address , nft_token_price_usd  ,gas_eth,block_height                                                  
        FROM reports.nft_sales_all_chains
        WHERE chain_name = 'eth_mainnet' AND block_height <= {block_end}
        AND block_height > {block_start}
        ORDER BY block_height DESC
LIMIT 10000