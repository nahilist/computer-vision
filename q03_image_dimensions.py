"""
Q3. Print the image height, width, and number of channels.

1. Approach/Logic:
   - Read the image using `cv2.imread()`.
   - Access the `.shape` attribute of the resulting NumPy array.
   - For a standard 3-channel color image, `shape` returns a tuple `(height, width, channels)`.
   - Handle grayscale images gracefully, where `shape` returns `(height, width)` (i.e. 1 channel).
   - Print each attribute clearly.

4. Short Explanation of Important Functions Used:
   - `img.shape`: A NumPy tuple representing matrix dimensions. For 3D arrays: `(rows/height, cols/width, channels)`.

5. Observation/Result:
   - For `sample.jpg`, the height is 400 pixels, width is 400 pixels, and it has 3 color channels (Blue, Green, Red).
"""

import cv2
import sys

def main():
    image_path = "sample.jpg"
    img = cv2.imread(image_path)

    if img is None:
        print(f"Error: Unable to load image from '{image_path}'")
        sys.exit(1)

    # Access dimensions via shape
    shape = img.shape
    height = shape[0]
    width = shape[1]
    channels = shape[2] if len(shape) > 2 else 1

    print("=" * 40)
    print("IMAGE DIMENSIONS INFORMATION")
    print("=" * 40)
    print(f"Image Path        : {image_path}")
    print(f"Height (rows)     : {height} pixels")
    print(f"Width (columns)   : {width} pixels")
    print(f"Number of Channels: {channels}")
    print(f"Shape Tuple       : {shape}")
    print("=" * 40)

if __name__ == "__main__":
    main()

