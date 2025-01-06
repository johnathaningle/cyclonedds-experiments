from dataclasses import dataclass
from cyclonedds.domain import DomainParticipant
from cyclonedds.core import Qos, Policy
from cyclonedds.sub import DataReader
from cyclonedds.pub import DataWriter
from cyclonedds.topic import Topic
import numpy as np
from idls import DataRequest, DataResponse, DataAvaliable
try:
    from names import get_full_name
    name = get_full_name()
except:
    import os
    name = f"{os.getpid()}"

#add command line arguments for filename and output directory
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("filename")
parser.add_argument("outputdir")
args = parser.parse_args()

dp = DomainParticipant()
datp = Topic(dp, "DataAvaliable", DataAvaliable, qos=Qos(Policy.Reliability.Reliable(0)))
dadr = DataReader(dp, datp)

drtp = Topic(dp, "DataRequest", DataRequest, qos=Qos(Policy.Reliability.Reliable(0)))
drdw = DataWriter(dp, drtp)

dstp = Topic(dp, "DataResponse", DataResponse, qos=Qos(Policy.Reliability.Reliable(0)))
dsdr = DataReader(dp, dstp)

outfile_size = 0
filesize = 0

while filesize == 0 or outfile_size < filesize:
    for sample in dadr.take(10):
        print("Read ", sample)
        if sample.filename == args.filename:
            filesize = sample.filesize
            msg = DataRequest(filename=sample.filename)
            print("Write ", msg)
            drdw.write(msg)
    for sample in dsdr.take(10):
        print("Read ", sample)
        if sample.filename == args.filename:
            outfile_size += len(sample.data)
            with open(f"{args.outputdir}/{sample.filename}", "ab") as f:
                f.write(bytes(sample.data))