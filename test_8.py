import cv2
import numpy as np
import matplotlib.pyplot as plt
import sys
import os
path = "/home/jongkook/.local/lib/python3.8/site-packages/cv2/data/haarcascade_frontalface_default.xml"
categories = ["0", "1", "2"] # 0 = 박효신, 1 = 한소희, 2 = 장범준
groups_folder_path = "all_face/"
num_classes = len(categories) # -> 3

face_cascade = cv2.CascadeClassifier(path)

image = cv2.imread("/home/jongkook/PycharmProjects/find_img/all_face/0/박효신_100.jpg")
grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 흑백이미지 그리기

faces = face_cascade.detectMultiScale(image, 1.03, 5)

for idex, categorie in enumerate(categories):
    label = [0 for i in range(num_classes)]
    label[idex] = 1
    image_dir = groups_folder_path + categorie + '/' # 모든 파일에 대한 작업
    for top, dir, f in os.walk(image_dir):
        #경로내 모든 파일에 대하여
        #print(len(f)) 박효신 351, 장범준 456, 한소희 180
        for filename in f:
            img = cv2.imread(image_dir+filename)
            #gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(img, 1.03, 5)
            if type(faces) == tuple:
                continue
            else:
                # 얼굴이 하나이면 얼굴부분 잘라내고 리사이즈 한 뒤 list에 추가
                if faces.shape[0] == 1:
                    for (x, y, w, h) in faces:
                        cropped = img[y:y + h, x:x + w]
                        resize_gray = cv2.resize(cropped, (144, 144))

plt.figure(figsize=(12,12))
plt.imshow(resize_gray) # plt.imshow(resize[:,:,::-1])  BGR -> RGB
plt.title("crop&resize")
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()

for top, dir, files in os.walk(image_dir):
    plt.imsave(f"training_data/test_{len(files)+1}.jpg", resize_gray)
