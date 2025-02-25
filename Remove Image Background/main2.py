from rembg import remove
from PIL import Image
import io

# Open the image file
with open('input_image.png', 'rb') as img_file:
    img_data = img_file.read()

# Remove the background
output_data = remove(img_data)

# Load the output image
output_image = Image.open(io.BytesIO(output_data))

# Resize the image
resized_image = output_image.resize((300, 300))

# Save the resized image
resized_image.save('resized_output_image.png')