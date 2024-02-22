import os
import time
import cv2
import numpy as np
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import pytesseract
from PIL import Image
import pyperclip


class ImageHandler(FileSystemEventHandler):
    def preprocess_image(self, image_path):
        """
        Enhanced preprocessing for more artistic images.
        """
        img = cv2.imread(image_path)

        # Convert to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Apply adaptive thresholding
        thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                       cv2.THRESH_BINARY, 11, 2)

        # Apply dilation and erosion to make the text more prominent
        kernel = np.ones((1, 1), np.uint8)
        img_dilation = cv2.dilate(thresh, kernel, iterations=1)
        img_erosion = cv2.erode(img_dilation, kernel, iterations=1)

        return img_erosion

    def process_image(self, image_path):
        """
        Directly process the image file given by image_path: perform OCR and copy text to clipboard.
        """
        print(f"Processing image: {image_path}")

        # Preprocess the image
        preprocessed_image = self.preprocess_image(image_path)

        # Convert the OpenCV image (numpy array) to a PIL image for pytesseract
        pil_image = Image.fromarray(preprocessed_image)

        # Perform OCR using pytesseract
        text = pytesseract.image_to_string(pil_image)
        pyperclip.copy(text)
        print("Text copied to clipboard.")
        print(text)
        return text  # Optionally return the extracted text for testing or further processing

    def process(self, event):
        """
        Process the image file from a watchdog event: perform OCR and copy text to clipboard.
        """
        self.process_image(event.src_path)

    def on_created(self, event):
        if not event.is_directory and event.src_path.lower().endswith(('.png', '.jpg', '.jpeg')):
            self.process(event)


def start_watching(path):
    event_handler = ImageHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


if __name__ == "__main__":
    path = "/Users/noushin/Desktop/Work/Portfolio/Projects/OCRTextExtractor/data"
    # path = "/path/to/your/directory"  # Change this to your target directory
    print(f"Watching for images in: {path}")
    start_watching(path)
