from cyclonedds.domain import DomainParticipant
from cyclonedds.core import Qos, Policy
from cyclonedds.pub import DataWriter
from cyclonedds.topic import Topic
from time import sleep
import numpy as np
from idls import Chatter
try:
    from names import get_full_name
    name = get_full_name()
except:
    import os
    name = f"{os.getpid()}"

rng = np.random.default_rng()
dp = DomainParticipant()
tp = Topic(dp, "Hello", Chatter, qos=Qos(Policy.Reliability.Reliable(0)))
dw = DataWriter(dp, tp)
count = 0
while True:
    sample = Chatter(name=name, message="Hello, World!", count=count)
    count = count + 1
    print("Writing ", sample)
    dw.write(sample)
    sleep(rng.exponential())