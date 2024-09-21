# importing system libraries
import os
import sys
# importing settings
import settings
# importing gRPC
import grpc
from grpc import StatusCode
from concurrent import futures
from grpc_out import plantdisease_pb2, plantdisease_pb2_grpc
# importing service
from services.disease_service import DiseaseService

os.environ.setdefault('MY_APP_SETTINGS_MODULE', 'settings')

# Import settings dynamically
settings = __import__(os.getenv('MY_APP_SETTINGS_MODULE'))

# Access the settings
GRPC_PORT = settings.GRPC_PORT

class DiseaseClassifierServicer(plantdisease_pb2_grpc.DiseaseClassifierServicer):
    def ClassifyDisease(self, request, context):
        vegetable = request.crop
        image_data = request.image

        if not vegetable:
            context.abort(StatusCode.INVALID_ARGUMENT,
                          "Crop field is required")

        if not image_data:
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
    port = GRPC_PORT
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    plantdisease_pb2_grpc.add_DiseaseClassifierServicer_to_server(
        DiseaseClassifierServicer(), server)
    server.add_insecure_port(f"[::]:{port}")
    server.start()
    print(f"gRPC server started on port {port}")
    server.wait_for_termination()


if __name__ == '__main__':
    import settings
    try:
        serve()
    except ImportError as exc:
        logging.error(f"Couldn't import necessary modules: {exc}")
        sys.exit(1)
    except Exception as e:
        logging.error(f"Unexpected error occured: {e}")
        sys.exit(1)
