#basit bir r harfi, dikdörtgen,çizgi ve çember çizme çalışması
import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)
cv2.imshow('img',img)
cv2.line(img, (0,0),(360,360),(0,100,0),5)
cv2.rectangle(img, (100,100),(200,200),(0,100,0),10)

cv2.line(img, (100,50),(100,150),(255, 105, 180),7)
cv2.line(img, (100,50),(150,50),(255, 105, 180),7)
cv2.line(img, (150,50),(120,100),(255, 105, 180),7)
cv2.line(img, (120,100),(150,150),(255, 105, 180),7)

cv2.circle(img, (300,300),60,(254, 105, 180),7)
cv2.circle(img, (400,400),60,(254, 105, 180),-1)
cv2.imshow('img',img)
