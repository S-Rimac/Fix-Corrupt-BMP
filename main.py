from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Load corrupt BMP image
image_path = 'corrupt.bmp'
image = Image.open(image_path)

# Convert image to numpy array
image_np = np.array(image)

# Check shape and data type of the image array
print("Image shape: ", image_np.shape)
print("Image data type: ", image_np.dtype)

# Visualize the image using matplotlib
plt.imshow(image_np)
plt.show()

# Fix BMP header corruption
bmp_header = b'BM' + image_np[2:6].tobytes()  # Extract BMP header from image array
image_np[0:14] = np.frombuffer(bmp_header, dtype=np.uint8)  # Update BMP header in image array

# Convert numpy array back to Image object
image_fixed = Image.fromarray(image_np)

# Save fixed image to a new file using PIL
image_fixed.save('fixed.bmp')
