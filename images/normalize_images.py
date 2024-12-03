import nibabel as nib
import numpy as np
import os

def normalize_image(input_path, output_path):
    img = nib.load(input_path)
    img_data = img.get_fdata()

    # Normalize data between 0 and 1
    normalized_data = (img_data - np.min(img_data)) / (np.max(img_data) - np.min(img_data))

    # Save normalized image
    normalized_img = nib.Nifti1Image(normalized_data, img.affine, img.header)
    nib.save(normalized_img, output_path)

# Paths for your images
input_images = ["IXI002-Guys-0828-T1.nii.gz", "IXI099-Guys-0748-T1.nii.gz"]
output_images = ["normalized_moving.nii.gz", "normalized_fixed.nii.gz"]

# Normalize each image
for input_image, output_image in zip(input_images, output_images):
    normalize_image(input_image, output_image)
    print(f"Normalized: {input_image} -> {output_image}")
