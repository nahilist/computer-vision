"""
Q6. Read an image and save it with a different filename using OpenCV.

1. Approach/Logic:
   - Read the original image from disk using `cv2.imread()`.
   - Verify the image loaded successfully.
   - Use `cv2.imwrite(output_path, img)` to write the image array to a new file (e.g. `saved_copy.png` or `saved_copy.jpg`).
   - Check the boolean return value of `cv2.imwrite()` to ensure the file was successfully written.
   - Verify that the new file exists on disk.

4. Short Explanation of Important Functions Used:
   - `cv2.imread(filepath)`: Loads the image from the specified path.
   - `cv2.imwrite(filename, img)`: Saves an image to a specified file path. Automatically detects and applies compression based on file extension (e.g., .png, .jpg). Returns True on success, False on failure.

5. Observation/Result:
   - OpenCV converts the in-memory array to the target format specified by the extension and writes it to disk.
"""

import cv2
import os
import sys

def main():
    input_path = "sample.jpg"
    output_path = "saved_copy.png"

    # Read the original image
    img = cv2.imread(input_path)
    if img is None:
        print(f"Error: Unable to read image '{input_path}'")
        sys.exit(1)

    print(f"Loaded '{input_path}' with shape {img.shape}.")

    # Save to a new filename / format
    success = cv2.imwrite(output_path, img)

    if success and os.path.exists(output_path):
        file_size = os.path.getsize(output_path)
        print(f"[SUCCESS] Image successfully saved as '{output_path}'.")
        print(f"File size on disk: {file_size:,} bytes")
    else:
        print(f"[ERROR] Failed to save image to '{output_path}'.")

if __name__ == "__main__":
    main()

