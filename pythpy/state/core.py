import json
from abc import ABC, abstractmethod
from construct import Struct, Container


class StateCore(ABC):
    layout: Struct = None

    @classmethod
    @abstractmethod
    def from_container(cls, container: Container):
        pass

    @classmethod
    def parse(cls, bytes_data: bytes, factor: int):
        container = cls.layout.parse(bytes_data)
        obj = cls.from_container(container=container)
        obj = obj.parse_precision(factor=factor)
        return obj

    @abstractmethod
    def parse_precision(self, factor: int):
        pass

    @abstractmethod
    def to_dict(self) -> dict:
        pass

    def __str__(self):
        my_dict = self.to_dict()
        return json.dumps(my_dict, sort_keys=False, indent=4)