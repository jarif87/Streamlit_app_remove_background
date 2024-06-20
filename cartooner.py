import numpy as np
import cv2

def cartoonize(image):
    # Ensure the image is a numpy array
    if not isinstance(image, np.ndarray):
        raise ValueError("Image should be a numpy array")

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply median blur to smoothen the image
    gray_blur = cv2.medianBlur(gray, 7)

    # Detect edges using adaptive thresholding
    edges = cv2.adaptiveThreshold(
        gray_blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 2
    )

    # Apply bilateral filter to smoothen flat regions while keeping edges sharp
    color = cv2.bilateralFilter(image, 9, 300, 300)

    # Combine color image with edges
    cartoon = cv2.bitwise_and(color, color, mask=edges)

    return cartoon
