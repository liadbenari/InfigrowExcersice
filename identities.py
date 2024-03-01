from typing import List

from Metrics.Field import MetricsCustomFilter, Filter
from Metrics.MetricsCluster import MetricsCluster
from identity.IdentitiesCluster import IdentitiesCluster
from identity.Identity import Identity


def identities_handler(identities):
    identities: List[Identity] = [Identity(**identity) for identity in identities]
    clusters = set()
    for identity in identities:
        relevant_clusters = [cluster for cluster in clusters if identity in cluster]
        clusters = clusters.difference(relevant_clusters)
        new_cluster = IdentitiesCluster.from_list(relevant_clusters)
        new_cluster.add_item(identity)
        clusters.add(new_cluster)
    return [cluster.to_dict() for cluster in clusters]


def metrics_handler(metrics_custom_filters: dict):
    metrics = []
    for metric_name, filters in metrics_custom_filters['metricsCustomFilters'].items():
        custom_filter = MetricsCustomFilter(metric_name, filters)
        metrics.append(custom_filter)
    clusters = set()
    for metric in metrics:
        relevant_clusters = [cluster for cluster in clusters if metric in cluster]
        clusters = clusters.difference(relevant_clusters)
        new_cluster = MetricsCluster.from_list(relevant_clusters)
        new_cluster.add_item(metric)
        clusters.add(new_cluster)
    return [cluster.to_dict() for cluster in clusters]
