import cv2
import numpy as np
import matplotlib.pyplot as plt
import sys
import os
from sklearn.model_selection import train_test_split

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
path_dir = "C:\\Users\john cookie\PycharmProjects\pythonProject1\\all_face\\0"
file_list = os.listdir(path_dir)

file_name_list = []

for i in range(len(file_list)):
    file_name_list.append(file_list[i].replace(".jpg",""))

def Cutting_face_save(image, name):
    image = cv2.imread(f"{path_dir}\\hyoshin_1.jpg")
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        cv2.rectangle(image, (x,y), (x+w, y+h), (255,0,0), 2)
        cropped = image[y: y + h, x: x + w]
        resize = cv2.resize(cropped, (180, 180))
        cv2.imshow("crop&resize", resize)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        cv2.imwrite(f"개개비/{name}.jpg", resize)

cnt = 1
for name in file_name_list:
    img = cv2.imread(f"C:\\Users\john cookie\PycharmProjects\pythonProject1\\all_face\\0\\{name}.jpg")
    Cutting_face_save(img, name)
    print(f"{name}.jpg is saved")
    cnt += 1
