"""
Q13. Read a color image and print the B, G, and R values of a selected pixel.

1. Approach/Logic:
   - Read a color image with `cv2.imread()`.
   - Access the channel values at coordinates `(x, y)`:
     - Blue channel (index 0): `img[y, x, 0]`
     - Green channel (index 1): `img[y, x, 1]`
     - Red channel (index 2): `img[y, x, 2]`
   - Verify indexing boundaries and print the separated component values.

4. Short Explanation of Important Functions Used:
   - `img[y, x, c]`: Accesses channel `c` (0=Blue, 1=Green, 2=Red) for the pixel at row `y` and column `x`.

5. Observation/Result:
   - OpenCV arrays have 3 dimensions: `[height/row, width/col, channel]`.
   - Channel 0 corresponds to Blue, Channel 1 to Green, Channel 2 to Red.
"""

import cv2
import sys

def print_bgr(img, x: int, y: int):
    h, w = img.shape[:2]
    if not (0 <= x < w and 0 <= y < h):
        print(f"Error: ({x}, {y}) out of range.")
        return

    # Extract individual B, G, R channels
    blue_val  = img[y, x, 0]
    green_val = img[y, x, 1]
    red_val   = img[y, x, 2]

    print(f"Pixel at (x={x}, y={y}):")
    print(f"  • Blue  (Channel 0): {blue_val}")
    print(f"  • Green (Channel 1): {green_val}")
    print(f"  • Red   (Channel 2): {red_val}")
    print(f"  • Combined [B, G, R]: [{blue_val}, {green_val}, {red_val}]")
    print("-" * 35)

def main():
    image_path = "sample.jpg"
    img = cv2.imread(image_path)

    if img is None:
        print(f"Error: Unable to load '{image_path}'")
        sys.exit(1)

    print("=" * 45)
    print("BGR CHANNEL VALUES INSPECTION")
    print("=" * 45)

    # Test distinct points:
    test_points = [(100, 100), (200, 200), (300, 300)]
    for x, y in test_points:
        print_bgr(img, x, y)

if __name__ == "__main__":
    main()

