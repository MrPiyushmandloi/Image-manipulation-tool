# Image Manipulation Tool

This project is a Python-based Image Manipulation Tool using the `Pillow` library. It allows users to:
- Apply various filters to images.
- Resize images to desired dimensions.
- Compress images by reducing quality.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/MrPiyushmandloi/Image-manipulation-tool.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Image-manipulation-tool
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
### How It Works:
1. `![Original Image](IMG_20241225_104631.jpg)` will display the original image you uploaded.
2. `![Blurred Image](New Project 191 [21185C7].png)` will display the blurred image.



## Features
- Supports filters like BLUR, CONTOUR, DETAIL, EMBOSS, SHARPEN.
- Easy resizing with specified width and height.
- Image compression to reduce file size.

  ## Sample
[!input](https://raw.githubusercontent.com/MrPiyushmandloi/Image-manipulation-tool/main/IMG_20241225_104631.jpg)
## 
[!output](https://raw.githubusercontent.com/MrPiyushmandloi/Image-manipulation-tool/main/output.jpg)
  
## License
This project is licensed under the MIT License.
