import grpc
from concurrent import futures
from grpc_out import plantdisease_pb2, plantdisease_pb2_grpc
from services.disease_service import DiseaseService
import logging
from grpc import StatusCode

logging.basicConfig(
    filename='logs/app.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filemode='a'
)


class DiseaseClassifierServicer(plantdisease_pb2_grpc.DiseaseClassifierServicer):
    def ClassifyDisease(self, request, context):
        vegetable = request.crop
        image_data = request.image

        if not vegetable:
            logging.error(StatusCode.INVALID_ARGUMENT, "Crop Field not provided")
            context.abort(StatusCode.INVALID_ARGUMENT,
                          "Crop field is required")

        if not image_data:
            logging.error(StatusCode.INVALID_ARGUMENT, "Image not provided")
            context.abort(StatusCode.INVALID_ARGUMENT,
                          "Image field is required")

        disease_service = DiseaseService(
            vegetable=vegetable,
            image_data=image_data
        )
        status, result = disease_service.classify_disease()

        if not status:
            context.abort(StatusCode.UNKNOWN, result)

        return plantdisease_pb2.ClassifyResponse(
            disease=result
        )


def serve():
    port = 50051
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    plantdisease_pb2_grpc.add_DiseaseClassifierServicer_to_server(
        DiseaseClassifierServicer(), server)
    server.add_insecure_port(f"[::]:{port}")
    server.start()
    print(f"gRPC server started on port {port}")
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
