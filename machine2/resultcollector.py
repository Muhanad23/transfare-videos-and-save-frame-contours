import time
import zmq

def result_collector():
    context = zmq.Context()
    results_receiver = context.socket(zmq.PULL)
    results_receiver.bind("tcp://127.0.0.1:9999")
    file = open("testfile.txt","w+") 
    print("result collector "+" created successfully!-------------recieve from port:9999"+"\n")

    while True:
        result = results_receiver.recv_pyobj() 
        file.write(str(result["fnum"])+"\n"+"\n"+"\n")
        bboxes = result["bboxes"]
        for box in bboxes:
          [Xmin, Xmax, Ymin, Ymax] = box
          file.write("Xmin ="+str(Xmin)+" Xmax="+str(Xmax)+" Ymin="+str(Ymin)+" Ymax="+str(Ymax)+"\n")
        file.write("----------------------------------------------------------"+"\n")
result_collector()
