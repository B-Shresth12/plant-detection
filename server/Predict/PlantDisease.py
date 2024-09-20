import torch
from torchvision import transforms
from PIL import Image
import logging
from typing import Tuple, Optional
from Constant import VEGETABLES, THRESHOLD
from Predict.models.ModelHandler import ModelHandler

# Initialize logging
logging.basicConfig(
    filename='logs/plant.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filemode='a'
)


class PlantDisease:
    def __init__(self, vegetable, image_path):
        self.image_path = image_path
        self.vegetable = vegetable

        self.device = torch.device(
            "cuda" if torch.cuda.is_available() else "cpu")

        self.detection_model = ModelHandler(
            model_path=VEGETABLES[vegetable]['detection']['model'],
            num_classes=VEGETABLES[vegetable]['detection']['num_classes'],
            device=self.device
        )
        self.disease_model = ModelHandler(
            model_path=VEGETABLES[vegetable]['disease']['model'],
            num_classes=VEGETABLES[vegetable]['disease']['num_classes'],
            device=self.device
        )

        self.transform_matrix = transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[
                0.229, 0.224, 0.225]),
        ])

    def detect(self):
        vegetable_status, disease_class = self.predict_image_with_threshold()
        disease_names = VEGETABLES[self.vegetable]["disease"]["names"]
        # return vegetable_class
        if vegetable_status:
            if disease_class == "Unknown disease":
                return True, disease_class
            else:
                return True, disease_names[disease_class]
        elif not vegetable_status:
            logging.error(f"Predicted class: {True}")
            return False, None
        else:
            logging.error("Error in prediction.")
            return None, None

    def predict_image_with_threshold(self, threshold=THRESHOLD) -> Tuple[bool, Optional[int]]:
        image = self.load_image(
            self.image_path, self.transform_matrix, self.device)
        if image is None:
            return "error", None

        # Predict cauliflower or non-cauliflower
        detection_outputs = self.detection_model.predict(image)
        _, vegetable_detection = torch.max(detection_outputs, 1)

        if vegetable_detection.item() == 0:  # It's a cauliflower
            # Apply confidence-based prediction for disease
            predicted_class, confidence = self.predict_with_threshold(
                image=image
            )

            if predicted_class == "Unknown":
                return True, "Unknown disease"

            return True, predicted_class
        else:
            return False, None

    def predict_with_threshold(self, image, threshold=THRESHOLD):
        """
        Predict the class with a confidence threshold.
        If the confidence is below the threshold, return 'Unknown'.
        """
        with torch.no_grad():
            outputs = self.disease_model.model(image)
            # Apply softmax to get probabilities
            softmax_outputs = torch.softmax(outputs, dim=1)
            max_prob, predicted_class = torch.max(softmax_outputs, 1)

            if max_prob.item() < threshold:
                return "Unknown", None
            return predicted_class.item(), max_prob.item()

    def load_image(self, image_path: str, transform: transforms.Compose, device: torch.device) -> Optional[torch.Tensor]:
        try:
            image = Image.open(image_path).convert('RGB')
            image = transform(image).unsqueeze(0).to(device)
            logging.info(f"Image loaded and transformed from {image_path}")
            return image
        except Exception as e:
            logging.error(f"Error loading image: {e}")
            return None
