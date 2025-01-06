from dataclasses import dataclass
from cyclonedds.domain import DomainParticipant
from cyclonedds.core import Qos, Policy
from cyclonedds.sub import DataReader
from cyclonedds.topic import Topic
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
dr = DataReader(dp, tp)
count = 0
while True:
    for sample in dr.take(10):
        print("Read ", sample)