"""
Q21. Convert an 8-bit grayscale image into a 4-bit quantized image and display the result.

1. Approach/Logic:
   - An 8-bit image has 2^8 = 256 discrete levels (0 to 255).
   - A 4-bit quantized image reduces the number of allowable intensity levels to 2^4 = 16 levels.
   - Quantization step size = 256 / 16 = 16.
   - Discretization: `quantized_4bit = img // 16` (maps values to integers in [0, 15]).
   - For proper display on standard 8-bit monitors, stretch back across [0, 255]:
     `display_img = (quantized_4bit * (255 // 15)).astype(np.uint8)`
     (Alternatively, using bitwise shift: `(img >> 4) << 4`).
   - Save and display the quantized image. Observe visible banding (false contouring).

4. Short Explanation of Important Functions Used:
   - Integer division `//` or bit-shifting `>>`: Reduces continuous range into 16 discrete bins.
   - `cv2.imshow()`, `cv2.imwrite()`: Displays and saves the quantized output.

5. Observation/Result:
   - In 4-bit quantization (16 levels), smooth gradients begin showing subtle step-like bands ("false contouring"), but major visual structures remain recognizable.
"""

import cv2
import numpy as np
import sys

def quantize_image(gray_img: np.ndarray, bits: int) -> tuple[np.ndarray, np.ndarray]:
    num_levels = 2 ** bits
    step = 256 // num_levels

    # Quantize into discrete bins [0 .. num_levels-1]
    levels = (gray_img // step).astype(np.uint8)

    # Scale back to [0 .. 255] for visual rendering on 8-bit monitors
    scale_factor = 255 // (num_levels - 1)
    display_img = (levels * scale_factor).astype(np.uint8)

    return levels, display_img

def main():
    image_path = "sample.jpg"
    gray = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    if gray is None:
        print(f"Error: Unable to load '{image_path}'")
        sys.exit(1)

    # 4-bit quantization (16 distinct gray levels)
    levels, display_4bit = quantize_image(gray, bits=4)

    unique_levels = np.unique(levels)
    unique_displays = np.unique(display_4bit)

    print("=" * 50)
    print("4-BIT IMAGE QUANTIZATION")
    print("=" * 50)
    print(f"Original Bit Depth     : 8 bits (256 levels: 0..255)")
    print(f"Quantized Bit Depth    : 4 bits (16 levels: 0..15)")
    print(f"Number of Unique Levels: {len(unique_levels)}")
    print(f"Discrete Level Values  : {unique_levels.tolist()}")
    print(f"Display Scaled Values  : {unique_displays.tolist()}")
    print("=" * 50)

    # Save output
    output_path = "output_quantized_4bit.png"
    cv2.imwrite(output_path, display_4bit)
    print(f"Saved 4-bit quantized image to '{output_path}'.")

    # Display comparison
    cv2.imshow("Original 8-bit Grayscale (256 levels)", gray)
    cv2.imshow("Q21 - 4-bit Quantized (16 levels)", display_4bit)
    print("Press any key to close windows (auto-close in 3s)...")
    cv2.waitKey(3000)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

