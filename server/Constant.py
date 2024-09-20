THRESHOLD = 0.6
VEGETABLES = {
    "cauliflower": {
        "detection": {
            "model": "Predict/models/caulidetect.pth",
            "num_classes": 2,
        },
        "disease": {
            "model": "Predict/models/caulidisease.pth",
            "num_classes": 4,
            "names": [
                'Bacterial spot rot',
                'Black Rot',
                'Downy Mildew',
                'No disease'
            ]
        },

    }
}
