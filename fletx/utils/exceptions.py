"""
FletX Exceptions 
"""

class FletXError(Exception):
    """Base exception for FletX"""
    pass

class RouteNotFoundError(FletXError):
    """Exception raised when a route is not found"""
    pass

class NavigationError(FletXError):
    """Exception raised on navigation errors"""
    pass

class NavigationAborted(FletXError):
    """Exception raised when navigation is cancelled"""
    pass

class DependencyNotFoundError(FletXError):
    """Exception raised when a dependency is not found"""
    pass

class ControllerError(FletXError):
    """Exception related to controllers"""
    pass

class StateError(FletXError):
    """Exception related to state management"""
    pass
