om rembg import remove
from PIL import Image, ImageOps
import io

# Open the image file
with open('input_image.png', 'rb') as img_file:
    img_data = img_file.read()

# Remove the background
output_data = remove(img_data)

# Load the output image
output_image = Image.open(io.BytesIO(output_data))

# Create a solid background (white)
new_background = Image.new('RGB', output_image.size, (255, 255, 255))

# Paste the image without the background on top of the white background
new_background.paste(output_image, mask=output_image.split()[3])

# Save the final image
new_background.save('new_background_image.png')