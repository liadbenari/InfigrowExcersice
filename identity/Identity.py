from dataclasses import dataclass
from typing import Union


@dataclass
class Identity:
    account_name: str
    account_id: int
    deal_id: Union[int, None]
    email: str
    contact_id: int
