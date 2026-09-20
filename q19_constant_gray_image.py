"""
Q19. Create a 256 × 256 grayscale image in which every pixel has intensity value 128.

1. Approach/Logic:
   - Generate a 2D matrix of shape (256, 256) filled with constant integer 128 using `np.full()`.
   - Ensure the dtype is explicitly set to `np.uint8` (standard 8-bit image type).
   - Intensity 128 corresponds exactly to mid-gray (halfway between 0=black and 255=white).
   - Save the image to disk with `cv2.imwrite()`.
   - Display the generated image with `cv2.imshow()`.

4. Short Explanation of Important Functions Used:
   - `np.full(shape, fill_value, dtype)`: Returns a new array of given shape and type, filled with `fill_value`.
   - `cv2.imwrite(filename, img)`: Saves the array as an image file.

5. Observation/Result:
   - The resulting image is uniformly mid-gray. The min, max, and mean are all exactly 128.0, and standard deviation is 0.0.
"""

import numpy as np
import cv2

def main():
    height, width = 256, 256
    intensity = 128

    # Create constant gray array
    gray_img = np.full((height, width), fill_value=intensity, dtype=np.uint8)

    print("=" * 45)
    print("CONSTANT 128 GRAYSCALE IMAGE")
    print("=" * 45)
    print(f"Shape           : {gray_img.shape}")
    print(f"Data type       : {gray_img.dtype}")
    print(f"Min intensity   : {np.min(gray_img)}")
    print(f"Max intensity   : {np.max(gray_img)}")
    print(f"Mean intensity  : {np.mean(gray_img)}")
    print(f"Std deviation   : {np.std(gray_img)}")
    print("=" * 45)

    # Save to disk
    output_path = "output_constant_gray_128.png"
    cv2.imwrite(output_path, gray_img)
    print(f"Image saved to '{output_path}'.")

    # Display image
    cv2.imshow("Q19 - Constant Gray (128)", gray_img)
    print("Press any key to close window (auto-close in 3s)...")
    cv2.waitKey(3000)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

