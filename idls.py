from dataclasses import dataclass
from cyclonedds.idl import IdlStruct
from cyclonedds.idl.annotations import key

# C, C++ require using IDL, Python doesn't
@dataclass
class Chatter(IdlStruct, typename="Chatter"):
    name: str
    key("name")
    message: str
    count: int
