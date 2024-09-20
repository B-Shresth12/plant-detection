from Predict.PlantDisease import PlantDisease
from datetime import datetime
import os
import base64
import logging
from utils import file_mover


class DiseaseService:
    def __init__(self, vegetable, image_data):
        self.vegetable = vegetable
        self.image_data = image_data
        self.image_path = None

    def save_image(self):
        self.image_path = f"data/new_request/{datetime.now().strftime("%Y_%m_%d_%H_%M_%S")}.png"
        with open(self.image_path, "wb")as f:
            f.write(self.image_data)

        logging.info(f"Image saved at {self.image_path}")
        return self.image_path

    def classify_disease(self):
        # Here we are saveing the image
        image_path = self.save_image()

        # Creating PlantDisease detector instance
        detector = PlantDisease(
            vegetable=self.vegetable,
            image_path=image_path
        )
        vegetable_status, disease = detector.detect()

        if not vegetable_status:
            file_mover.move_file(image_path, self.vegetable, 'invalid')
            return False, "Invalid Image"

        if disease == "Unknown disease":
            file_mover.move_file(image_path, self.vegetable, 'unknown')
        else:
            file_mover.move_file(image_path, self.vegetable, disease)

        return True, disease
