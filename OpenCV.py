#task 2
import cv2

x=cv2.VideoCapture('input.mp4')
if not x.isOpened():
    print("Video cannot be opened")
frame_skip_interval=4
fps=int(x.get(cv2.CAP_PROP_FPS))
while True:
    ret, frame=x.read()
    if not ret:
        break
    cv2.imshow('Video',frame)
    cv2.waitKey(1)
    for i in range(0,fps,frame_skip_interval):
        x.grab()
x.release()
cv2.destroyAllWindows
