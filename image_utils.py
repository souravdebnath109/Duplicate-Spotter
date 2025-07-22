# image_utils.py
from PIL import Image
import imagehash
import numpy as np
# from deepface import DeepFace
import cv2
import face_recognition
def is_image_duplicate(img1, img2, threshold=5):
    """Detect image similarity using perceptual hash"""
    hash1 = imagehash.phash(img1)
    hash2 = imagehash.phash(img2)
    diff = abs(hash1 - hash2)
    return diff <= threshold, diff


# def is_face_duplicate(img1_path, img2_path, threshold=0.6):
#     """
#     Compares two face images.
#     Returns: (bool, float) -> (are same person, face distance)
#     Lower distance means more similar. Threshold default ~0.6.
#     """
#     # Load and convert to RGB to avoid unsupported formats
#     def load_and_convert(path):
#         img = face_recognition.load_image_file(path)
#         if img.ndim == 2:  # grayscale
#             img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
#         elif img.shape[2] == 4:  # RGBA
#             img = cv2.cvtColor(img, cv2.COLOR_RGBA2RGB)
#         return img

#     img1 = load_and_convert(img1_path)
#     img2 = load_and_convert(img2_path)

#     # Get face encodings (embedding vectors)
#     encodings1 = face_recognition.face_encodings(img1)
#     encodings2 = face_recognition.face_encodings(img2)

#     if len(encodings1) == 0 or len(encodings2) == 0:
#         raise ValueError("No face found in one or both images.")

#     # Take the first face found in each image
#     encoding1 = encodings1[0]
#     encoding2 = encodings2[0]

#     # Calculate Euclidean distance between faces
#     dist = face_recognition.face_distance([encoding1], encoding2)[0]

#     # Compare distance to threshold
#     is_same = dist <= threshold

#     return is_same, dist
