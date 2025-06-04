from typing import Optional, List
from flet import *
from dataclasses import dataclass, field

from fletx.core.state import RxBool, RxStr
from fletx.core.widget import FletXWidget
from fletx.decorators import reactive_control
    

# Reactive Password Field
class ReactivePasswordField(TextField, FletXWidget):
    def __init__(
        self, 
        is_password: RxBool = RxBool(), 
        **kwargs
    ):
        super().__init__(**kwargs)
        FletXWidget.__init__(self, **kwargs)

        self.is_password = is_password
        # print("ReactivePasswordField initialized with reactives:", type(reactives.password))
        self.bind('password', self.is_password)
        # self.bind('label', reactives.label)
        # self.bind('hint_text', reactives.hint_text)
        # self.bind('can_reveal_password', reactives.can_reveal_password)

        
@reactive_control(
    bindings = {
        '_is_done':'is_completed'
    }
)
class TaskComponent(Container):
    """
    Reactive CheckBox widget that integrates with FletX's reactivity system.
    """

    is_completed: RxBool

    def __init__(self, index: int, task_id: str, task_name: str, **kwargs):
        super().__init__(**kwargs)
        self._task_name: str = task_name
        self._task_id: str = task_id
        self.index: int = index

        # Reactive state for task completion
        self.is_completed: RxBool = RxBool(False)
        self._is_done = False

        self.padding = padding.symmetric(horizontal = 15, vertical = 10)
        self.bgcolor = Colors.GREY_900
        self.border_radius = 15
        self.height = 60
        
        # Events
        self.on_click = self._handle_click

        # content
        self.content = self.build()

    def build(self) -> Row:
        return Row(
            expand = False,
            spacing = 15,
            alignment = MainAxisAlignment.START,
            vertical_alignment = CrossAxisAlignment.CENTER,

            # Controls for the task component
            controls = [
                # Icon for the task
                Icon(
                    Icons.CIRCLE_OUTLINED if not self._is_done else Icons.CHECK_CIRCLE,
                    size = 24,
                    color = Colors.GREY_400 if self._is_done else (Colors.BLUE if not self.index % 2 == 0 else Colors.PINK_600),
                ),

                # Text for the task name
                Text(
                    self._task_name,
                    size = 16,
                    weight = FontWeight.NORMAL,
                    color = Colors.WHITE if not self._is_done else Colors.GREY_400,
                    style = TextStyle(
                        decoration = TextDecoration.LINE_THROUGH if self._is_done else TextDecoration.NONE
                    )
                ),
            ]
        )
    
    def _handle_click(self, e):
        """Change the completion state of the task."""
        self.is_completed.toggle()
        # Update UI or perform other actions based on completion state
        print(f"Task {self._task_id} completed: {self._is_done}")
