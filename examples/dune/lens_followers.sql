
SELECT *
FROM (
SELECT et."contract_address" as followed, et.to as follower, lf.call_block_time as call_block_time
FROM lens."LensHub_call_followWithSig" lf
LEFT JOIN erc721."ERC721_evt_Transfer" et ON et."evt_tx_hash"="call_tx_hash"
WHERE "call_success" = True
and lf.call_block_time >= '2022-04-01 00:00'
UNION
SELECT et."contract_address" as followed2,  et.to as follower, lf2.call_block_time as call_block_time
FROM lens."LensHub_call_follow" lf2
LEFT JOIN erc721."ERC721_evt_Transfer" et ON et."evt_tx_hash"="call_tx_hash"
WHERE "call_success" = True
and lf2.call_block_time >= '2022-04-01 00:00'