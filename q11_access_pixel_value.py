"""
Q11. Access and print the pixel value at a user-provided `(x, y)` coordinate.

1. Approach/Logic:
   - Read image using `cv2.imread()`.
   - Obtain user coordinates `(x, y)` (where `x` = column, `y` = row).
   - In NumPy array indexing, indexing follows `image[y, x]` (row first, column second).
   - Validate that `0 <= x < width` and `0 <= y < height` to prevent out-of-bounds `IndexError`.
   - Extract and print pixel values (B, G, R for color or intensity for grayscale).

4. Short Explanation of Important Functions Used:
   - `img[y, x]`: Accesses array element at row `y` and column `x`.
   - `img.shape`: Used to validate boundaries before indexing.

5. Observation/Result:
   - Careful attention is required to avoid flipping rows and columns: (x, y) maps to img[y, x].
"""

import cv2
import sys

def access_pixel(img, x: int, y: int):
    h, w = img.shape[:2]
    if not (0 <= x < w and 0 <= y < h):
        print(f"[ERROR] Coordinate ({x}, {y}) is out of bounds! Valid range: x in [0, {w-1}], y in [0, {h-1}].")
        return None

    pixel_value = img[y, x]
    return pixel_value

def main():
    image_path = "sample.jpg"
    img = cv2.imread(image_path)

    if img is None:
        print(f"Error: Unable to load image '{image_path}'.")
        sys.exit(1)

    h, w = img.shape[:2]
    print(f"Image loaded: {w}x{h} pixels.")

    # Coordinates to query (can be user-provided or demonstration values)
    demo_coords = [(100, 100), (200, 200), (350, 50)]

    print("\n" + "=" * 45)
    print("PIXEL VALUE LOOKUP (img[y, x])")
    print("=" * 45)

    for x, y in demo_coords:
        val = access_pixel(img, x, y)
        if val is not None:
            if len(img.shape) == 3:
                b, g, r = val
                print(f"Pixel at (x={x}, y={y}) -> B={b}, G={g}, R={r} | Array: {val}")
            else:
                print(f"Pixel at (x={x}, y={y}) -> Intensity={val}")

    print("=" * 45)

if __name__ == "__main__":
    main()

