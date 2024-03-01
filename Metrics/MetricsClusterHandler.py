from typing import Type

from Cluster.ClusterHandler import ClusterHandler
from Metrics.Field import MetricsCustomFilter
from Metrics.MetricsCluster import MetricsCluster


class MetricsClusterHandler(ClusterHandler):
    def _get_items(self, items):
        return items['metricsCustomFilters'].items()

    def _single_item_transform_func(self, t: tuple) -> object:
        return MetricsCustomFilter(t[0], t[1])

    def _get_cluster_class(self) -> Type[MetricsCluster]:
        return MetricsCluster
