
import cv2

image = cv2.imread("./2.jpg")

image = cv2.resize(image,(500,400))


cv2.imshow("image",image)

cv2.waitKey(0)


gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("gray",gray_image)

cv2.waitKey(0)

inverted_img = 255 - gray_image

cv2.imshow("imverted_image",inverted_img)
cv2.waitKey(0)

blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)
cv2.imshow("blurred_image",inverted_img)
cv2.waitKey(0)

inverted_blurred = 255 - blurred

pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)
cv2.imshow("Sketch", pencil_sketch)
cv2.waitKey(0)