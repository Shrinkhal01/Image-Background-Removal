from rembg import remove
import requests
from PIL import Image #the image manipulator
from io import BytesIO  # handle img data as bytes
import os #imports the os library for managing the file paths
os.makedirs('originals',exist_ok=True)#makes à folder named originals
os.makedirs('masked', exist_ok=True)#makes a folder named masked
image_path = 'nameLogo.png'#the path of the file whose background is to be removed
image = Image.open(image_path)#opens the image in the pa
imgar = remove(image) # here is the function that is working in order to remove the background
masked_path = 'masked/' + os.path.basename(image_path) # where to save here to save
imgar.save(masked_path)
