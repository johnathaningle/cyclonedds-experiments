from dataclasses import dataclass
from cyclonedds.domain import DomainParticipant
from cyclonedds.core import Qos, Policy
from cyclonedds.pub import DataWriter
from cyclonedds.sub import DataReader
from cyclonedds.topic import Topic
from time import sleep
from idls import Chatter

dp = DomainParticipant()
tp = Topic(dp, "Hello", Chatter, qos=Qos(Policy.Reliability.Reliable(0)))
dw = DataWriter(dp, tp)
dr = DataReader(dp, tp)
count = 0
while count < 10:
    sample = Chatter(name="1234", message="Hello, World!", count=count)
    count = count + 1
    print("Writing ", sample)
    dw.write(sample)
    for sample in dr.take(10):
        print("Read ", sample)
    sleep(1)