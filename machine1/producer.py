import cv2
from skimage import io
import time
import zmq

cap = cv2.VideoCapture('Alberto Mardegan - Selfie del futuro.ogv')
frames=[]
ret=True
while(ret):
    ret, frame = cap.read()
    if ret:
        frames.append(frame)

def producer(frames):
    context = zmq.Context()
    zmq_socket = context.socket(zmq.PUSH)
    zmq_socket.bind("tcp://127.0.0.1:5557")
    print("Producer created successfully!\n")
    for i in range(len(frames)):
        zmq_socket.send_pyobj([frames[i],i])
        
producer(frames)
