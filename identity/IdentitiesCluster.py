from typing import List

from Cluster.Cluster import Cluster
from identity.Identity import Identity


class IdentitiesCluster(Cluster):

    def __init__(self):
        self._sets = {}
        for field_name in Identity.__annotations__.keys():
            self._sets[field_name] = set()

    @staticmethod
    def from_list(identities_clusters: List['IdentitiesCluster']):
        new_instance = IdentitiesCluster()
        for identities_cluster in identities_clusters:
            for field_name, field_set in identities_cluster._sets.items():
                new_instance._sets.setdefault(field_name, set()).update(field_set)
        return new_instance

    def add_item(self, item):
        for field_name, field_value in vars(item).items():
            self._sets[field_name].add(getattr(item, field_name))

    def __contains__(self, identity: Identity):
        return any([
            field_value and field_value in self._sets[field_name]
            for field_name, field_value in vars(identity).items()
        ])

    def __hash__(self):
        return hash(tuple((field_name, frozenset(field_values)) for field_name, field_values in self._sets.items()))

    def to_dict(self) -> dict:
        return {
            field_name: list(field_set)
            for field_name, field_set in self._sets.items()
        }
