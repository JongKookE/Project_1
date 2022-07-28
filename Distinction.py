import cv2
import numpy as np
import matplotlib.pyplot as plt
import sys
import os
path = "/home/jongkook/.local/lib/python3.8/site-packages/cv2/data/haarcascade_frontalface_default.xml"

face_cascade = cv2.CascadeClassifier(path)
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

image = cv2.imread("/home/jongkook/PycharmProjects/find_img/all_face/0/박효신_100.jpg")
grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 흑백이미지 그리기

faces = face_cascade.detectMultiScale(image, 1.03, 5)
"""print(f"사진의 TYPE: {type(image)}")
print(faces.shape)
print("얼굴 개수: " + str(faces.shape[0]))"""

for (x,y,w,h) in faces:
    cv2.rectangle(grayImage,(x,y),(x+w, y+h),(255,0,0),2)
    cropped = grayImage[y: y + h, x: x + w]
    resize = cv2.resize(cropped, (144, 144))

print(resize.shape)

plt.figure(figsize=(12,12))
plt.imshow(resize) # plt.imshow(resize[:,:,::-1])  BGR -> RGB
plt.title("crop&resize")
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()

plt.imsave("training_data/test_1.jpg", resize)
