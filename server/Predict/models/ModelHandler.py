import torch
from efficientnet_pytorch import EfficientNet
import torch.nn as nn
import os
import logging


class ModelHandler:
    def __init__(self, model_path: str, num_classes: int, device: torch.device):
        self.device = device
        self.model = EfficientNet.from_pretrained('efficientnet-b0')
        self.model._fc = nn.Linear(self.model._fc.in_features, num_classes)
        self.load_model(model_path)

    def load_model(self, model_path: str):
        if os.path.exists(model_path):
            logging.info(f"Loading model from {model_path}")
            try:
                self.model.load_state_dict(torch.load(
                    model_path, map_location=self.device))
                self.model.eval()
                self.model.to(self.device)
                logging.info("Model loaded successfully.")
            except Exception as e:
                logging.error(f"Error loading model: {e}")
        else:
            logging.error(f"Model file does not exist: {model_path}")

    def predict(self, image: torch.Tensor) -> torch.Tensor:
        with torch.no_grad():
            outputs = self.model(image)
        return outputs
