import SimpleITK as sitk
import numpy as np
import os
import skimage


# Function to preprocess images (optional, resampling)
def preprocess_image(image, reference_spacing=None):
    if reference_spacing is not None:
        resampler = sitk.ResampleImageFilter()
        resampler.SetInterpolator("Linear")
        resampler.SetOutputSpacing(reference_spacing)
        resampler.SetOutputOrigin(image.GetOrigin())
        return resampler.Execute(image)
    else:
        return image


# Main fusion workflow
pet_folder = "./pet_images"  # Replace with path to PET images folder
ct_folder = "./ct_images"   # Replace with path to CT images folder
output_folder = "./f"  # Replace with desired output folder

for pet_filename in os.listdir(pet_folder):
    pet_path = os.path.join(pet_folder, pet_filename)
    pet_base = os.path.splitext(pet_filename)[0]  # Extract base filename for CT pairing

    matching_ct_filename = f"{pet_base}.dcm"  # Assuming CT files have same base name
    ct_path = os.path.join(ct_folder, matching_ct_filename)

    if os.path.exists(ct_path):  # Check if matching CT file exists
        try:
            # Load PET and CT scans
            pet_image = sitk.ReadImage(pet_path)
            ct_image = sitk.ReadImage(ct_path)

            # Preprocess images (optional, uncomment and adjust spacing if needed)
            # preprocessed_pet = preprocess_image(pet_image, reference_spacing=...)
            # preprocessed_ct = preprocess_image(ct_image, reference_spacing=...)

            # Simple averaging fusion
            fused_array = 0.5 * sitk.GetArrayFromImage(pet_image) + 0.5 * sitk.GetArrayFromImage(ct_image)
            fused_image = sitk.GetImageFromArray(fused_array.astype(np.float32))

            # Save fused image
            output_filename = os.path.join(output_folder, f"{pet_base}_fused.nrrd")
            if not os.path.exists(output_folder):
                os.makedirs(output_folder)
            writer = sitk.ImageFileWriter()
            writer.SetFileName(output_filename)
            writer.Execute(fused_image)

            print(f"Fusion completed for {pet_filename} and {matching_ct_filename}")

        except Exception as e:
            print(f"Error processing {pet_filename} and {matching_ct_filename}: {e}")
    else:
        print(f"Matching CT file not found for {pet_filename}")

print("All image pairs processed!")
