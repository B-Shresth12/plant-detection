import os
from dotenv import load_dotenv

import logging

load_dotenv()

# Base directory of the project
BASE_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), os.getenv('BASE_DIR'))

# Log Directory of the project
LOG_DIR = os.path.join(BASE_DIR, os.getenv('LOG_DIR'))

# Data Directory to store images
DATA_DIR = os.path.join(BASE_DIR, os.getenv('DATA_DIR'))
# Data Directory for new requests
NEW_REQUEST_DIR = os.path.join(DATA_DIR, 'new_request')
#Data Directory for analysed data
PREDICTED_DIR = os.path.join(DATA_DIR, 'predicted_data')

# gRPC Port
GRPC_PORT = os.getenv('GRPC_PORT', '50051')

# Ensure directories exist
os.makedirs(LOG_DIR, exist_ok=True)
os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(NEW_REQUEST_DIR, exist_ok=True)
os.makedirs(PREDICTED_DIR, exist_ok=True)
