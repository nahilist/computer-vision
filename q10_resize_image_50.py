"""
Q10. Resize an image to 50% of its original width and height.

1. Approach/Logic:
   - Read the image and get original dimensions `(h, w) = img.shape[:2]`.
   - Calculate target dimensions: `new_w = int(w * 0.5)` and `new_h = int(h * 0.5)`.
   - Use `cv2.resize()`. Note that `dsize` expects `(width, height)` which is opposite of NumPy's `(height, width)`.
   - Alternatively, use scaling factors `fx=0.5, fy=0.5` with `dsize=None`.
   - Use `interpolation=cv2.INTER_AREA` which is best practice for downsampling/shrinking.
   - Save and display the resized image.

4. Short Explanation of Important Functions Used:
   - `cv2.resize(src, dsize, fx, fy, interpolation)`: Resizes an image. `dsize=(width, height)`.
   - `cv2.INTER_AREA`: Pixel area relation interpolation, preferred for decimation/shrinking to avoid moire artifacts.

5. Observation/Result:
   - Original resolution 400x400 is reduced to 200x200 pixels. Total pixels decrease by 75% (from 160k to 40k).
"""

import cv2
import sys

def main():
    image_path = "sample.jpg"
    img = cv2.imread(image_path)

    if img is None:
        print(f"Error: Unable to load image '{image_path}'.")
        sys.exit(1)

    orig_h, orig_w = img.shape[:2]

    # Method 1: Using explicit dsize (width, height)
    target_w = int(orig_w * 0.5)
    target_h = int(orig_h * 0.5)
    resized_img = cv2.resize(img, (target_w, target_h), interpolation=cv2.INTER_AREA)

    print("=" * 45)
    print("IMAGE RESIZING (50%)")
    print("=" * 45)
    print(f"Original Dimensions : {orig_w} x {orig_h}")
    print(f"Resized Dimensions  : {resized_img.shape[1]} x {resized_img.shape[0]}")
    print(f"Original Pixel Count: {img.shape[0] * img.shape[1]:,}")
    print(f"Resized Pixel Count : {resized_img.shape[0] * resized_img.shape[1]:,}")
    print("=" * 45)

    # Save output
    output_path = "output_resized_50.jpg"
    cv2.imwrite(output_path, resized_img)
    print(f"Saved 50% resized image to '{output_path}'.")

    # Display both
    cv2.imshow("Original (100%)", img)
    cv2.imshow("Resized (50%)", resized_img)
    print("Press any key to close windows (auto-close in 3s)...")
    cv2.waitKey(3000)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

