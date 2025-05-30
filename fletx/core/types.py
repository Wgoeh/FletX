"""
FletX Types module
"""

from typing import Dict, Any, Type, Optional
from dataclasses import dataclass


####
##      ROUTE INFO CLASS
#####
@dataclass
class RouteInfo:
    """
    Route information
    Contains detailed information about a specific route,
    such as its path, parameters etc...
    """
    
    def __init__(
        self, 
        path: str, 
        params: Dict[str, Any] = None, 
        query: Dict[str, Any] = None
    ):
        self.path = path
        self.params = params or {}
        self.query = query or {}
        self._extra = {}

    def add_extra(self, key: str, value: Any):
        """
        Adds additional data to the route
        Allows associating additional data with a route, 
        such as metadata, security information, or context data.
        """
        self._extra[key] = value
    
    def get_extra(self, key: str, default: Any = None) -> Any:
        """
        Gets additional data
        Retrieves the additional data associated with a route, 
        such as metadata, security information, or context data.
        """
        return self._extra.get(key, default)