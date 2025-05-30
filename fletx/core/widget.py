"""
Base Widget for FletX

The base widget for FletX is a fundamental component that serves 
as a template for all other widgets. It provides a basic structure 
for creating custom widgets and offers common features such as event handling, 
layout, and appearance customization.
"""

import flet as ft
from abc import ABC, abstractmethod
from typing import Union, List, Optional, Any, Dict
from fletx.core.state import Reactive
from fletx.utils import get_logger
from fletx.core.factory import FletXWidgetRegistry
from fletx.utils.context import AppContext

# from flet_core.control import Control as ft_Control 


class FletXWidgetMeta(type(ft.Control)):
    """Métaclasse pour l'enregistrement automatique"""
    def __new__(cls, name, bases, dct):
        # Crée la classe
        new_class = super().__new__(cls, name, bases, dct)
        
        # Enregistre auprès de Flet si c'est un widget concret
        if 'build' in dct and not getattr(new_class, '_abstract', False):
            # ft.Control.(new_class)
            pass
        return new_class


####
##      FLETX WIDGET CLASS
#####
class FletXWidget(ABC):
    """
    Base reactive widget that inherits from flet.Control.
    Combines Flet's rendering with FletX's reactivity system.
    """
    
    _logger = get_logger('FletX.Widget')

    def __init__(self, **kwargs):
        super().__init__()
        self._reactives: Dict[str, Reactive] = {}  # Tracks reactive bindings
        self._props = kwargs                      # Original properties system
        self._is_mounted = False        
        # self.content = self.build()
        
        # Automatic registration for cleanup
        # if AppContext.get_data("page"):
        #     AppContext.get_data("page").add(self)

    def __init_subclass__(cls, **kwargs):
        """Automatically register widget classes with FletXWidgetRegistry"""
        
        super().__init_subclass__(**kwargs)
        # Register the widget class
        FletXWidgetRegistry.register(cls)
        

    @classmethod
    @property
    def logger(cls):
        if not cls._logger:
            cls._logger = get_logger('FletX.Widget')
        return cls._logger
    
    @abstractmethod
    def build(self) -> Union[ft.Control, List[ft.Control]]:
        """
        Builds the widget
        This method is responsible for creating and configuring the widget. 
        It defines the widget's properties and behaviors, such as its appearance, 
        content, and user interactions.
        """
        pass

    def did_mount(self):
        """Called when widget is added to the page"""
        self._is_mounted = True

    def will_unmount(self):
        """Called before widget is removed"""
        self._dispose_reactives()
        self._is_mounted = False
    
    def bind(self, prop_name: str, reactive_obj: Reactive):
        """
        Binds a widget property to a reactive object
        Usage: self.bind("text", rx_text)
        """
        print(f"Binding {prop_name} to {reactive_obj}")
        if not isinstance(reactive_obj, Reactive):
            self.logger.error(
                f"Attempted to bind {prop_name} to a non-reactive object: {reactive_obj}"
            )
            return 
        
        if prop_name in self._reactives:
            self._reactives[prop_name].dispose()
        
        reactive_obj.listen(self._create_update_callback(prop_name))
        self._reactives[prop_name] = reactive_obj
        setattr(self, prop_name, reactive_obj.value)

    def _create_update_callback(self, prop_name: str):
        """Generates a safe update callback"""

        def callback():
            if not self._is_mounted:
                self.logger.warning(
                    f"Attempted to update {self.__class__.__name__}.{prop_name} "
                    "but the widget is not mounted."
                )
                # Optionally, you could raise an exception or log an error
                # raise RuntimeError(f"{self.__class__.__name__} is not mounted")
                # or return to prevent further processing
                return
                
            new_value = self._reactives[prop_name].value
            setattr(self, prop_name, new_value)
            
            # Special handling for Control properties
            if hasattr(self, "content") and isinstance(self.content, ft.Control):
                setattr(self.content, prop_name, new_value)
                
            self.update()
        return callback

    # def _build_add_commands(self, *args, **kwargs) -> None:
    #     """Internal method to add commands to the widget."""
        
    #     return self.build()._build_add_commands(*args, **kwargs)

    def _dispose_reactives(self):
        """Cleanup all reactive bindings"""

        for reactive in self._reactives.values():
            reactive.dispose()
        self._reactives.clear()
    
    # Maintain backwards compatibility
    def get_prop(self, key: str, default: Any = None) -> Any:
        """Retrieves the value of a specific property of the widget."""

        return self._props.get(key, default)
    
    def update_props(self, **kwargs):
        """Updates the widget's properties to reflect changes or new values."""

        self._props.update(kwargs)
        if self._is_mounted:
            self.update()

    # Override ft.Control's methods
    # def _get_control_name(self):
    #     return "fletxwidget"
    
    def _get_children(self):
        content = self.build()
        if isinstance(content, list):
            return content
        return [content] if content else []
    
    def before_update(self):
        """Called before Flet updates the UI"""

        super().before_update()
        if not hasattr(self, "_initialized"):
            self._initialized = True
            self.did_mount()
    
    def render(self) -> Union[ft.Control, List[ft.Control]]:
        """Renders the widget"""
        try:
            return self.build()
        except Exception as e:
            self.logger.error(
                f"Error when trying to render the {self.__class__.__name__} Widget: {e}"
            )
            return ft.Text(f"Error: {e}", color=ft.Colors.RED)