"""
Q9. Display an image using Matplotlib and hide the axis.

1. Approach/Logic:
   - Read image with OpenCV's `cv2.imread()`.
   - Remember: OpenCV loads color channels in BGR order, but Matplotlib expects RGB order.
   - Convert from BGR to RGB using `cv2.cvtColor(img, cv2.COLOR_BGR2RGB)`.
   - Use `plt.imshow()` to render the image.
   - Call `plt.axis('off')` to remove pixel coordinate ticks and frame borders.
   - Save the plot as `output_matplotlib.png` and display using `plt.show()`.

4. Short Explanation of Important Functions Used:
   - `cv2.cvtColor(img, cv2.COLOR_BGR2RGB)`: Swaps B and R channels so colors display accurately in Matplotlib.
   - `plt.imshow(X)`: Displays 2D or 3D array as an image.
   - `plt.axis('off')`: Hides coordinate axes, ticks, and labels.
   - `plt.savefig(fname)`: Saves the current Matplotlib figure to disk.

5. Observation/Result:
   - Without BGR-to-RGB conversion, blue appears red and red appears blue.
   - `plt.axis('off')` removes coordinate rulers, leaving only the clean image canvas.
"""

import cv2
import matplotlib.pyplot as plt
import sys

def main():
    image_path = "sample.jpg"
    bgr_img = cv2.imread(image_path)

    if bgr_img is None:
        print(f"Error: Unable to load image '{image_path}'.")
        sys.exit(1)

    # Convert BGR to RGB for Matplotlib
    rgb_img = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2RGB)

    # Plot using Matplotlib
    plt.figure(figsize=(6, 6))
    plt.imshow(rgb_img)
    plt.title("Matplotlib Display (Axis Hidden)", fontsize=14)
    plt.axis("off")  # Hide axis

    # Save figure to disk
    output_path = "output_matplotlib.png"
    plt.savefig(output_path, bbox_inches="tight", dpi=150)
    print(f"Saved plot without axis to '{output_path}'.")

    # Display plot
    print("Displaying figure via Matplotlib (close window to finish)...")
    plt.show(block=False)
    plt.pause(2)
    plt.close()

if __name__ == "__main__":
    main()

