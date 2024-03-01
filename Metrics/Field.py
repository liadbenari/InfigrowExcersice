from dataclasses import dataclass
from typing import List, Set


@dataclass(init=False)
class FilterData:
    fieldIndex: int
    variant: int
    selectedOptions: Set[str]

    def __init__(self, data_dict):
        self.fieldIndex = data_dict['fieldIndex']
        self.variant = data_dict['variant']
        self.selectedOptions = set(data_dict['selectedOptions'])

    def __hash__(self):
        iterable_to_hash = [self.fieldIndex, self.variant]
        iterable_to_hash.extend(sorted(self.selectedOptions))
        return hash(tuple(iterable_to_hash))


@dataclass(init=False)
@dataclass
class Filter:
    kind: str
    data: FilterData

    def __init__(self, data_dict):
        self.kind = data_dict['kind']
        self.data = FilterData(data_dict['data'])

    def __hash__(self):
        hash_value = hash(self.kind)
        hash_value ^= hash(self.data)
        return hash_value

    def __lt__(self, other):
        if self.kind != other.kind:
            return self.kind < other.kind

        for k in sorted(vars(self.data).keys()):
            if vars(self.data)[k] != vars(other.data)[k]:
                return vars(self.data)[k] < vars(other.data)[k]
        return 0


@dataclass(init=False)
class MetricsCustomFilter:
    name: str
    filters: List[Filter]

    def __init__(self, name, filters):
        self.name = name
        self.filters = [Filter(filt) for filt in filters]
