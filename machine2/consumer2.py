import cv2
import zmq
import sys
import skimage.io as io
from skimage.measure import find_contours
import numpy as np

def consumer2():

    context = zmq.Context()
    receiver = context.socket(zmq.PULL)
    receiver.connect("tcp://"+sys.argv[2]+":"+sys.argv[1])
    

    sender = context.socket(zmq.PUSH)
    sender.connect("tcp://127.0.0.1:9999")
    print("Consumer2 #"+" created successfully!-------------recieve from port:"+sys.argv[1]+"\n")

    while True:
        frame = receiver.recv_pyobj()
        dictt = {}
        dictt["image"]=frame[0]
        dictt["fnum"]=frame[1] 
        image=dictt.get("image")
        contours = find_contours(frame[0],0.8) 
        bounding_boxes = []
        for contour in contours:
            Xmin = np.min(contour[:,1])
            Xmax = np.max(contour[:,1])
            Ymin = np.min(contour[:,0])
            Ymax = np.max(contour[:,0])
            bounding_boxes.append([int(Xmin), int(Xmax), int (Ymin), int(Ymax)])
            
        dictt["bboxes"]=bounding_boxes   
        sender.send_pyobj(dictt)

consumer2()
