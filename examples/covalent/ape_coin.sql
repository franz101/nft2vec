SELECT 
  block_height,
 to_float64_raw(data0) AS amount,
  extract_address(hex(topic1)) AS from,
  extract_address(hex(topic2)) AS to
             FROM blockchains.all_chains 
       WHERE 
       chain_name = 'eth_mainnet'
        AND log_emitter = unhex('4d224452801ACEd8B2F0aebE155379bb5D594381')
 AND topic0 = unhex('ddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef')
 AND block_height <= {block_end}
        AND block_height > {block_start}
        ORDER BY block_height DESC
LIMIT 10000