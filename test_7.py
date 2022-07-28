import cv2
import numpy as np
import matplotlib.pyplot as plt
import sys
import os

path_dir = "all_face/0/"
file_list = os.listdir(path_dir)

file_name_list = []
path = "/home/jongkook/.local/lib/python3.8/site-packages/cv2/data/haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(path)



for i in range(len(file_list)):
    file_name_list.append(file_list[i].replace(".jpg", ""))


image = cv2.imread('all_face/0/박효신_4.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.03, 5)


for (x, y, w, h) in faces:
    cv2.rectangle(gray, (x, y), (x+w, y+h), (255, 0, 0), 2)
    cropped = image[y: y + h, x: x + w]
    resize = cv2.resize(cropped, (144, 144))

    plt.figure(figsize=(12, 12))
    plt.imshow(resize)
    plt.title("crop&resize")
    plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
    plt.show()

