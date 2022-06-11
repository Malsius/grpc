from concurrent import futures

import grpc
import crypto_pb2
import crypto_pb2_grpc
import credentials


class CryptoServicer(crypto_pb2_grpc.CryptoServicer):

    def GetPlusOne(self, request, context):
        print(f"Receipt {request.number} from client")
        number_plus_one = request.number + 1
        print(f"Return {number_plus_one}")
        return crypto_pb2.Response(number=number_plus_one)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    crypto_pb2_grpc.add_CryptoServicer_to_server(CryptoServicer(), server)
    server_credentials = grpc.ssl_server_credentials(((credentials.SERVER_CERTIFICATE_KEY, credentials.SERVER_CERTIFICATE,),))
    server.add_secure_port('localhost:50051', server_credentials)
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    try:
        serve()
    except KeyboardInterrupt:
        print("\nServer stopped")
        exit()
