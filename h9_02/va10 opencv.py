import cv2
img = cv2.imread('images/pasta.jpg')
cv2.imshow('Deneme',img)
cv2.waitKey(50) # 3 saniye bekle   # (0) dersek bi tuşa basana kadar
cv2.destroyAllWindows() # pencereleri kapa

