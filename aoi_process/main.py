import os
import shutil
import json
from PIL import Image
from datetime import datetime


def process_images(input_dir, output_dir, dataset_name):
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Initialize metadata structure
    metadata = {
        "version": "1.0.0",
        "description": f"{dataset_name} dataset for Metadata",
        "timestamp": datetime.utcnow().replace(microsecond=0).isoformat() + "Z",
        "machineInfo": {
            "machineId": "dummy",
            "jobType": "test",
            "batchId": None,
            "serialNumber": "0123123"
        },
        "aoiDefects": {
            "count": 1,
            "details": [
                {
                    "defectType": "MissingComponent",
                    "count": "1"
                }
            ]
        },
        "imageInfo": {}
    }

    # Process each image in the input directory
    for filename in os.listdir(input_dir):
        if filename.endswith(('.jpg', '.jpeg', '.png', '.tiff')):
            # Get image path
            image_path = os.path.join(input_dir, filename)

            # Create a new folder for each image and copy the image
            new_folder = os.path.join(output_dir, os.path.splitext(filename)[0])
            os.makedirs(new_folder, exist_ok=True)
            shutil.copy(image_path, os.path.join(new_folder, filename))

            # Get image width and height
            with Image.open(image_path) as img:
                width, height = img.size

            # Update metadata with image information
            metadata["imageInfo"] = {
                "imageType": "full",
                "path": f"./{filename}",
                "golden-ref": f"./{filename}",
                "golden-refWidth": width,
                "golden-refHeight": height,
                "layer": "0",
                "cropInfo": [
                    {
                        "id": "dummy",
                        "packageType": "dummy",
                        "partNumber": "151574-00",
                        "crop": {
                            "cropType": "bbox",
                            "coordinates": {
                                "left": 0,
                                "top": 0,
                                "width": width,
                                "height": height
                            }
                        },
                        "rotation_angle": 0,
                        "aoiDefectInfo": {
                            "defectType": "MissingComponent"
                        }
                    }
                ]
            }

            # Write metadata to JSON file
            with open(os.path.join(new_folder, 'aoi_metadata.json'), 'w') as json_file:
                json.dump(metadata, json_file, indent=4)

    print("Processing complete.")


# Example usage
dataset_name = 'xxxx'
input_directory = "./Images"
output_directory = "./Dataset/"
process_images(input_directory, output_directory, dataset_name)
