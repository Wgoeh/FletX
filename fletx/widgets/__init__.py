from functools import wraps
from typing import get_type_hints
from fletx.core.state import (
    Reactive, RxInt, RxStr, RxBool, RxList, RxDict 
)

def reactive_control(cls):
    """
    Décorateur qui transforme un contrôle Flet en widget réactif
    avec liaison automatique des propriétés Rx.
    """
    class ReactiveControl(cls):
        def __init__(self, **kwargs):
            # Séparation des props réactives et normales
            reactive_props = {}
            normal_props = {}
            
            for k, v in kwargs.items():
                if isinstance(v, (Reactive, RxInt, RxStr, RxBool, RxList, RxDict)):
                    reactive_props[k] = v
                else:
                    normal_props[k] = v
            
            # Initialisation du widget parent
            super().__init__(**normal_props)
            
            # Liaison automatique des propriétés réactives
            self._reactive_bindings = {}
            for prop_name, rx_obj in reactive_props.items():
                self._bind_reactive(prop_name, rx_obj)
        
        def _bind_reactive(self, prop_name: str, rx_obj: Reactive):
            """Crée une liaison bidirectionnelle"""
            # Initialisation de la valeur
            setattr(self, prop_name, rx_obj.value)
            
            # Mise à jour du widget quand Rx change
            def update_widget(value):
                setattr(self, prop_name, value)
                if hasattr(self, 'update'):
                    self.update()
            
            cleanup = rx_obj.listen(update_widget)
            self._reactive_bindings[prop_name] = cleanup
            
            # Mise à jour de Rx quand le widget change (si événement disponible)
            widget_event = f"on_{prop_name}_change"
            if hasattr(self, widget_event):
                def handle_change(e):
                    rx_obj.value = getattr(self, prop_name)
                setattr(self, widget_event, handle_change)
        
        def dispose(self):
            """Nettoyage des liaisons réactives"""
            for cleanup in self._reactive_bindings.values():
                cleanup()
            self._reactive_bindings.clear()
            if hasattr(super(), 'dispose'):
                super().dispose()
    
    return ReactiveControl