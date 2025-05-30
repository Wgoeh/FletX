from dataclasses import dataclass
from typing import Optional

@dataclass
class User:
    id: int
    email: str
    name: Optional[str] = None
    is_admin: bool = False