import cv2

#image = cv2.imread("titanic.JPG", cv2.IMREAD_UNCHANGED)
#cv2.imshow("title", image)
#cv2.waitKey(0)

# Configurable Parameters

source = "titanic.JPG" #file1
destination = 'newimage.png' #file2
scale_percent = 50

src = cv2.imread(source, cv2.IMREAD_UNCHANGED)

# calculate the new percent of original dimensions
new_width = int(src.shape[1] * scale_percent / 100)
new_height = int(src.shape[0] * scale_percent / 100)

#resize image
output = cv2.resize(src, (new_width, new_height))

cv2.imwrite(destination, output)
