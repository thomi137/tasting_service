import logging
import grpc

import taster_pb2
import taster_pb2_grpc
from concurrent import futures



class Taster(taster_pb2_grpc.MachineTasterServicer):

    def __init__(self):
        logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)s - %(levelname)s - %(message)s')
        self._logger = logging.getLogger('Taster')

    def getScore(self, request, context):
        self._logger.info('calling with {}'.format(request.note))
        return taster_pb2.Score(predicted_label=1)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    taster_pb2_grpc.add_MachineTasterServicer_to_server(Taster(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
