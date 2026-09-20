"""
Q18. Calculate and print the mean and standard deviation of a grayscale image using NumPy/OpenCV.

1. Approach/Logic:
   - Read image in grayscale mode (`cv2.IMREAD_GRAYSCALE`).
   - Method A (OpenCV): Use `cv2.meanStdDev(src)` which computes both mean and standard deviation simultaneously.
   - Method B (NumPy): Use `np.mean(src)` and `np.std(src)`.
   - Mean indicates average brightness; Standard Deviation measures the spread of pixel intensities, which correlates with image contrast.
   - Print and compare both methods.

4. Short Explanation of Important Functions Used:
   - `cv2.meanStdDev(src)`: Calculates a mean and standard deviation of array elements. Returns two matrices `(mean, stddev)`.
   - `np.mean(a)`: Calculates arithmetic average of array.
   - `np.std(a)`: Calculates standard deviation of array.

5. Observation/Result:
   - High standard deviation implies wide contrast (distinct dark and bright areas).
   - Low standard deviation implies low contrast (flat/uniform wash).
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

    # 1. OpenCV cv2.meanStdDev
    cv_mean, cv_stddev = cv2.meanStdDev(gray)

    # 2. NumPy methods
    np_mean = np.mean(gray)
    np_std = np.std(gray)

    print("=" * 50)
    print("MEAN & STANDARD DEVIATION (CONTRAST METRICS)")
    print("=" * 50)
    print("OpenCV cv2.meanStdDev():")
    print(f"  • Mean Intensity        : {cv_mean[0][0]:.4f}")
    print(f"  • Standard Deviation    : {cv_stddev[0][0]:.4f}")
    print("\nNumPy np.mean() & np.std():")
    print(f"  • Mean Intensity        : {np_mean:.4f}")
    print(f"  • Standard Deviation    : {np_std:.4f}")
    print("=" * 50)

if __name__ == "__main__":
    main()

