# boş resim oluşturma
# python -m pip install opencv-python
import cv2
import numpy as np
from numpy import random  #NumPy random

x1= random.randint(100)

r5= np.full((50, 170, 3), [random.randint(255),0, random.randint(255)], dtype=np.uint8)
cv2.imshow("Olusan resim4", r5)


cv2.waitKey(0)
 
cv2.destroyAllWindows()
