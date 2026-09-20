"""
Q8. Convert a color image to grayscale using `cv2.cvtColor()`.

1. Approach/Logic:
   - Load the original color image in BGR mode using `cv2.imread()`.
   - Use `cv2.cvtColor()` with the conversion code `cv2.COLOR_BGR2GRAY`.
   - OpenCV applies the standard luminance formula:
     `Y = 0.299 * R + 0.587 * G + 0.114 * B`
   - Compare shapes before and after conversion (`(H, W, 3)` -> `(H, W)`).
   - Save the converted grayscale image to disk.

4. Short Explanation of Important Functions Used:
   - `cv2.cvtColor(src, code)`: Converts an input image from one color space to another.
   - `cv2.COLOR_BGR2GRAY`: Flag indicating conversion from 3-channel BGR to 1-channel Grayscale.

5. Observation/Result:
   - The output matrix drops the 3rd channel dimension, condensing 3 color planes into a single intensity channel with values [0, 255].
"""

import cv2
import sys

def main():
    image_path = "sample.jpg"
    bgr_img = cv2.imread(image_path)

    if bgr_img is None:
        print(f"Error: Unable to load image '{image_path}'.")
        sys.exit(1)

    print(f"Original BGR Shape: {bgr_img.shape}")

    # Convert to grayscale using cv2.cvtColor
    gray_img = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2GRAY)

    print(f"Converted Grayscale Shape: {gray_img.shape}")

    # Save output
    output_path = "output_cvt_grayscale.jpg"
    cv2.imwrite(output_path, gray_img)
    print(f"Converted image saved to '{output_path}'.")

    # Display result
    cv2.imshow("Original BGR Image", bgr_img)
    cv2.imshow("Q8 - Converted Grayscale", gray_img)
    print("Press any key to close windows (auto-close in 3s)...")
    cv2.waitKey(3000)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

