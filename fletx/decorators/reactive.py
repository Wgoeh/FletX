"""
Decorators for reactivity.

These decorators enable reactive programming patterns by automatically 
tracking dependencies and updating components when underlying data changes,
facilitating seamless UI updates.
"""


from typing import Callable, Any
from functools import wraps
from fletx.core.state import (
    Reactive, ReactiveDependencyTracker, Computed
)
from fletx.utils.logger import SharedLogger


####    COMPUTED PROPERTIES DECORATOR
def computed(func: Callable) -> property:
    """Decorator for computed properties"""
    
    @property
    @wraps(func)
    def wrapper(self):
        # Create a Computed if not exists
        if not hasattr(self, f"__computed_{func.__name__}"):
            # Deps detection
            def getter():
                return func(self)
                
            _, deps = ReactiveDependencyTracker.track(getter)
            
            # Now Create the computed property
            computed_obj = Computed(getter, list(deps))
            setattr(self, f"__computed_{func.__name__}", computed_obj)
        
        return getattr(self, f"__computed_{func.__name__}").value
    
    return wrapper


###     REACTIVE PROPERTIES DECORATOR
def reactive_property(func: Callable) -> property:
    """Decorator for reactive properties"""
    
    @property
    @wraps(func)
    def wrapper(self):
        return func(self)
    
    @wrapper.setter
    def wrapper(self, value):
        # Simplified Implementation
        setattr(self, f"_{func.__name__}", value)
        if hasattr(self, "update"):
            self.update()
    
    return wrapper

####    WATCH REACTIVE OBJETCS
def watch(reactive_obj: Reactive):
    """Decorator for watching reactive objetcs"""

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            # Register objserver
            if hasattr(reactive_obj, 'listen'):
                reactive_obj.listen(lambda: func(self, *args, **kwargs))
            else:
                SharedLogger.logger.warning(f"L'objet {reactive_obj} n'est pas réactif")
            
            return func(self, *args, **kwargs)
        return wrapper
    return decorator