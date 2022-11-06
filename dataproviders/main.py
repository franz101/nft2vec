#!/usr/bin/env python3

import requests
from ast import arg
import http.client
import sys
import os
import time
import grpc
import sys
import base64
import csv

# import pandas as pd
from google.protobuf.json_format import MessageToDict

from sf.substreams.v1 import substreams_pb2_grpc
from sf.substreams.v1.substreams_pb2 import Request, STEP_IRREVERSIBLE
from sf.substreams.v1.substreams_pb2 import ModuleOutput
from sf.substreams.v1.package_pb2 import Package
from sf.substreams.v1 import erc721_pb2


API_KEY = os.getenv("SUBSTREAMS_API_KEY")
r = requests.post(
    "https://auth.streamingfast.io/v1/auth/issue", json={"api_key": API_KEY}
).json()
jwt_token = r.get("token")
if not jwt_token:
    raise Error("set SUBSTREAMS_API_TOKEN")
endpoint = "api.streamingfast.io:443"
package_pb = "substreams-erc721-transfers-v0.1.0.spkg"
output_modules = ["map_transfers"]
start_block = 12369621
end_block = 0


def substreams_service():
    credentials = grpc.composite_channel_credentials(
        grpc.ssl_channel_credentials(),
        grpc.access_token_call_credentials(jwt_token),
    )
    channel = grpc.secure_channel(endpoint, credentials=credentials)
    return substreams_pb2_grpc.StreamStub(channel)


def main():
    all_transfers = []
    with open(package_pb, "rb") as f:
        pkg = Package()
        pkg.ParseFromString(f.read())

    service = substreams_service()
    stream = service.Blocks(
        Request(
            start_block_num=start_block,
            stop_block_num=end_block,
            fork_steps=[STEP_IRREVERSIBLE],
            modules=pkg.modules,
            output_modules=output_modules,
        )
    )

    counter = 0
    for response in stream:
        # progress message
        if response.progress:
            data = (
                MessageToDict(response.data)
                .get("outputs", [{}])[0]
                .get("mapOutput", {})
            )
        else:
            continue
        transfers = data.get("transfers", [])
        if transfers:
            all_transfers += transfers
        if len(all_transfers) > 10:
            # convert array of dicts to csv
            with open(f"./data/transfers_{counter}.csv", "w") as file:
                writer = csv.writer(file)
                for row in all_transfers:
                    writer.writerow(row.values())
            counter += 1
            all_transfers = []
            print("saving data", counter)


main()
