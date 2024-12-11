import sys
import os
from PIL import Image
import numpy as np

# Add the root directory of the project to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ai.model.model_wrapper import model_wrapper

def get_artwork_model():
    # Default model path within the project
    default_model_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'model', 'model.h5'))
    # Model path from environment variable or default to project path
    model_path = os.getenv('MODEL_PATH', default_model_path)
    print(f"Model path: {model_path}")
    if not os.path.exists(model_path):
        print(f"Model path does not exist: {model_path}")
        raise FileNotFoundError(f"Model path does not exist: {model_path}")
    wrapper_obj = model_wrapper(model_path)
    return wrapper_obj.get_model()

def process_image(img_path):
    with Image.open(img_path) as img:
        img = img.convert('RGB')
        img = img.resize((256, 256))
        img_array = np.array(img)
        img_array = np.expand_dims(img_array, axis=0)
        print("Image resized to", img_array.shape)
        return img_array

def predict_image(img_path):
    model = get_artwork_model()
    img_array = process_image(img_path)
    prediction = model.predict(img_array)
    return prediction