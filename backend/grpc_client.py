import grpc
from grpc_out import plantdisease_pb2, plantdisease_pb2_grpc


def classify_disease(crop: str, image_data: bytes):

    try:
        channel = grpc.insecure_channel('localhost:50051')
        stub = plantdisease_pb2_grpc.DiseaseClassifierStub(channel)

        request = plantdisease_pb2.ClassifyRequest(
            crop=crop,
            image=image_data
        )

        response = stub.ClassifyDisease(request)

        return {"disease": response.disease}
    except grpc.RpcError as e:
        return {"status": "error", 'message': e.details()}
