from dataclasses import asdict
from typing import List

from Cluster.Cluster import Cluster
from Metrics.Field import MetricsCustomFilter, FilterData


class MetricsCluster(Cluster):

    def __init__(self):
        self._name_set = set()
        self._filters_set = set()

    @staticmethod
    def from_list(metrics_clusters: List['MetricsCluster']):
        new_instance = MetricsCluster()
        for metrics_cluster in metrics_clusters:
            new_instance._name_set.update(metrics_cluster._name_set)
            new_instance._filters_set.update(metrics_cluster._filters_set)
        return new_instance

    def add_item(self, item: MetricsCustomFilter):
        self._name_set.add(item.name)
        self._filters_set.update(item.filters)

    def __contains__(self, metrics_custom_filter: MetricsCustomFilter):
        return set(metrics_custom_filter.filters) == self._filters_set

    def __hash__(self):
        return hash(tuple(sorted(self._name_set))) + hash(tuple(sorted(self._filters_set)))

    @staticmethod
    def _filter_data_to_dict(filter_data: FilterData):
        return_value = asdict(filter_data)
        return_value['selectedOptions'] = list(return_value['selectedOptions'])
        return return_value

    def to_dict(self) -> dict:
        return {
            "metrics": list(self._name_set),
            "filters": [{"kind": filt.kind, "data": self._filter_data_to_dict(filt.data)} for filt in self._filters_set]
        }
