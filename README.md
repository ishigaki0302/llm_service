# llm_service

対話履歴をリセットするには「reset」と打ってください
- pip install grpciogrpcio>=1.63.0
- pip install grpcio-tools
- python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. llm_service.proto
