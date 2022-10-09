import os
from PIL import Image

FromDir = 'img'
ToDir = 'resize'

# Enter appropriate width
Width = 250

# Enter appropriate height
Height = 180

imgFiles = os.listdir(FromDir)

for file in imgFiles:
    img = Image.open(os.path.join(FromDir, file))
    resized_img = img.resize((Width, Height))
    resized_img.save(os.path.join(ToDir, file))
