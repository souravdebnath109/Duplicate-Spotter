import cv2
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from tensorflow.keras.applications.vgg16 import VGG16, preprocess_input
from tensorflow.keras.models import Model

# Load VGG16 model for feature extraction
base_model = VGG16(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
model = Model(inputs=base_model.input, outputs=base_model.output)

def preprocess_image(image_bytes):
    # Convert to OpenCV format
    file_bytes = np.asarray(bytearray(image_bytes.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    # Resize to 224x224 and preprocess for VGG
    img = cv2.resize(img, (224, 224))
    img = preprocess_input(img)
    img = np.expand_dims(img, axis=0)
    return img

def extract_features(image_bytes):
    img = preprocess_image(image_bytes)
    features = model.predict(img)
    return features.flatten().reshape(1, -1)

def compare_handwriting(image1, image2, threshold=0.85):
    feat1 = extract_features(image1)
    feat2 = extract_features(image2)
    score = cosine_similarity(feat1, feat2)[0][0]
    return score >= threshold, score
