"""
Q17. Calculate and print the mean intensity of a grayscale image.

1. Approach/Logic:
   - Read image in grayscale mode (`cv2.IMREAD_GRAYSCALE`).
   - Compute mean intensity using:
     1. OpenCV's `cv2.mean(gray)[0]` (returns a tuple with scalar means for up to 4 channels).
     2. NumPy's `np.mean(gray)`.
   - The mean intensity represents the overall average brightness of the image (0 = totally black, 255 = totally white).
   - Print both results to demonstrate accuracy.

4. Short Explanation of Important Functions Used:
   - `cv2.mean(src)`: Computes the mean value M of array elements independently for each channel.
   - `np.mean(a)`: Computes the arithmetic mean along the specified axis (or flattened array).

5. Observation/Result:
   - Both methods produce identical mean intensity values (e.g. around 130-170 depending on image content).
"""

import cv2
import numpy as np
import sys

def main():
    image_path = "sample.jpg"
    gray = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    if gray is None:
        print(f"Error: Unable to load '{image_path}'")
        sys.exit(1)

    # 1. OpenCV cv2.mean
    cv2_mean_val = cv2.mean(gray)[0]

    # 2. NumPy np.mean
    numpy_mean_val = np.mean(gray)

    print("=" * 45)
    print("MEAN INTENSITY CALCULATION")
    print("=" * 45)
    print(f"Image Resolution     : {gray.shape[1]} x {gray.shape[0]}")
    print(f"Total Pixels         : {gray.size:,}")
    print(f"OpenCV cv2.mean()    : {cv2_mean_val:.4f}")
    print(f"NumPy np.mean()      : {numpy_mean_val:.4f}")
    print(f"Brightness Category  : {'Bright' if cv2_mean_val > 128 else 'Dark/Moderate'}")
    print("=" * 45)

if __name__ == "__main__":
    main()

