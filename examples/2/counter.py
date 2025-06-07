import flet as ft

from fletx.app import FletXApp
from fletx.core import (
    FletXPage, FletXController, RxInt, RxStr
)
from fletx.decorators import (
simple_reactive,
)


class CounterController(FletXController):
    count = RxInt(0)  # Reactive state


@simple_reactive(
    bindings={
        'value': 'text'
    }
)
class MyReactiveText(ft.Text):

    def __init__(self, rx_text: RxStr, **kwargs):
        self.text: RxStr = rx_text
        super().__init__(**kwargs)

class CounterPage(FletXPage):
    ctrl = CounterController()
    
    def build(self):
        return ft.Column(
            controls = [
                MyReactiveText(rx_text=self.ctrl.count, size=200, weight="bold"),
                ft.ElevatedButton(
                    "Increment",
                    on_click = lambda e: self.ctrl.count.increment()  # Auto UI update
                )
            ]
        )


def main(page: ft.Page):
    page.title = "Counter Example"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.add(CounterPage().build())             # Add the CounterPage to the FletX page
    app = FletXApp(
        routes = {"/": CounterPage}
    )
    app._main(page)                             # Initialize the FletX application with the page

if __name__ == "__main__":
    ft.app(target=main)

