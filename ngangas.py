import cv2
import numpy as np

# Load the image using OpenCV
image = cv2.imread(image_path)

# Convert the image to RGB (OpenCV loads images in BGR format)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Manually define the coordinates of the sticker area to be removed
# Coordinates are in the format (x, y, width, height)
sticker_area = (230, 190, 140, 140)  # These values are approximate and might need adjustment

# Create a mask for the sticker area
mask = np.zeros(image_rgb.shape[:2], dtype=np.uint8)
x, y, w, h = sticker_area
mask[y:y+h, x:x+w] = 255

# Inpaint the sticker area using the mask
inpainted_image = cv2.inpaint(image_rgb, mask, 3, cv2.INPAINT_TELEA)

# Convert the result back to BGR for saving with OpenCV
inpainted_image_bgr = cv2.cvtColor(inpainted_image, cv2.COLOR_RGB2BGR)

# Save the edited image
output_path = "/mnt/data/edited_image.jpg"
cv2.imwrite(output_path, inpainted_image_bgr)

output_path
