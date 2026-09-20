"""
Q12. Modify the intensity/value of a selected pixel and save the modified image.

1. Approach/Logic:
   - Read image using `cv2.imread()`.
   - Make a copy using `.copy()` to keep the original intact.
   - Select coordinates `(x, y)`. Assign a new color value: `modified_img[y, x] = [B, G, R]`.
   - Because a single pixel in a high-res image is too small to see with the naked eye, we also modify a small visible patch/square (e.g., 20x20 around (x, y)) to clearly visualize the change.
   - Save the modified image using `cv2.imwrite()`.

4. Short Explanation of Important Functions Used:
   - `img.copy()`: Creates a deep copy of the image array to prevent altering the original array.
   - `img[y, x] = value`: Directly assigns a new BGR value to the pixel.
   - `cv2.imwrite(path, img)`: Saves the modified array to disk.

5. Observation/Result:
   - Modifying array elements in-place directly changes color intensities.
"""

import cv2
import sys

def main():
    image_path = "sample.jpg"
    img = cv2.imread(image_path)

    if img is None:
        print(f"Error: Unable to load image '{image_path}'.")
        sys.exit(1)

    modified_img = img.copy()

    # Target coordinate
    x, y = 200, 200
    print(f"Original pixel at (x={x}, y={y}): {modified_img[y, x]}")

    # 1. Modify single pixel to bright yellow [B=0, G=255, R=255]
    modified_img[y, x] = [0, 255, 255]
    print(f"Modified single pixel at (x={x}, y={y}) to: {modified_img[y, x]}")

    # 2. Modify a 20x20 region around (x, y) to make the modification clearly visible to human eye
    half_box = 15
    modified_img[y-half_box : y+half_box, x-half_box : x+half_box] = [0, 255, 255]

    # Save output
    output_path = "output_modified_pixel.png"
    cv2.imwrite(output_path, modified_img)
    print(f"[SUCCESS] Modified image saved to '{output_path}'.")

    # Display comparison
    cv2.imshow("Original", img)
    cv2.imshow("Modified (with yellow patch at center)", modified_img)
    print("Press any key to close windows (auto-close in 3s)...")
    cv2.waitKey(3000)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

