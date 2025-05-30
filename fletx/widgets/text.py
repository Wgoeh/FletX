"""
Widget Text personnalisé pour FletX
"""

import flet as ft
from typing import Optional, Union
from fletx.core.widget import FletXWidget

class FletXText(FletXWidget):
    """Widget Text personnalisé"""
    
    def __init__(
        self, 
        text: str = "",
        size: Optional[float] = None,
        color: Optional[str] = None,
        weight: Optional[ft.FontWeight] = None,
        italic: bool = False,
        **kwargs
    ):
        super().__init__(
            text=text,
            size=size,
            color=color,
            weight=weight,
            italic=italic,
            **kwargs
        )
    
    def build(self) -> ft.Control:
        """Construit le widget Text"""
        return ft.Text(
            value=self.get_prop('text', ""),
            size=self.get_prop('size'),
            color=self.get_prop('color'),
            weight=self.get_prop('weight'),
            italic=self.get_prop('italic', False),
            **{k: v for k, v in self.props.items() 
               if k not in ['text', 'size', 'color', 'weight', 'italic']}
        )