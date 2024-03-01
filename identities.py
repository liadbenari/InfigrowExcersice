from typing import List

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
