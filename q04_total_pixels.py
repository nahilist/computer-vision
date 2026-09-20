"""
Q4. Calculate and print the total number of pixels in an image.

1. Approach/Logic:
   - Read the image using `cv2.imread()`.
   - The spatial resolution (total pixel count) is defined as `height * width`.
   - The total number of elements/bytes in the multi-channel array can be retrieved directly via NumPy's `.size` attribute (`height * width * channels`).
   - Print both spatial pixels and total array values to show a clear distinction between pixels and color channel components.

4. Short Explanation of Important Functions Used:
   - `img.shape[0]`, `img.shape[1]`: Returns height and width respectively.
   - `img.size`: Total number of elements in the NumPy ndarray.

5. Observation/Result:
   - For a 400x400 image, total spatial pixels = 400 * 400 = 160,000 pixels.
   - For a 3-channel image, total values stored = 160,000 * 3 = 480,000 elements.
"""

import cv2
import sys

def main():
    image_path = "sample.jpg"
    img = cv2.imread(image_path)

    if img is None:
        print(f"Error: Unable to load image from '{image_path}'")
        sys.exit(1)

    height, width = img.shape[:2]
    total_pixels = height * width
    total_array_elements = img.size

    print("=" * 45)
    print("TOTAL PIXELS CALCULATION")
    print("=" * 45)
    print(f"Image Dimensions        : {width} x {height}")
    print(f"Total Spatial Pixels    : {total_pixels:,} pixels")
    print(f"Total Elements (Channels): {total_array_elements:,} (via img.size)")
    print("=" * 45)

if __name__ == "__main__":
    main()

