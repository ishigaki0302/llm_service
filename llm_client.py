import grpc
import llm_service_pb2
import llm_service_pb2_grpc

def run_inference(input_text):
    with grpc.insecure_channel('133.20.57.175:50051') as channel:
        stub = llm_service_pb2_grpc.LLMServiceStub(channel)
        response = stub.Infer(llm_service_pb2.InferRequest(input_text=input_text))
        return response.output_text

input_text = input(">")
output_text = run_inference(input_text)
print(output_text)