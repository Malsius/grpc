python -m grpc_tools.protoc -I./protos/ --python_out=./unsecure/ --grpc_python_out=./unsecure/ ./protos/crypto.proto