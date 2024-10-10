
from PIL import Image
import numpy as np
import SimpleITK as sitk
import nrrd


def manipulating_nrrd_contrast(img, level):
    img_c = img.astype(int).copy()
    factor = (8 * (level+255)) / (255 * (259-level)) #This 8 here is the value that i changes manually by try and test and found out that this works best
    img_c = factor * (img_c - 128) + 128
    img_c = np.clip(img_c, 0, 255)
    return img_c.astype(np.uint8)

filename = "image.nrrd"
readdata, header = nrrd.read(filename)
print(readdata.shape)
for i in range(readdata.shape[2]):
  b = np.asarray(readdata[:,:,i]).astype(int)
  final = Image.fromarray(manipulating_nrrd_contrast(b, 128))
  final.save("./_fused.png")