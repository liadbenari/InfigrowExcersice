from typing import List

from Metrics.Field import MetricsCustomFilter
from Metrics.MetricsCluster import MetricsCluster
from identity.IdentitiesCluster import IdentitiesCluster
from identity.Identity import Identity
from identity.IdentityClusterHandler import IdentityClusterHandler


def identities_handler(identities):
    cluster_handler = IdentityClusterHandler()
    return cluster_handler.handle_items(identities)


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
