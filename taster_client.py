import grpc

import taster_pb2
import taster_pb2_grpc


def run() -> object:
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = taster_pb2_grpc.MachineTasterStub(channel)
        tasting_note = taster_pb2.Note(note='lala')

        result = stub.getScore(tasting_note)
        print(result)
        channel.close()


if __name__ == '__main__':
    run()