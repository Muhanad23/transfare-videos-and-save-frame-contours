import time
import zmq
import random
import sys
import cv2

def consumer():
    context = zmq.Context()
    # recieve work
    consumer_receiver = context.socket(zmq.PULL)
    consumer_receiver.connect("tcp://127.0.0.1:5557")
    # send work
    n=int(sys.argv[1])//2
    n=n+6000
    send_port="tcp://127.0.0.1:"+str(n)
    consumer_sender = context.socket(zmq.PUSH)
    consumer_sender.connect(send_port)
    print("Consumer #"+sys.argv[1]+" created successfully!-------------send to port:"+str(n)+"\n")
    while True:
        work = consumer_receiver.recv_pyobj()
        im_gray=cv2.cvtColor(work[0], cv2.COLOR_BGR2GRAY)
        ret,img = cv2.threshold(im_gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        consumer_sender.send_pyobj([img,work[1]])

consumer()
