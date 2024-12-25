from PIL import Image, ImageFilter

def apply_filter(filepath, outputpath, filter_name):
    try:
        image = Image.open(filepath)
        filters = {
            "BLUR": ImageFilter.BLUR,
            "CONTOUR": ImageFilter.CONTOUR,
            "DETAIL": ImageFilter.DETAIL,
            "EMBOSS": ImageFilter.EMBOSS,
            "SHARPEN": ImageFilter.SHARPEN,
        }
        if filter_name in filters:
            filtered_image = image.filter(filters[filter_name])
            filtered_image.save(outputpath)
            print(f"Filter applied and saved to {outputpath}.")
        else:
            print("Filter not found. Choose from: BLUR, CONTOUR, DETAIL, EMBOSS, SHARPEN.")
    except Exception as e:
        print(f"Error: {e}")

def resize_image(filepath, outputpath, width, height):
    try:
        image = Image.open(filepath)
        resized_image = image.resize((width, height))
        resized_image.save(outputpath)
        print(f"Image resized and saved to {outputpath}.")
    except Exception as e:
        print(f"Error: {e}")

def compress_image(filepath, outputpath, quality):
    try:
        image = Image.open(filepath)
        image.save(outputpath, quality=quality)
        print(f"Image compressed and saved to {outputpath}.")
    except Exception as e:
        print(f"Error: {e}")
