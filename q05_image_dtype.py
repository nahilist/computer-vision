"""
Q5. Print the data type (`dtype`) of the image matrix.

1. Approach/Logic:
   - Read an image using `cv2.imread()`.
   - Access the `.dtype` attribute of the NumPy ndarray.
   - Explain what the data type means in the context of computer vision (e.g., `uint8` stands for 8-bit unsigned integer, ranging from 0 to 255).
   - Also print `itemsize` (bytes per element) and value range.

4. Short Explanation of Important Functions Used:
   - `img.dtype`: Returns the data type of the array elements (typically `uint8` for standard images).
   - `img.itemsize`: Returns the length of one array element in bytes (1 byte for `uint8`).

5. Observation/Result:
   - Standard images loaded with OpenCV are of type `uint8` (unsigned 8-bit integer), where each channel value is an integer between 0 and 255.
"""

import cv2
import sys
import numpy as np

def main():
    image_path = "sample.jpg"
    img = cv2.imread(image_path)

    if img is None:
        print(f"Error: Unable to load image from '{image_path}'")
        sys.exit(1)

    print("=" * 45)
    print("IMAGE DATA TYPE & MEMORY INFO")
    print("=" * 45)
    print(f"Data type (dtype) : {img.dtype}")
    print(f"Item size (bytes) : {img.itemsize} byte per channel value")
    print(f"Minimum value     : {np.iinfo(img.dtype).min}")
    print(f"Maximum value     : {np.iinfo(img.dtype).max}")
    print(f"Total Memory      : {img.nbytes} bytes ({img.nbytes / 1024:.2f} KB)")
    print("=" * 45)

if __name__ == "__main__":
    main()

