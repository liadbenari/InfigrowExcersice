from abc import ABC, abstractmethod
from typing import List


class Cluster(ABC):
    @abstractmethod
    def add_item(self, item):
        pass

    @abstractmethod
    def __contains__(self, item):
        pass

    @abstractmethod
    def __hash__(self):
        pass

    @abstractmethod
    def to_dict(self) -> dict:
        pass

    @staticmethod
    @abstractmethod
    def from_list(l: List):
        pass
