"""
Q16. Calculate and print the minimum and maximum intensity values of a grayscale image.

1. Approach/Logic:
   - Load the image directly in grayscale mode (`cv2.IMREAD_GRAYSCALE`).
   - Use OpenCV's `cv2.minMaxLoc()` to calculate both the minimum/maximum intensity values AND their corresponding `(x, y)` coordinate locations.
   - Also demonstrate NumPy's `np.min()` and `np.max()` methods.
   - Print the results clearly.

4. Short Explanation of Important Functions Used:
   - `cv2.minMaxLoc(src)`: Finds the global minimum and maximum values in a 1-channel array and their (x, y) coordinates.
   - `np.min()`, `np.max()`: Returns minimum and maximum element values in a NumPy array.

5. Observation/Result:
   - For an 8-bit grayscale image, values are bounded in [0, 255]. `cv2.minMaxLoc` also pinpoints the exact pixel location where extreme values occur.
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

    # Method 1: Using OpenCV's cv2.minMaxLoc
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(gray)

    # Method 2: Using NumPy methods
    np_min = np.min(gray)
    np_max = np.max(gray)

    print("=" * 45)
    print("MINIMUM & MAXIMUM INTENSITY VALUES")
    print("=" * 45)
    print(f"OpenCV cv2.minMaxLoc():")
    print(f"  • Minimum Intensity : {min_val} at (x={min_loc[0]}, y={min_loc[1]})")
    print(f"  • Maximum Intensity : {max_val} at (x={max_loc[0]}, y={max_loc[1]})")
    print(f"\nNumPy np.min() / np.max():")
    print(f"  • np.min()          : {np_min}")
    print(f"  • np.max()          : {np_max}")
    print("=" * 45)

if __name__ == "__main__":
    main()

