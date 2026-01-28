import cv2
print(cv2.__version__)
img=cv2.imread('Resources/logo4.jpg')
print(img.shape)
cv2.imshow("frame",img)
img=cv2.resize(img,(int(img.shape[1]/1.5),int(img.shape[0]/1.5)))
img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("frame",img)
cv2.waitKey(0)