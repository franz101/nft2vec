PKG=./substreams-erc721-transfers-v0.1.0.spkg
alias protogen_py="python -m grpc_tools.protoc --descriptor_set_in=$PKG --python_out=. --grpc_python_out=."

protogen_py sf/substreams/v1/substreams.proto
protogen_py sf/substreams/v1/package.proto
protogen_py sf/substreams/v1/modules.proto
protogen_py sf/substreams/v1/clock.proto
python -m grpc_tools.protoc --descriptor_set_in=$PKG --python_out=sf/substreams/v1/ --grpc_python_out=sf/substreams/v1/ --proto_path proto/eth/v1 erc721.proto
unalias protogen_py