# Image Assets Generator

This script processes image files (SVG, PNG, JPG, and JPEG) to generate resized assets suitable for Swift projects. It ensures proper formatting of filenames and produces 1x, 2x, and 3x image assets.

## Features

- Converts SVG files to PNG format.
- Resizes images to 1x, 2x, and 3x scales.
- Automatically reformats filenames by:
  - Removing the `ic_` prefix.
  - Removing underscores (`_`).
  - Capitalizing the first letter of each word.
- Outputs the processed images into a specified directory.

## Prerequisites

Ensure you have the following installed:

- Python 3.9 or later
- Required Python libraries:
  - `Pillow`
  - `cairosvg`

Install the required libraries using pip:

```bash
pip install pillow cairosvg
```

## Usage

### Input Folder

Place your image files in a folder named `images` (or any other folder of your choice).

### Output Directory

The processed image assets will be saved in a folder named `output_assets` (or a folder of your choice).

### Running the Script

1. Save the script as `main.py`.
2. Run the script:
   ```bash
   python main.py
   ```

### Example Input

#### Input Filename

`ic_change_password.svg`

### Example Output

#### Output Filenames

- `ChangePassword@1x.png`
- `ChangePassword@2x.png`
- `ChangePassword@3x.png`

## Script Workflow

1. **File Processing**:
   - Reads files from the specified input folder.
   - Processes SVG, PNG, JPG, and JPEG files.
2. **Filename Transformation**:
   - Removes the `ic_` prefix.
   - Removes underscores and capitalizes the first letter of each word.
3. **Image Conversion**:
   - Converts SVG files to PNG format using `cairosvg`.
   - Resizes images to 1x, 2x, and 3x scales using `Pillow`.
4. **Output**:
   - Saves processed images to the output folder with the transformed filename.

## Customization

### Input and Output Directories

Modify the `input_image_folder` and `output_directory` variables in the script to use different folders:

```python
input_image_folder = "your_input_folder"
output_directory = "your_output_folder"
```

### Supported File Formats

To add or remove supported file formats, update the `file_extension` check in the script:

```python
if file_extension in ['svg', 'png', 'jpg', 'jpeg']:
```

## Troubleshooting

### Common Issues

1. **Missing Libraries**:
   If you encounter a `ModuleNotFoundError`, ensure you have installed all required libraries:
   ```bash
   pip install pillow cairosvg
   ```
2. **File Not Processed**:
   Ensure your input files are in the correct folder and have supported extensions (`svg`, `png`, `jpg`, `jpeg`).

### Error Handling

The script logs errors during processing. If an error occurs, review the output for details.

## License

This script is open-source and free to use for personal or commercial projects.
