import flet as ft
from fletx.core import (
    FletXPage
)

from ..controllers.counter import CounterController
from ..components import MyReactiveText


class CounterPage(FletXPage):
    ctrl = CounterController()
    
    def build(self):
        return ft.Column(
            alignment = ft.MainAxisAlignment.CENTER,
            horizontal_alignment = ft.CrossAxisAlignment.CENTER,
            spacing = 20,
            controls = [
                ft.Text(
                    "{{ project_name }} Counter",
                    size = 40,
                    weight = ft.FontWeight.BOLD
                ),
                MyReactiveText(
                    rx_text = self.ctrl.count, # Auto update when count changes
                    size = 100, 
                    weight = ft.FontWeight.BOLD
                ),
                ft.ElevatedButton(
                    "Increment",
                    on_click=lambda e: self.ctrl.count.increment()  # Auto UI update
                )
            ]
        )