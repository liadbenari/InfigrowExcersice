from abc import ABC, abstractmethod
from Cluster.Cluster import Cluster


class ClusterHandler(ABC):

    @abstractmethod
    def _get_cluster_class(self) -> Cluster:
        pass

    @abstractmethod
    def _item_transform_func(self, d: dict) -> object:
        pass

    def handle_items(self, items):
        clusters = set()
        cluster_class = self._get_cluster_class()
        for item in items:
            transformed_item = self._item_transform_func(item)
            relevant_clusters = [cluster for cluster in clusters if transformed_item in cluster]
            clusters = clusters.difference(relevant_clusters)
            new_cluster = cluster_class.from_list(relevant_clusters)
            new_cluster.add_item(transformed_item)
            clusters.add(new_cluster)
        return [cluster.to_dict() for cluster in clusters]
