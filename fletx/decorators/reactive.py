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

            # create a ref for the callback
            ref = ft.Ref[ft.Control]()
            result = func(self, *args, **kwargs)

            # If the function returns a Control, set it to the content
            if isinstance(result, ft.Control):
                # result.ref = ref
                ref.current = result

                def update_callback(new_value):
                    """Callback to update the control when reactive_obj changes"""
                    if ref.current:
                        # Update the control with the new value
                        page = get_page()
                        ref.current = new_value
                        logger.debug(
                            f"Updated {ref.current} due to changes in {reactive_obj}."
                        )
                    else:
                        logger.warning(
                            f"Ref {ref} is not set, cannot update control."
                        )

                # Register objserver
                reactive_obj.listen(
                    lambda: update_callback(
                        func(self, *args, **kwargs)
                    )
                )
                logger.warning(
                    f"Linstening to {reactive_obj} changes with {func.__name__}."
                )
            else:
                # If the result is not a Control, log a warning
                # and return the result as is
                logger.warning(
                    f"Function {func.__name__} did not return a Control. "
                    "Reactive updates will not be applied."
                )
                reactive_obj.listen(lambda: func(self, *args, **kwargs))
                
            
            return result
        # Set the name of the wrapper to match the original function
        wrapper.__name__ = func.__name__
        wrapper.__qualname__ = func.__qualname__
        # Preserve the original function's docstring
        wrapper.__doc__ = func.__doc__
        # Return the wrapped function
        wrapper.__wrapped__ = func
        return wrapper
    return decorator