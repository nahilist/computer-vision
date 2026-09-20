"""
Q22. Convert an 8-bit grayscale image into a 2-bit quantized image and display the result.

1. Approach/Logic:
   - An 8-bit image has 2^8 = 256 intensity levels.
   - A 2-bit quantized image permits only 2^2 = 4 discrete intensity levels (0, 1, 2, 3).
   - Step size = 256 / 4 = 64.
   - Map pixels: `levels = gray // 64` (produces values in {0, 1, 2, 3}).
   - Scale back to standard 8-bit range [0, 255] for visual display:
     `display_img = levels * 85` (maps to {0, 85, 170, 255}).
   - Save and display the result. Notice severe posterization and stark contour borders.

4. Short Explanation of Important Functions Used:
   - Integer division `// 64`: Maps pixel values into 4 bins.
   - Scalar multiplication `* 85`: Stretches 4 levels uniformly across dynamic range [0..255].

5. Observation/Result:
   - In 2-bit quantization, dramatic posterization occurs. All subtle variations and textures collapse into only 4 broad tone regions.
"""

import cv2
import numpy as np
import sys

def quantize_2bit(gray_img: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    # 2-bit -> 4 levels: 0, 1, 2, 3
    num_levels = 4
    step = 256 // num_levels  # 64

    levels = (gray_img // step).astype(np.uint8)
    
    # Scale across [0, 255]: 0 -> 0, 1 -> 85, 2 -> 170, 3 -> 255
    scale_factor = 255 // (num_levels - 1)  # 85
    display_img = (levels * scale_factor).astype(np.uint8)

    return levels, display_img

def main():
    image_path = "sample.jpg"
    gray = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    if gray is None:
        print(f"Error: Unable to load '{image_path}'")
        sys.exit(1)

    levels, display_2bit = quantize_2bit(gray)

    print("=" * 50)
    print("2-BIT IMAGE QUANTIZATION")
    print("=" * 50)
    print(f"Original Bit Depth     : 8 bits (256 levels: 0..255)")
    print(f"Quantized Bit Depth    : 2 bits (4 levels: 0, 1, 2, 3)")
    print(f"Unique Quantized Bins  : {np.unique(levels).tolist()}")
    print(f"Display Intensities    : {np.unique(display_2bit).tolist()}")
    print("=" * 50)

    # Save output
    output_path = "output_quantized_2bit.png"
    cv2.imwrite(output_path, display_2bit)
    print(f"Saved 2-bit quantized image to '{output_path}'.")

    # Display comparison
    cv2.imshow("Original 8-bit Grayscale (256 levels)", gray)
    cv2.imshow("Q22 - 2-bit Quantized (4 levels)", display_2bit)
    print("Press any key to close windows (auto-close in 3s)...")
    cv2.waitKey(3000)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

