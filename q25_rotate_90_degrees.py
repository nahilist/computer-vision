"""
Q25. Rotate an image by 90 degrees, display it, and save the rotated image.

1. Approach/Logic:
   - Read image using `cv2.imread()`.
   - Use OpenCV's dedicated, hardware-optimized `cv2.rotate()` function with flag `cv2.ROTATE_90_CLOCKWISE`.
   - Notice that for rectangular non-square images, a 90-degree rotation swaps width and height:
     `(height, width) -> (width, height)`.
   - Save the rotated image with `cv2.imwrite()`.
   - Display original and rotated images side-by-side or in separate windows.

4. Short Explanation of Important Functions Used:
   - `cv2.rotate(src, rotateCode)`: Rotates a 2D array in multiples of 90 degrees.
     Supported flags:
     - `cv2.ROTATE_90_CLOCKWISE`
     - `cv2.ROTATE_180`
     - `cv2.ROTATE_90_COUNTERCLOCKWISE`

5. Observation/Result:
   - The image is cleanly rotated 90 degrees clockwise without any interpolation blur or clipping.
"""

import cv2
import sys

def main():
    image_path = "sample.jpg"
    img = cv2.imread(image_path)

    if img is None:
        print(f"Error: Unable to load '{image_path}'")
        sys.exit(1)

    # Rotate 90 degrees clockwise
    rotated_90_cw = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

    print("=" * 50)
    print("IMAGE ROTATION (90 DEGREES CLOCKWISE)")
    print("=" * 50)
    print(f"Original Dimensions: {img.shape[1]} (W) x {img.shape[0]} (H)")
    print(f"Rotated Dimensions : {rotated_90_cw.shape[1]} (W) x {rotated_90_cw.shape[0]} (H)")
    print("=" * 50)

    # Save output
    output_path = "output_rotated_90.png"
    cv2.imwrite(output_path, rotated_90_cw)
    print(f"Saved rotated image to '{output_path}'.")

    # Display results
    cv2.imshow("Original Image", img)
    cv2.imshow("Q25 - Rotated 90 Degrees Clockwise", rotated_90_cw)
    print("Press any key to close windows (auto-close in 3s)...")
    cv2.waitKey(3000)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

