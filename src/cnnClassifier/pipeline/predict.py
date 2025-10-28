import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model 
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # Suppress info and warning messages

class PredictionPipeline:
    def __init__(self, filename):
        self.filename = filename

    def predict(self):
        model_path = os.path.join("artifacts", "training", "model.h5")  # Correct model path
        model = load_model(model_path)
        img_path = self.filename
        test_image = image.load_img(img_path, target_size=(224, 224))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)
        result = np.argmax(model.predict(test_image), axis=1)
        print(result)

        if result[0] == 1:
            prediction = 'Healthy'
            return [{"image": prediction}]
        else:
            prediction = 'Coccidiosis Infected'
            return [{"image": prediction}]