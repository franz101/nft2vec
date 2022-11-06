
function sftoken {
    export FIREHOSE_API_TOKEN=$(curl https://auth.streamingfast.io/v1/auth/issue -s --data-binary '{"api_key":"'$STREAMINGFAST_KEY'"}' | jq -r .token)
    export SUBSTREAMS_API_TOKEN=$FIREHOSE_API_TOKEN
    echo Token set on FIREHOSE_API_TOKEN and SUBSTREAMS_API_TOKEN
}
sftoken
#substreams run -e api-dev.streamingfast.io:443 substreams.yaml map_transfers --start-block 12292922 --stop-block +1
substreams run -e api-dev.streamingfast.io:443 substreams.yaml store_transfers --start-block 12292922
