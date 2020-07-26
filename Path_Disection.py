from imutils import paths
import os
import time 
imagePaths = list(paths.list_images("dataset"))
imagePath = imagePaths[0]
print(imagePath)
print(imagePath.split(os.path.sep))
time.sleep(5)

