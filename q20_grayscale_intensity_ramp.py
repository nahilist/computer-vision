"""
Q20. Create and display a grayscale intensity ramp whose intensity gradually changes from 0 to 255.

1. Approach/Logic:
   - Construct a horizontal intensity gradient (ramp) of size 256 x 256.
   - Use `np.tile()` or `np.linspace()`:
     Create a 1D vector `np.arange(256, dtype=np.uint8)` where each column index from 0 to 255 holds value 0 to 255.
   - Tile/repeat this 1D row 256 times vertically: `np.tile(row, (height, 1))`.
   - The result is a smooth horizontal gradient starting from 0 (pitch black) on the left to 255 (pure white) on the right.
   - Save and display the ramp.

4. Short Explanation of Important Functions Used:
   - `np.arange(stop, dtype)`: Generates evenly spaced values from 0 up to stop-1.
   - `np.tile(A, reps)`: Constructs an array by repeating `A` the number of times given by `reps`.

5. Observation/Result:
   - A smooth gradient visualizes the complete dynamic range of an 8-bit grayscale image [0..255].
"""

import numpy as np
import cv2

def main():
    height = 256
    width = 256

    # Create a 1D row ramp from 0 to 255
    ramp_row = np.arange(256, dtype=np.uint8).reshape(1, width)

    # Repeat vertically to create a 256x256 2D matrix
    intensity_ramp = np.tile(ramp_row, (height, 1))

    print("=" * 45)
    print("GRAYSCALE INTENSITY RAMP (0 -> 255)")
    print("=" * 45)
    print(f"Dimensions       : {width} x {height}")
    print(f"Leftmost column  : intensity {intensity_ramp[:, 0].mean():.0f} (Black)")
    print(f"Middle column    : intensity {intensity_ramp[:, 128].mean():.0f} (Mid-Gray)")
    print(f"Rightmost column : intensity {intensity_ramp[:, 255].mean():.0f} (White)")
    print("=" * 45)

    # Save output
    output_path = "output_intensity_ramp.png"
    cv2.imwrite(output_path, intensity_ramp)
    print(f"Ramp image saved to '{output_path}'.")

    # Display ramp
    cv2.imshow("Q20 - Grayscale Intensity Ramp (0 to 255)", intensity_ramp)
    print("Press any key to close window (auto-close in 3s)...")
    cv2.waitKey(3000)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

