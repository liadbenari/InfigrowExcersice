import json
from dataclasses import dataclass, field, fields, asdict
from typing import List, Union


@dataclass
class IdentitiesMultiple:
    account_name: List[str] = field(default_factory=list)
    account_id: List[int] = field(default_factory=list)
    deal_id: List[int] = field(default_factory=list)
    email: List[str] = field(default_factory=list)
    contact_id: List[int] = field(default_factory=list)


@dataclass(unsafe_hash=True)
class IdentitySingular:
    account_name: str
    account_id: int
    deal_id: Union[int, None]
    email: str
    contact_id: int


class MultipleIdentitiesDataStruct:

    def __init__(self):
        self._sets = {}
        for field_name in IdentitySingular.__annotations__.keys():
            self._sets[field_name] = set()

    @classmethod
    def from_list(cls, lists: List['MultipleIdentitiesDataStruct']):
        new_instance = cls()
        for multiple_identities_data_struct in lists:
            for field_name, field_set in multiple_identities_data_struct._sets.items():
                new_instance._sets.setdefault(field_name, set()).update(field_set)
        return new_instance

    def add_identity(self, identity: IdentitySingular):
        for field_name, field_value in vars(identity).items():
            self._sets[field_name].add(getattr(identity, field_name))

    def contains_identity(self, identity: IdentitySingular):
        return any([
            field_value and field_value in self._sets[field_name]
            for field_name, field_value in vars(identity).items()
        ])

    def __hash__(self):
        return hash(tuple((field_name, frozenset(field_values)) for field_name, field_values in self._sets.items()))

    def to_identities_multiple(self):
        return IdentitiesMultiple(**{field_name: list(field_set) for field_name, field_set in self._sets.items()})


def identities_handler(identities):
    identities: List[IdentitySingular] = [IdentitySingular(**identity) for identity in identities]
    clusters = set()
    for id in identities:
        relevant_clusters = [cluster for cluster in clusters if cluster.contains_identity(id)]
        clusters = clusters.difference(relevant_clusters)
        new_cluster = MultipleIdentitiesDataStruct.from_list(relevant_clusters)
        new_cluster.add_identity(id)
        clusters.add(new_cluster)
    return [asdict(cluster.to_identities_multiple()) for cluster in clusters]
