"""
Q23. Downsample an image by a factor of 2 in both width and height and print the original and new resolutions.

1. Approach/Logic:
   - Spatial downsampling reduces spatial resolution by picking every k-th pixel or averaging local neighborhoods.
   - Method 1 (NumPy sub-sampling): Slicing with step 2: `img[::2, ::2]` (skips alternate rows and columns).
   - Method 2 (OpenCV area downsampling): `cv2.resize(img, (w//2, h//2), interpolation=cv2.INTER_AREA)` or `cv2.pyrDown()`.
   - Print original vs. new resolution `(width, height)`.
   - Save the downsampled image.

4. Short Explanation of Important Functions Used:
   - `img[::2, ::2]`: Strided array slicing that samples every 2nd pixel in row and column dimensions.
   - `cv2.resize(src, dsize, interpolation=cv2.INTER_AREA)`: Resamples the image while averaging pixel blocks to minimize aliasing.

5. Observation/Result:
   - Downsampling by a factor of 2 halves both width and height, reducing total pixel count to 1/4 (25%) of the original image.
"""

import cv2
import sys

def main():
    image_path = "sample.jpg"
    img = cv2.imread(image_path)

    if img is None:
        print(f"Error: Unable to load '{image_path}'")
        sys.exit(1)

    orig_h, orig_w = img.shape[:2]

    # Method 1: NumPy strided downsampling (decimation)
    downsampled_slice = img[::2, ::2]
    new_h1, new_w1 = downsampled_slice.shape[:2]

    # Method 2: OpenCV area interpolation (anti-aliased)
    downsampled_cv = cv2.resize(img, (orig_w // 2, orig_h // 2), interpolation=cv2.INTER_AREA)
    new_h2, new_w2 = downsampled_cv.shape[:2]

    print("=" * 50)
    print("IMAGE DOWNSAMPLING (FACTOR OF 2)")
    print("=" * 50)
    print(f"Original Resolution   : {orig_w} x {orig_h} ({orig_w * orig_h:,} pixels)")
    print(f"Downsampled Resolution: {new_w2} x {new_h2} ({new_w2 * new_h2:,} pixels)")
    print(f"Reduction Ratio       : 4x reduction in total pixel count (25% retained)")
    print("=" * 50)

    # Save output
    output_path = "output_downsampled.jpg"
    cv2.imwrite(output_path, downsampled_cv)
    print(f"Saved downsampled image to '{output_path}'.")

    # Display comparison
    cv2.imshow("Original (400x400)", img)
    cv2.imshow("Downsampled (200x200)", downsampled_cv)
    print("Press any key to close windows (auto-close in 3s)...")
    cv2.waitKey(3000)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

