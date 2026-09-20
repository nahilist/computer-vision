"""
Q24. Crop a rectangular Region of Interest (ROI) from an image using user-provided coordinates.

1. Approach/Logic:
   - In computer vision, a Region of Interest (ROI) is a sub-region extracted for targeted processing.
   - Coordinates are given as `(x1, y1)` (top-left) and `(x2, y2)` (bottom-right).
   - In NumPy array slicing: `roi = img[y1:y2, x1:x2]`.
   - Validate that bounds are strictly within `[0, width]` and `[0, height]` and `x1 < x2`, `y1 < y2`.
   - Draw a visual rectangle on a copy of the original image to show where the ROI was cropped from.
   - Save and display the cropped ROI.

4. Short Explanation of Important Functions Used:
   - `img[y1:y2, x1:x2]`: NumPy slice extracting the sub-array rows y1..y2 and columns x1..x2.
   - `cv2.rectangle(img, pt1, pt2, color, thickness)`: Draws an outlined rectangle demarcating the crop region.

5. Observation/Result:
   - Slicing creates a clean sub-image matrix with shape `(y2-y1, x2-x1, C)`.
"""

import cv2
import sys

def crop_roi(image, x1: int, y1: int, x2: int, y2: int):
    h, w = image.shape[:2]

    # Validate coordinate ordering
    xmin, xmax = min(x1, x2), max(x1, x2)
    ymin, ymax = min(y1, y2), max(y1, y2)

    # Clamp to image boundaries
    xmin = max(0, min(xmin, w - 1))
    xmax = max(1, min(xmax, w))
    ymin = max(0, min(ymin, h - 1))
    ymax = max(1, min(ymax, h))

    if xmin >= xmax or ymin >= ymax:
        print(f"Error: Invalid ROI dimensions ({xmin}, {ymin}) to ({xmax}, {ymax}).")
        return None

    # NumPy array slicing: img[rows, cols] -> img[y1:y2, x1:x2]
    roi = image[ymin:ymax, xmin:xmax]
    return roi, (xmin, ymin, xmax, ymax)

def main():
    image_path = "sample.jpg"
    img = cv2.imread(image_path)

    if img is None:
        print(f"Error: Unable to load '{image_path}'")
        sys.exit(1)

    # User-provided coordinates (x1, y1) to (x2, y2)
    # Centered box covering the red circle
    x1, y1 = 120, 120
    x2, y2 = 280, 280

    result = crop_roi(img, x1, y1, x2, y2)
    if result is None:
        return
    roi, (xmin, ymin, xmax, ymax) = result

    print("=" * 50)
    print("REGION OF INTEREST (ROI) CROPPING")
    print("=" * 50)
    print(f"Original Image Size : {img.shape[1]} x {img.shape[0]}")
    print(f"Crop Bounding Box   : Top-Left=({xmin}, {ymin}) to Bottom-Right=({xmax}, {ymax})")
    print(f"Cropped ROI Size    : {roi.shape[1]} x {roi.shape[0]} ({roi.shape})")
    print("=" * 50)

    # Save cropped ROI
    output_path = "output_cropped_roi.png"
    cv2.imwrite(output_path, roi)
    print(f"Saved cropped ROI to '{output_path}'.")

    # Visual demonstration: Draw bounding box on original image copy
    annotated = img.copy()
    cv2.rectangle(annotated, (xmin, ymin), (xmax, ymax), (0, 255, 255), 2)
    cv2.putText(annotated, "Cropped ROI", (xmin, ymin - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)

    # Display results
    cv2.imshow("Original with ROI Box", annotated)
    cv2.imshow("Q24 - Cropped ROI", roi)
    print("Press any key to close windows (auto-close in 3s)...")
    cv2.waitKey(3000)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

