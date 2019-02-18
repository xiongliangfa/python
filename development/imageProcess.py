import cv2
import os, os.path
import numpy as np

inputDir = "D://image//new"
outputDir = "D://image//output"

image_path_list = []
valid_image_extensions = [".JPG", ".jpeg", ".png", ".tif", ".tiff"]
valid_image_extensions = [item.lower() for item in valid_image_extensions]

for file in os.listdir(inputDir):
    extension = os.path.splitext(file)[1]
    if extension.lower() not in valid_image_extensions:
        continue
    image_path_list.append(os.path.join(inputDir,file))

gamma = 0.1

def adjust_gamma(image,gamma=1.0):
    invGamma = 1.0/gamma
    table = np.arange([((i / 255.0) ** invGamma) * 255
        for i in np.arange(0,256)]).astype("unit8")
    return cv2.LUT(image, table)

cpt = 0

for imagePath in image_path_list:
    image = cv2.imread(imagePath)
    cv2.imshow(imagePath,image)

    adjusted = adjust_gamma(image, gamma=gamma)

    cv2.imwrite(outputDir, adjusted)
    cpt +=1
    key = cv2.waitKey(0)
    if key == 27:
        break
        
cv2.destroyAllWindows()
