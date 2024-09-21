# Plant Disease Classification System

This project is a microservice-based application for plant disease classification using gRPC for communication between a FastAPI client and a PyTorch-based machine learning backend. It classifies plant diseases from images and organizes the data for future dataset creation.

## Features

- **gRPC-based microservices**: Efficient communication between the FastAPI client and ML inference service.
- **Machine Learning**: Uses PyTorch models for vegetable type and plant disease detection.
- **Modular Design**: Clean separation of concerns for scalability and flexibility.
- **FastAPI for HTTP API**: Provides an interface for uploading images and receiving classification results.
- **Logging and Data Handling**: Logs all requests and stores predicted data for future use.

## Project Structure

```bash
server/
  ├── data/
  │   ├── new_request/         # Directory for newly received images
  │   └── predicted_data/      # Directory for processed images, categorized by crop type
  ├── grpc_out/                # Generated gRPC code
  ├── logs/                    # Log files
  ├── Predict/                 # ML models and prediction logic
  ├── app.py                   # gRPC server
  ├── settings.py              # Configuration and settings
  ├── constant.py              # Constant values
  └── requirements.txt         # Dependencies

fastapi_app/
  ├── main.py                  # FastAPI client for handling API requests
  ├── models.py                # Request/Response models
  ├── grpc_client.py           # Client logic to communicate with the gRPC server
  └── requirements.txt         # FastAPI dependencies
```

## Installation

### Windows

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/plant-disease-classification.git
    cd plant-disease-classification
    ```

2. Create a virtual environment:
    ```bash
    python -m venv .venv
    .venv\Scripts\activate
    ```

3. Install dependencies:
    ```bash
    pip install -r server/requirements.txt
    pip install -r fastapi_app/requirements.txt
    ```

4. Set up environment variables by copying `.env.example` to `.env` and modifying it:
    ```bash
    copy .env.example .env
    ```

5. Run the gRPC server:
    ```bash
    python server/app.py
    ```

6. Run the FastAPI server:
    ```bash
    uvicorn fastapi_app.main:app --reload
    ```

### Linux / MacOS

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/plant-disease-classification.git
    cd plant-disease-classification
    ```

2. Create a virtual environment:
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3. Install dependencies:
    ```bash
    pip install -r server/requirements.txt
    pip install -r fastapi_app/requirements.txt
    ```

4. Set up environment variables by copying `.env.example` to `.env` and modifying it:
    ```bash
    cp .env.example .env
    ```

5. Run the gRPC server:
    ```bash
    python3 server/app.py
    ```

6. Run the FastAPI server:
    ```bash
    uvicorn fastapi_app.main:app --reload
    ```

## API Usage

1. **Start the servers**:
   - Run the gRPC server: 
     ```bash
     python server/app.py
     ```
   - Run the FastAPI server:
     ```bash
     uvicorn fastapi_app.main:app --reload
     ```

2. **API Request Example (CURL)**:
   ```bash
   curl -X 'POST' \
   'http://127.0.0.1:8000/classify' \
   -H 'accept: application/json' \
   -H 'Content-Type: multipart/form-data' \
   -F 'crop=cauliflower' \
   -F 'image=@your-image-file.png'
   ```

3. **API Response**:
   ```json
   {
     "disease": "Black Rot"
   }
   ```

## Environment Variables

The project uses environment variables to manage paths and ports. The variables include:
- `BASE_DIR`: Base directory for data and logs.
- `LOG_DIR`: Directory for storing log files.
- `GRPC_PORT`: Port for gRPC server communication.

## How it Works

1. **FastAPI** accepts image upload and crop details from the user.
2. The FastAPI server forwards the request to the gRPC service.
3. **gRPC** service runs PyTorch models to predict the disease based on the image.
4. Results are returned to the FastAPI client, and the response is sent back to the user.

## License

MIT License
```

This version uses proper GitHub markdown with backticks for code and commands, and it includes installation instructions for Windows, Linux, and macOS.