from Metrics.MetricsClusterHandler import MetricsClusterHandler
from identity.IdentityClusterHandler import IdentityClusterHandler


def identities_handler(identities):
    cluster_handler = IdentityClusterHandler()
    return cluster_handler.handle_items(identities)


def metrics_handler(metrics_custom_filters):
    cluster_handler = MetricsClusterHandler()
    return cluster_handler.handle_items(metrics_custom_filters)
