import grpc
import crypto_pb2
import crypto_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:50050') as channel:
        stub = crypto_pb2_grpc.CryptoStub(channel)
        number = int(input("Input a number : "))
        while True:
            response = stub.GetPlusOne(crypto_pb2.Request(number=number))
            print(f"Response from server : {response.number}")
            number = int(input("Input a number : "))


if __name__ == '__main__':
    try:
        run()
    except KeyboardInterrupt:
        print("\nClient stopped")
        exit()
