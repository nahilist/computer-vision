"""
Q14. Split a color image into its B, G, and R channels and display each channel.

1. Approach/Logic:
   - Read color image with `cv2.imread()`.
   - Use `cv2.split(img)` to decompose the image into 3 separate 2D matrices: `b`, `g`, and `r`.
   - Alternatively, note that NumPy slicing `img[:, :, 0]` is computationally more efficient.
   - When displayed directly as 2D matrices, each channel appears as a grayscale intensity map representing the brightness of that color.
   - Save the individual channel images and display them.

4. Short Explanation of Important Functions Used:
   - `cv2.split(m)`: Divides a multi-channel array into several single-channel arrays.
   - `cv2.imshow(winname, mat)`: Renders each single channel.

5. Observation/Result:
   - Each channel is a 2D array of shape (H, W). Regions with high blue intensity appear bright white in the Blue channel image, and dark in regions with little or no blue.
"""

import cv2
import sys

def main():
    image_path = "sample.jpg"
    img = cv2.imread(image_path)

    if img is None:
        print(f"Error: Unable to load '{image_path}'")
        sys.exit(1)

    # 1. Split using cv2.split
    b, g, r = cv2.split(img)

    print("=" * 45)
    print("SPLIT CHANNELS INFORMATION")
    print("=" * 45)
    print(f"Original Shape : {img.shape}")
    print(f"Blue Channel   : shape={b.shape}, min={b.min()}, max={b.max()}")
    print(f"Green Channel  : shape={g.shape}, min={g.min()}, max={g.max()}")
    print(f"Red Channel    : shape={r.shape}, min={r.min()}, max={r.max()}")
    print("=" * 45)

    # Save channels
    cv2.imwrite("output_channel_blue.png", b)
    cv2.imwrite("output_channel_green.png", g)
    cv2.imwrite("output_channel_red.png", r)
    print("Saved individual channel images to disk.")

    # Display channels
    cv2.imshow("Original BGR Image", img)
    cv2.imshow("Blue Channel (Grayscale Intensity)", b)
    cv2.imshow("Green Channel (Grayscale Intensity)", g)
    cv2.imshow("Red Channel (Grayscale Intensity)", r)

    print("Press any key to close windows (auto-close in 3s)...")
    cv2.waitKey(3000)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

