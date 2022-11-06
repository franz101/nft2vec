curl 'https://gateway.thegraph.com/api/540064f67791087737214d20f5982ccf/deployments/id/Qmccst5mbV5a6vT6VvJMLPKMAA1VRgT6NGbxkLL8eDRsE7' \
-X 'POST' \
-H 'Content-Type: application/json' \
-H 'Accept: application/json, multipart/mixed' \
-H 'Origin: https://thegraph.com' \
-H 'Referer: https://thegraph.com/' \
-H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6.1 Safari/605.1.15' \
--data-binary '{"query":"{\n  contracts(first: 5) {\n    id\n    asERC721 {\n      id\n    }\n  }\n  accounts(first: 5) {\n    id\n    tokens {\n      id\n    }\n    transfersFrom {\n      id\n    }\n    transfersTo {\n      id\n    }\n  }\n}"}'