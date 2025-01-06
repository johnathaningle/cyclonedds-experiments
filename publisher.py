from cyclonedds.domain import DomainParticipant
from cyclonedds.core import Qos, Policy
from cyclonedds.pub import DataWriter
from cyclonedds.sub import DataReader
from cyclonedds.topic import Topic
from time import sleep
import numpy as np
from idls import DataRequest, DataAvaliable, DataResponse
import os
try:
    from names import get_full_name
    name = get_full_name()
except:
    name = f"{os.getpid()}"

rng = np.random.default_rng()
dp = DomainParticipant()
datp = Topic(dp, "DataAvaliable", DataAvaliable, qos=Qos(Policy.Reliability.Reliable(0)))
dadw = DataWriter(dp, datp)

drtp = Topic(dp, "DataRequest", DataRequest, qos=Qos(Policy.Reliability.Reliable(0)))
drdr = DataReader(dp, drtp)

dstp = Topic(dp, "DataResponse", DataResponse, qos=Qos(Policy.Reliability.Reliable(0)))
dsdw = DataWriter(dp, dstp)

count = 0

# find files in directory
files = os.listdir(".")
#filter out directories
files = [file for file in files if os.path.isfile(file)]

fileinfo = {}
for file in files:
    fileinfo[file] = {
        "size": os.path.getsize(file),
        "data": None
    }
    #get file contents in uint8
    with open(file, "rb") as f:
        fileinfo[file]["data"] = np.frombuffer(f.read(), dtype=np.uint8)

while True:
    # loop over file info and write a data avaliable message
    for file, info in fileinfo.items():
        if info["size"] > 0:
            msg = DataAvaliable(filename=file, filesize=info["size"])
            print("Write ", msg)
            dadw.write(msg)

    #listen for data requests
    for sample in drdr.take(10):
        print("Read ", sample)
        if sample.filename in fileinfo:
            msg = DataResponse(filename=sample.filename, data=fileinfo[sample.filename]["data"].tolist())
            print("Write ", msg)
            dsdw.write(msg)
    sleep(1)