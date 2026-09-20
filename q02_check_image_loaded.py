"""
Q2. Check whether an image was loaded successfully. If loading fails, print a meaningful error message.

1. Approach/Logic:
   - Attempt to read the image using `cv2.imread(filepath)`.
   - In OpenCV, if the image does not exist or has an unsupported format, `cv2.imread()` does NOT throw an exception; it returns `None`.
   - Check if the returned object is `None` (or use `os.path.exists` as an additional sanity check).
   - If `img is None`, print a descriptive error message explaining possible reasons (wrong path, corrupted file, unsupported extension).
   - If `img is not None`, print a confirmation message along with the image shape.

4. Short Explanation of Important Functions Used:
   - `cv2.imread(path)`: Reads an image file. Returns a NumPy array if successful, or `None` if loading fails.
   - `os.path.exists(path)`: Verifies if the file actually exists on the filesystem.

5. Observation/Result:
   - Testing with both a valid image and a non-existent path demonstrates graceful error handling instead of an unhandled runtime crash.
"""

import os
import cv2

def load_and_verify_image(file_path: str):
    print(f"\nAttempting to load: '{file_path}'")
    
    # Check filesystem existence
    if not os.path.exists(file_path):
        print(f"[ERROR] Loading failed: File '{file_path}' does not exist on disk.")
        return None

    # Load with OpenCV
    image = cv2.imread(file_path)

    # OpenCV returns None if the image file is corrupted or unsupported
    if image is None:
        print(f"[ERROR] Loading failed: '{file_path}' could not be decoded as an image. Check format or corruption.")
        return None

    print(f"[SUCCESS] Image loaded successfully! Shape: {image.shape}, Data type: {image.dtype}")
    return image

def main():
    # Test case 1: Valid image
    print("--- Test Case 1: Valid Image ---")
    valid_img = load_and_verify_image("sample.jpg")

    # Test case 2: Non-existent image
    print("\n--- Test Case 2: Non-existent Image ---")
    invalid_img = load_and_verify_image("missing_file.png")

if __name__ == "__main__":
    main()

