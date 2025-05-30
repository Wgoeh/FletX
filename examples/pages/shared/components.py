from typing import Optional
from flet import *
from dataclasses import dataclass

from fletx.core.state import RxBool, RxStr
from fletx.core.widget import FletXWidget
from fletx.core.router import FletXRouter

# class AppHeader(FletXWidget):
#     """En-tête réutilisable"""
    
#     def __init__(self, title: str):
#         super().__init__(title=title)
    
#     def build(self) -> Control:
#         return Row(
#             controls=[
#                 Text(self.get_prop('title'), size=20, weight="bold"),
#                 IconButton(Icons.SETTINGS, on_click=lambda e: FletXRouter.to("/settings"))
#             ],
#             alignment="spaceBetween"
#         )

@dataclass
class ReactiveTextFieldProps:
    can_reveal_password: RxBool = RxBool(False)
    value: RxStr = RxStr("")
    label: RxStr = RxStr("")
    hint_text: RxStr = RxStr("")
    password: RxBool = RxBool(False)
    
class ReactivePasswordField(TextField, FletXWidget):
    def __init__(
        self, 
        reactives: ReactiveTextFieldProps = ReactiveTextFieldProps(), 
        **kwargs
    ):
        super().__init__(**kwargs)
        FletXWidget.__init__(self, **kwargs)
        print("ReactivePasswordField initialized with reactives:", type(reactives.password))
        self.bind('password', reactives.password)
        # self.bind('label', reactives.label)
        # self.bind('hint_text', reactives.hint_text)
        # self.bind('can_reveal_password', reactives.can_reveal_password)

        