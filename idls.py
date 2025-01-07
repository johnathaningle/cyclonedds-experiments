from dataclasses import dataclass
from cyclonedds.idl import IdlStruct
from cyclonedds.idl.annotations import key
from cyclonedds.idl.types import *

# C, C++ require using IDL, Python doesn't
@dataclass
class Chatter(IdlStruct, typename="Chatter"):
    name: str
    key("name")
    message: str
    count: int

@dataclass
class DataRequest(IdlStruct, typename="DataRequest"):
    filename: str
    key("filename")

@dataclass
class DataAvaliable(IdlStruct, typename="DataAvaliable"):
    filename: str
    key("filename")
    filesize: int

@dataclass
class DataResponse(IdlStruct, typename="DataResponse"):
    filename: str
    key("filename")
    data: sequence[uint8]
