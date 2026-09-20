"""
Q1. Read an image using OpenCV and display it.

1. Approach/Logic:
   - Use `cv2.imread()` to load the image matrix from the specified file path into memory as a NumPy BGR array.
   - Use `cv2.imshow()` to open a graphical window presenting the image.
   - Use `cv2.waitKey(0)` to pause execution and keep the window visible until any key is pressed.
   - Use `cv2.destroyAllWindows()` to properly close and clean up all allocated OpenCV GUI windows.

4. Short Explanation of Important Functions Used:
   - `cv2.imread(filename, flags)`: Loads an image from the specified path. By default, loads in BGR 3-channel format (`cv2.IMREAD_COLOR`).
   - `cv2.imshow(winname, mat)`: Displays the image array in an interactive window with the specified window title.
   - `cv2.waitKey(delay)`: Waits for a key event for `delay` milliseconds. If `delay=0`, it waits indefinitely until a key is pressed.
   - `cv2.destroyAllWindows()`: Destroys and cleans up all active OpenCV display windows.

5. Observation/Result:
   - The image is loaded into memory as a NumPy ndarray of shape (H, W, C) with dtype uint8.
   - An interactive window pops up displaying the image with correct BGR color rendering.
"""

import cv2
import os

def main():
    image_path = "sample.jpg"

    if not os.path.exists(image_path):
        print(f"Error: File '{image_path}' not found.")
        return

    # 1. Read the image
    img = cv2.imread(image_path)

    # Check if loaded successfully
    if img is None:
        print(f"Error: Unable to load image from '{image_path}'.")
        return

    print(f"Image successfully read with shape: {img.shape}")

    # 2. Display the image in a window
    window_name = "Q1 - Display Image (Press any key to close)"
    cv2.imshow(window_name, img)

    # 3. Wait for user key press to exit
    print("Displaying window. Press any key to close...")
    cv2.waitKey(0)

    # 4. Clean up window
    cv2.destroyAllWindows()
    print("Window closed.")

if __name__ == "__main__":
    main()

