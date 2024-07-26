from rembg import remove
import requests
from PIL import Image
from io import BytesIO  # helps image reading using byte
import os
os.makedirs('originals',exist_ok=True)
os.makedirs('masked', exist_ok=True)
image_path = 'nameLogo.png'
image = Image.open(image_path)
imgar = Image.open(image_path)
imgar = remove(imgar)
masked_path = 'masked/' + os.path.basename(image_path)
imgar.save(masked_path)
