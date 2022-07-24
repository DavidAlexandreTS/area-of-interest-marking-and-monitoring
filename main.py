import numpy as np
import cv2
#import torch

# Model
#model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  # or yolov5n - yolov5x6, custom

def left_click_detect(event, x, y, flags, points):
    if (event == cv2.EVENT_LBUTTONDOWN):
        print(f"\tClick on {x}, {y}")
        points.append([x,y])
        print(points)

if __name__ == "__main__":
    flag = 0

    cap = cv2.VideoCapture(r"C:\Users\David\Desktop\TCC Studies\yolov5\experimental_videos\PETS09-S2L1-raw.mp4")  # Open video file

    polygon = []
    points = []

    while(cap.isOpened()):
        ret, frame = cap.read()  # read a frame
        if not ret:
            print('EOF')
            break

        #print("Hi im ret: ", type(ret))
        #print("Hi im Frame First: ", type(frame))

        frame = cv2.polylines(frame, polygon, False, (255, 0, 0), thickness=2)

        #print("Hi im Frame =D: ", type(frame))

        cv2.imshow('Frame', frame)

        key = cv2.waitKey(25)
        if (key == ord('q')):
            break
        elif (key == ord('p')):
            flag = 1
            points.append(points[0])
            polygon = [np.int32(points)]
            #polygon_check = Polygon(points)
            #current = (0, 0)
            print("Final Polygon: ", points)
            points = []

        cv2.setMouseCallback('Frame', left_click_detect, points)
        #if(flag == 1):
            #pm = Point(1, 2)
            #print(polygon_check.contains(pm))

    cap.release()
    cv2.destroyAllWindows()