from PIL import Image
Image.MAX_IMAGE_PIXELS = None
def get_image_info(image_path):
    try:
        # Open the image file
        with Image.open(image_path) as img:
            # Get image dimensions
            width, height = img.size

            # Get image format
            image_format = img.format

            # Get color mode
            color_mode = img.mode

            # Create a dictionary to store the information
            image_info = {
                "Width": width,
                "Height": height,
                "Format": image_format,
                "Color Mode": color_mode
            }

            return image_info
    except Exception as e:
        print("Error:", e)

def save_info_to_txt(info, txt_file):
    try:
        with open(txt_file, "w") as f:
            for key, value in info.items():
                f.write(f"{key}: {value}\n")
        print("Image information saved to", txt_file)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    # Path to the certificate background image
    image_path = "../certificate/cert_background.png"

    # Path to save the information
    txt_file = "image-property.txt"

    # Get image information
    image_info = get_image_info(image_path)

    # Save image information to a text file
    save_info_to_txt(image_info, txt_file)
