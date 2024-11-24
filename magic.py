import cv2
import os

# Specify the input and output folders
input_folder = r"C:\Users\bannu\OneDrive\Desktop\face-predict\face-predict\test\Akshaya"
output_folder = r"C:\Users\bannu\OneDrive\Desktop\charan_images"

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Loop through all files in the input folder
for filename in os.listdir(input_folder):
    # Construct the full file path
    input_path = os.path.join(input_folder, filename)

    # Check if it's a valid file (ignoring folders or non-image files)
    if os.path.isfile(input_path):
        try:
            # Read the RGB image
            rgb_image = cv2.imread(input_path)
            
            # Check if the image was loaded successfully
            if rgb_image is not None:
                # Convert the RGB image to grayscale
                gray_image = cv2.cvtColor(rgb_image, cv2.COLOR_RGB2GRAY)
                
                # Construct the output file path
                output_path = os.path.join(output_folder, filename)
                
                # Save the grayscale image
                cv2.imwrite(output_path, gray_image)
                print(f"Processed: {filename}")
            else:
                print(f"Skipping: {filename} (Could not load image)")
        except Exception as e:
            print(f"Error processing {filename}: {e}")
