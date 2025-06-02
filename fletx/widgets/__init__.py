import flet as ft
from functools import wraps
from typing import (
    get_type_hints, Dict
)

from fletx.core.state import (
    Reactive, RxInt, RxStr, RxBool, RxList, RxDict 
)
from fletx.core.widget import FletXWidget


def reactive_control(bindings: Dict[str, str]):
    """
    Decorator that creates a reactive control while preserving the original inheritance chain.
    This decorator grafts reactive capabilities onto existing control classes.
    Modifies the class in-place by:
    1. Adding FletXWidget as a parent class
    2. Injecting reactive initialization
    3. Preserving all original functionality
    
    Args:
        bindings: Dictionary mapping widget properties to reactive attribute names
                 Example: {'value': 'rx_value', 'color': 'rx_color'}
    Returns: A Reactive Version of the ControlClass

    Usage:
    ```python
        @reactive_control(bindings={'value': 'rx_value',})
        class MyReactiveCheckbox(ft.Checkbox):
        
            # Defining the reactive properties
            self.rx_value: RxBool = RxBool(False)   # Reactive property for checkbox value

            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
    ```
    """

    # Validate bindings
    if not isinstance(bindings, dict):
        raise TypeError(
            f"Bindings must be a dictionary, got {type(bindings).__name__}"
        )

    def decorator(ControlClass):

        # Store original init
        original_init = ControlClass.__init__

        # Add FletXWidget as a parent while preserving existing parents
        ControlClass.__bases__ = (*ControlClass.__bases__, FletXWidget)

        @wraps(original_init)
        def __init__(self, *args, **kwargs):
            # Separate reactive props from normal kwargs

            # Process checks
            for prop, rx_name in bindings.items():
                # if not hasattr(ControlClass, prop):
                #     raise AttributeError(
                #         f"{ControlClass.__name__} does not have property '{prop}'"
                #         "You must define it in your reactive control class."
                #     )
                
                # ControlCall must define the reactive properties specified in bindings
                # if not hasattr(ControlClass(), rx_name) :
                #     raise ValueError(
                #         f"Reactive property '{rx_name}' must be provided in kwargs."
                #     )
                
                if not get_type_hints(ControlClass).get(rx_name, None) in (
                    Reactive, RxInt, RxStr, RxBool, RxList, RxDict
                ):
                    raise TypeError(
                        f"Property '{rx_name}' in {ControlClass.__name__} must be a reactive type."
                    )
                
            # _rx_store = {
            #     rx_name: kwargs.pop(rx_name)
            #     for rx_name in bindings.values()
            #     if rx_name in kwargs
            # }

            # Call original initialization
            original_init(self, *args, **kwargs)

            # Initialize FletXWidget
            FletXWidget.__init__(self)

            # Setup reactive bindings
            for widget_prop, rx_name in bindings.items():
                # if rx_name in _rx_store:
                # If the reactive attribute is provided, bind it 
                self.bind(widget_prop, getattr(self, rx_name)) # Inherited from FletXWidget

        
        # Inject new methods
        ControlClass.__init__ = __init__

        return ControlClass
    
    return decorator