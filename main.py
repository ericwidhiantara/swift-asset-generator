import os
from PIL import Image
import cairosvg

def convert_svg_to_png(svg_path, output_png_path):
    """
    Converts an SVG file to a PNG file.

    :param svg_path: Path to the input SVG file.
    :param output_png_path: Path to save the output PNG file.
    """
    cairosvg.svg2png(url=svg_path, write_to=output_png_path)

def generate_image_assets(input_image_folder, output_directory):
    """
    Generate 1x, 2x, and 3x image assets for Swift projects from images in the specified folder.

    :param input_image_folder: Folder containing input images.
    :param output_directory: Directory where the generated assets will be saved.
    """
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    try:
        # Loop through all files in the input image folder
        for filename in os.listdir(input_image_folder):
            # Process SVG, PNG, JPG, and JPEG images
            file_extension = filename.lower().split('.')[-1]
            if file_extension in ['svg', 'png', 'jpg', 'jpeg']:

                input_image_path = os.path.join(input_image_folder, filename)

                # Remove 'ic_' prefix if it exists
                base_filename = filename.lstrip("ic_")

                # Split by underscores, capitalize each part, and join them back together
                base_filename = ''.join(word.capitalize() for word in base_filename.split('_'))

                # If the file is an SVG, convert it to PNG
                if file_extension == 'svg':
                    temp_png_path = os.path.join(output_directory, f"{os.path.splitext(base_filename)[0]}.png")
                    convert_svg_to_png(input_image_path, temp_png_path)
                    input_image_path = temp_png_path  # Use the converted PNG for resizing
                    print(f"Converted SVG to PNG: {temp_png_path}")

                # Open the image (either the original PNG or the converted one)
                img = Image.open(input_image_path)

                # Get the original size of the image
                width, height = img.size

                # Generate and save 1x, 2x, and 3x images
                sizes = {
                    "1x": (width, height),
                    "2x": (width * 2, height * 2),
                    "3x": (width * 3, height * 3),
                }

                for scale, size in sizes.items():
                    resized_img = img.resize(size, Image.ANTIALIAS)
                    file_name = f"{os.path.splitext(base_filename)[0]}@{scale}.png"  # Naming without 'ic' prefix
                    output_path = os.path.join(output_directory, file_name)
                    resized_img.save(output_path, "PNG")
                    print(f"Generated: {output_path}")

    except Exception as e:
        print(f"Error processing images: {e}")

# Example usage
input_image_folder = "images"  # Folder containing your input images
output_directory = "output_assets"  # Desired output directory for generated images
generate_image_assets(input_image_folder, output_directory)
