from abc import ABC, abstractmethod
from typing import List

from Cluster.Cluster import Cluster


class ClusterHandler(ABC):

    @abstractmethod
    def _get_cluster_class(self) -> Cluster:
        pass

    @abstractmethod
    def _single_item_transform_func(self, d) -> object:
        pass

    @abstractmethod
    def _get_items(self, items)->List[tuple]:
        pass

    def handle_items(self, items):
        clusters = set()
        cluster_class = self._get_cluster_class()
        items = self._get_items(items)
        for item in items:
            transformed_item = self._single_item_transform_func(item)
            relevant_clusters = [cluster for cluster in clusters if transformed_item in cluster]
            clusters = clusters.difference(relevant_clusters)
            new_cluster = cluster_class.from_list(relevant_clusters)
            new_cluster.add_item(transformed_item)
            clusters.add(new_cluster)
        return [cluster.to_dict() for cluster in clusters]
