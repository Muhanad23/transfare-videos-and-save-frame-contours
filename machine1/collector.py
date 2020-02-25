import time
import zmq
import random
import sys
import cv2
import socket

def getIp():
    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    s.connect(("8.8.8.8",80))
    print("\nMy IP:"+s.getsockname()[0]+"\n")
    return s.getsockname()[0]
def collector():
    context = zmq.Context()
    # recieve work
    collector_receiver = context.socket(zmq.PULL)
    recevie_port="tcp://127.0.0.1:"+str(int(sys.argv[1])+6000)
    collector_receiver.bind(recevie_port)
    # send work
    collector_sender = context.socket(zmq.PUSH)
    send_port="tcp://"+str(getIp())+":"+str(int(sys.argv[1])+7000)
    collector_sender.bind(send_port)
    print("collector #"+sys.argv[1]+" created successfully!"+"-----receive_port: "+str(int(sys.argv[1])+6000)+"-----send_port: "+str(int(sys.argv[1])+7000)+"\n")
    while True:
        work = collector_receiver.recv_pyobj()
        collector_sender.send_pyobj(work)

collector()
