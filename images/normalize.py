import nibabel as nib
import numpy as np
import os

def normalize_nifti(input_path, output_path):
    """
    Normalize a 3D NIfTI image to range [0, 1].
    
    Args:
        input_path (str): Path to the input .nii.gz file.
        output_path (str): Path to save the normalized .nii.gz file.
    """
    # Load the NIfTI file
    nii_img = nib.load(input_path)
    img_data = nii_img.get_fdata()  # Get the 3D image data as a numpy array

    # Normalize the image data to range [0, 1]
    img_data = img_data.astype('float32')  # Ensure float for division
    img_data -= np.min(img_data)  # Shift the data to start from 0
    img_data /= np.max(img_data)  # Scale the maximum value to 1

    # Save the normalized data as a new NIfTI file
    normalized_nii = nib.Nifti1Image(img_data, affine=nii_img.affine, header=nii_img.header)
    nib.save(normalized_nii, output_path)
    print(f"Normalized image saved to {output_path}")

if __name__ == "__main__":
    input_dir = "./images"  # Directory containing the .nii.gz files
    output_dir = "./normalized_images"  # Directory to save the normalized images

    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Iterate over .nii.gz files in the input directory
    for file_name in os.listdir(input_dir):
        if file_name.endswith(".nii.gz"):
            input_path = os.path.join(input_dir, file_name)
            output_path = os.path.join(output_dir, file_name)

            # Normalize the NIfTI file
            normalize_nifti(input_path, output_path)
