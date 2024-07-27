from rembg import remove
import requests
from PIL import Image
from io import BytesIO  # helps image reading using byte
import os
os.makedirs('originals',exist_ok=True)#makes à folder named originals
os.makedirs('masked', exist_ok=True)#makes a folder named masked
image_path = 'nameLogo.png'#the name of the file whose background is to be removed
image = Image.open(image_path)#opens the image in the path specified
imgar = Image.open(image_path)
imgar = remove(imgar)
masked_path = 'masked/' + os.path.basename(image_path)
imgar.save(masked_path)
