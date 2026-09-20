"""
Q15. Merge three separate image channels into a single color image.

1. Approach/Logic:
   - Separate an image into individual 2D channels (B, G, R).
   - Use `cv2.merge([b, g, r])` to combine the three 2D single-channel arrays back into a single 3-channel BGR image.
   - Verify that the merged image array is identical to the original image array using `np.array_equal()`.
   - Also demonstrate creating an isolated single-color display (e.g., pure Blue image by merging `[b, zeros, zeros]`).
   - Save and display the results.

4. Short Explanation of Important Functions Used:
   - `cv2.merge(mv)`: Combines several single-channel arrays into a multi-channel array. All input arrays must have the same size and depth.
   - `np.array_equal(a1, a2)`: Returns True if two arrays have identical shapes and elements.

5. Observation/Result:
   - Merging [b, g, r] perfectly reconstructs the original color image with zero loss.
"""

import cv2
import numpy as np
import sys

def main():
    image_path = "sample.jpg"
    img = cv2.imread(image_path)

    if img is None:
        print(f"Error: Unable to load '{image_path}'")
        sys.exit(1)

    # 1. Split into individual channels
    b, g, r = cv2.split(img)

    # 2. Merge back into BGR image
    merged_bgr = cv2.merge([b, g, r])

    # Verify identity
    is_identical = np.array_equal(img, merged_bgr)
    print("=" * 45)
    print("CHANNEL MERGING RESULTS")
    print("=" * 45)
    print(f"Merged Shape: {merged_bgr.shape}")
    print(f"Is merged image strictly equal to original? {is_identical}")
    print("=" * 45)

    # Create a pure Blue visualizer (B channel kept, G and R set to zero)
    zeros = np.zeros_like(b)
    pure_blue = cv2.merge([b, zeros, zeros])

    # Save output
    cv2.imwrite("output_merged_image.png", merged_bgr)
    cv2.imwrite("output_pure_blue.png", pure_blue)
    print("Saved 'output_merged_image.png' and 'output_pure_blue.png'.")

    # Display results
    cv2.imshow("Original / Merged Image", merged_bgr)
    cv2.imshow("Pure Blue Visualizer", pure_blue)
    print("Press any key to close windows (auto-close in 3s)...")
    cv2.waitKey(3000)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

