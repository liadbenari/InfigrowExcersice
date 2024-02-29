import json
from dataclasses import dataclass, field, fields, asdict
from typing import List, Union


@dataclass
class IdentitiesMultiple:
    account_name: List[str] = field(default_factory=list)
    account_id: List[int] = field(default_factory=list)
    deal_id: List[int] = field(default_factory=list)
    email: List[str] = field(default_factory=list)
    contact_id: List[int] = field(default_factory=list)


@dataclass(unsafe_hash=True)
class IdentitySingular:
    account_name: str
    account_id: int
    deal_id: Union[int, None]
    email: str
    contact_id: int


def identities_handler(identities):
    identities: List[IdentitySingular] = [IdentitySingular(**identity) for identity in identities]
    identity_fields = {f.name: {} for f in fields(IdentitySingular)}
    for id in identities:
        for id_field in fields(IdentitySingular):
            field_name = id_field.name
            relevant_field_dict = identity_fields[field_name]
            field_value = getattr(id, field_name)
            if field_value and field_value not in relevant_field_dict:
                relevant_field_dict[field_value] = [id]
            elif field_value:
                relevant_field_dict[field_value].append(id)
    clusters = set()
    for k, v in identity_fields.items():
        for unique_values in v.values():
            all_relevant_clusters = [cluster for cluster in clusters if any([val in cluster for val in unique_values])]
            clusters = clusters.difference(all_relevant_clusters)
            union_set = frozenset(unique_values)
            for cluster in all_relevant_clusters:
                union_set = union_set.union(cluster)
            clusters.add(union_set)
    all_identities = []
    for cluster in clusters:
        account_name = set()
        account_id =set()
        deal_id = set()
        email = set()
        contact_id = set()
        for identity in cluster:
            account_name.add(identity.account_name)
            account_id.add(identity.account_id)
            deal_id.add(identity.deal_id)
            email.add(identity.email)
            contact_id.add(identity.contact_id)
        identities_multiple = IdentitiesMultiple(list(account_name),list(account_id),list(deal_id),list(email),list(contact_id))

        all_identities.append(asdict(identities_multiple))
    return all_identities
