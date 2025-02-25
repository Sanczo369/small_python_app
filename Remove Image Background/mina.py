from rembg import remove
from PIL import Image

# Open the image file
with open('input_image.png', 'rb') as img_file:
    img_data = img_file.read()

# Remove the background
output_data = remove(img_data)

# Save the result
with open('output_image.png', 'wb') as out_file:
    out_file.write(output_data)