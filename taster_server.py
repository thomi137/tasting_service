import logging
import pickle
import grpc
import numpy
import sklearn

import taster_pb2
import taster_pb2_grpc
from concurrent import futures


class Taster(taster_pb2_grpc.MachineTasterServicer):

    def __init__(self):
        logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)s - %(levelname)s - %(message)s')
        self._logger = logging.getLogger('Taster')
        self._clf = pickle.load(open('classifier.pkl', 'rb'))

    def getScore(self, request, context):
        self._logger.info('Calling with {}'.format(request.note))
        note_array = []
        note_array.append(request.note)
        prediction = self._clf.predict(note_array)
        return taster_pb2.Score(predicted_label=int(prediction.item(0)))


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    taster_pb2_grpc.add_MachineTasterServicer_to_server(Taster(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
