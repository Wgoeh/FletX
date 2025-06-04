"""
Decorators for reactivity.

These decorators enable reactive programming patterns by automatically 
tracking dependencies and updating components when underlying data changes,
facilitating seamless UI updates.
"""

import flet as ft
from typing import Callable, Any
from functools import wraps
from fletx.core.state import (
    Reactive, ReactiveDependencyTracker, Computed
)
from fletx.utils import get_logger, get_page

logger = get_logger('FletX.Decorators.Reactive')

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

    def decorator(func: Callable[[],ft.Control]) -> Callable:
        @wraps(func)
        def wrapper(self, *args, **kwargs):

            # Check if the reactive_obj is a valid reactive type
            if not hasattr(reactive_obj, 'listen'):
                raise TypeError(
                    f"Reactive object {reactive_obj} is not a valid reactive type."
                )

            # Register objserver
            reactive_obj.listen(
                lambda: func(self, *args, **kwargs)
            )
            logger.warning(
                f"Linstening to {reactive_obj} changes with {func.__name__}."
            )
            return func(self, *args, **kwargs)
        return wrapper
    return decorator