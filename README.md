# Image Manipulation Tool

This project is a Python-based Image Manipulation Tool using the `Pillow` library. It allows users to:
- Apply various filters to images.
- Resize images to desired dimensions.
- Compress images by reducing quality.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/Image-Manipulation-Tool.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Image-Manipulation-Tool
   ```
3. Install the required library:
   ```bash
   pip install pillow
   ```

## Usage
### 1. Apply a Filter
```python
from image_tool import apply_filter
apply_filter("input.jpg", "output.jpg", "BLUR")
```
### 2. Resize an Image
```python
from image_tool import resize_image
resize_image("input.jpg", "output.jpg", 200, 200)
```
### 3. Compress an Image
```python
from image_tool import compress_image
compress_image("input.jpg", "compressed.jpg", 50)
```

## Example Images
- `example_images/input_image.jpg`
- `example_images/output_image.jpg`

## Features
- Supports filters like BLUR, CONTOUR, DETAIL, EMBOSS, SHARPEN.
- Easy resizing with specified width and height.
- Image compression to reduce file size.

## License
This project is licensed under the MIT License.
