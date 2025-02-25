from rembg import remove
from PIL import Image
import io

# Open the image file
with open('input_image.png', 'rb') as img_file:
    img_data = img_file.read()

# Remove the background
output_data = remove(img_data)

# Convert the output to an image
output_image = Image.open(io.BytesIO(output_data))

# Convert and save as JPEG
output_image.convert('RGB').save('output_image.jpg', 'JPEG')