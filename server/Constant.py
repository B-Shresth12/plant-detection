import settings
import os 

BASE_DIR = settings.BASE_DIR
THRESHOLD = 0.6
VEGETABLES = {
    "cauliflower": {
        "detection": {
            "model": os.path.join(BASE_DIR, "Predict/models/caulidetect.pth"),
            "num_classes": 2,
        },
        "disease": {
            "model": os.path.join(BASE_DIR, "Predict/models/caulidisease.pth"),
            "num_classes": 4,
            "names": [
                'Bacterial spot rot',
                'Black Rot',
                'Downy Mildew',
                'No disease'
            ]
        }
    }
}
