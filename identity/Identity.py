from dataclasses import dataclass, field
from typing import List, Union

@dataclass
class IdentitiesMultiple:
    account_name: List[str] = field(default_factory=list)
    account_id: List[int] = field(default_factory=list)
    deal_id: List[int] = field(default_factory=list)
    email: List[str] = field(default_factory=list)
    contact_id: List[int] = field(default_factory=list)

@dataclass
class IdentitySingular:
    account_name: str
    account_id: int
    deal_id: Union[int, None]
    email: str
    contact_id: int