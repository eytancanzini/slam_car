#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import numpy as np

threshold_low = 5
threshold_high = 200
rho = 2
theta = np.pi/2
threshold = 10
min_line_len = 1
max_line_gap = 1
alpha = 1
beta = 1
gamma = 0

def detect_lanes(frame):
    lines = cv2.HoughLinesP(frame, rho, theta, threshold, np.array([]), minLineLength=min_line_len, maxLineGap=max_line_gap)
    line_image = np.zeros((frame.shape[0], frame.shape[1], 3), dtype=np.uint8)
    if lines is not None:
        for line in lines:
            for x1, y1, x2, y2 in line:
                cv2.line(line_image, (x1, y1), (x2, y2), [0, 0, 255], 20)
    else:
        print('No lines detected')
    return line_image

def region_of_interest(frame, g_frame):
    vertices = np.array([[(319, 708), (688, 438), (825, 438), (1198, 710)]], dtype=np.int32)
    mask = np.zeros_like(g_frame)
    cv2.fillPoly(mask, vertices, 255)
    masked_image = cv2.bitwise_and(frame, mask)
    return masked_image

def filter_env(frame):
    image_g = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    frame_blurred = cv2.GaussianBlur(image_g, (7,7), 0)
    frame_canny = cv2.Canny(frame_blurred, threshold_low, threshold_high)
    frame_filter = region_of_interest(frame_canny, frame_blurred)
    return frame_filter
        

if __name__ == "__main__":
    try:
        cap = cv2.VideoCapture('./Fast Driving Car On Straight Road-59fWb5A_dH4.mp4')
        while (cap.isOpened()):
            ret, frame = cap.read()
            if ret == True:
                image_f = filter_env(frame)
                image_l = detect_lanes(image_f)
                frame_lines = cv2.addWeighted(frame, alpha, image_l, beta, gamma)
                cv2.imshow('Frame', frame_lines)
                if cv2.waitKey(25) & 0xFF == ord('q'):
                    break
            else:   
                break
        cap.release()
        cv2.destroyAllWindows()
    except Exception as e:
        print('Error opening window: ' + e)

