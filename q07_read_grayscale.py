"""
Q7. Read an image directly in grayscale mode and display it.

1. Approach/Logic:
   - Use `cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)` (or flag `0`) to decode the image directly as a single-channel grayscale array.
   - Confirm that the shape has only 2 dimensions: `(height, width)` instead of 3.
   - Save the grayscale result as `output_grayscale_direct.jpg`.
   - Display the image using `cv2.imshow()`.

4. Short Explanation of Important Functions Used:
   - `cv2.imread(path, cv2.IMREAD_GRAYSCALE)`: Decodes and converts the image directly to an 8-bit single-channel grayscale image upon reading.
   - `cv2.imshow(winname, mat)`: Displays the single-channel image correctly using gray levels.

5. Observation/Result:
   - The loaded image array has shape `(400, 400)` with `len(shape) == 2`. Memory footprint is reduced to 1/3 compared to a 3-channel BGR image.
"""

import cv2
import sys

def main():
    image_path = "sample.jpg"

    # Read directly in grayscale mode
    gray_img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    if gray_img is None:
        print(f"Error: Unable to load image '{image_path}'.")
        sys.exit(1)

    print(f"Grayscale image loaded successfully!")
    print(f"Shape : {gray_img.shape} (2D array, 1 channel)")
    print(f"dtype : {gray_img.dtype}")

    # Save output copy
    output_path = "output_grayscale_direct.jpg"
    cv2.imwrite(output_path, gray_img)
    print(f"Saved grayscale copy to: {output_path}")

    # Display image
    window_name = "Q7 - Direct Grayscale (Press any key to close)"
    cv2.imshow(window_name, gray_img)
    print("Displaying window. Press any key to close (or closes automatically in 3s)...")
    cv2.waitKey(3000)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

