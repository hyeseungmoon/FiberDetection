import matplotlib.pyplot as plt
from Functions.cv2_functions import *
import math
import csv

COLOR_THRESHOLD = 170
NOISE_THRESHOLD = 10

img = cv2.imread('Images/sample2.jpg', 0)
bin_img = img_threshold(img, COLOR_THRESHOLD)

cv2.imwrite("binary_img.png", bin_img)

tmp, hierarchy = cv2.findContours(bin_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
contour_img = gray2rgb(img.copy())
contours = []
for cnt in tmp:
    if cv2.contourArea(cnt) > NOISE_THRESHOLD:
        contours.append(cnt)

cv2.drawContours(contour_img, contours, -1, (255, 0, 255), 1)
cv2.imwrite("contour_img.png", contour_img)

ellipse_list = get_ellipse_data(contours)
res = gray2rgb(img.copy())
draw_ellipse(res, ellipse_list)
show_images(res)

cv2.imwrite("ellipse_img.png", res)

angle_list = []
for ellipse in ellipse_list:
    minor, major = sorted(ellipse[1])
    angle_list.append(math.degrees(math.acos(minor / major)))

l = []
for i in range(len(ellipse_list)):
    (x, y), (a, b), _ = ellipse_list[i]
    angle = angle_list[i]
    l.append([x, y, angle])
fields = ['a', 'b', 'angle']
with open('result.csv', 'w', newline='') as f:
    write = csv.writer(f)
    write.writerow(fields)
    write.writerows(l)