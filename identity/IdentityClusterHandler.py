from typing import Type

from Cluster.ClusterHandler import ClusterHandler
from identity.IdentitiesCluster import IdentitiesCluster
from identity.Identity import Identity


class IdentityClusterHandler(ClusterHandler):
    def _item_transform_func(self, d: dict) -> object:
        return Identity(**d)

    def _get_cluster_class(self) -> Type[IdentitiesCluster]:
        return IdentitiesCluster
