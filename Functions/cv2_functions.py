import cv2
import numpy as np

def show_images(*args):
    tmp = []
    for img in args:
        if len(img.shape) != 3:
            img = gray2rgb(img)
        tmp.append(img)
    numpy_horizontal = np.hstack(tmp)
    cv2.namedWindow('original', flags=cv2.WINDOW_NORMAL)
    cv2.imshow('original', numpy_horizontal)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def show_img(img):
    show_images(img)

def rgb2gray(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def gray2rgb(bin_img):
    return cv2.cvtColor(bin_img, cv2.COLOR_GRAY2BGR)

def img_threshold(img, threshold=127):
    if len(img.shape) != 2:
        img = rgb2gray(img)
    _, threshold_img = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY)
    return threshold_img

def draw_ellipse(img, ellipse_info):
    for contour in ellipse_info:
        cv2.ellipse(img, contour, color=(255, 0, 255), thickness=1, lineType=cv2.LINE_AA)

def get_ellipse_data(contours):
    ellipses = []
    for contour in contours:
        ellipse = cv2.fitEllipse(contour)
        ellipses.append(ellipse)
    return ellipses

def remove_outlier(df, quantile=0.999, column='area'):
    q = df[column].quantile(quantile)
    df = df[df[column] < q]
    return df
