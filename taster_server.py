import taster_pb2
import taster_pb2_grpc
from concurrent import futures

import grpc


class Taster(taster_pb2_grpc.MachineTasterServicer):

    def getScore(self, request, context):
        return taster_pb2.Score(predicted_label=1)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    taster_pb2_grpc.add_MachineTasterServicer_to_server(Taster(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
