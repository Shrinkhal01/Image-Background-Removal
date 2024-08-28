# Image Background Removal

A Python script to remove the background from images using the rembg library.

## Project Structure

```plaintext
Image-Background-Removal/
│
├── originals/         # Directory for original images
├── masked/            # Directory for images with removed background
├── main.py            # Main script for background removal
├── requirements.txt   # Python dependencies
└── README.md          # Project documentation
```

## How to Execute the Program

This script removes the background from an image using the `rembg` library and saves both the original and the processed images in separate folders.

### Prerequisites

Make sure you have the following libraries installed:

- `rembg`
- `requests`
- `Pillow`

You can install them using pip:

```bash
pip install rembg requests Pillow
```
