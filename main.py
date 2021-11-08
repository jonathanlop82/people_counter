import cv2
import numpy as np

def run():
    cap = cv2.VideoCapture('rtsp://altaplaza:62741797@10.0.0.91/H264?ch=1&subtype=0')

    while(True):
        ret, frame = cap.read()
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    run()