import flet as ft
from fletx.app import FletXApp
from fletx.core.page import FletXPage
from fletx.core.controller import FletXController
from fletx.core.state import RxInt, RxStr
from fletx.decorators.reactive import computed, watch
from fletx.widgets import ReactiveBuilder
from fletx.decorators.widgets import reactive_control


class CounterController(FletXController):
    count = RxInt(0)  # Reactive state


@reactive_control(
    bindings={
        'value': 'text'
    }
)
class MyReactiveText(ft.Text):

    text: RxStr

    def __init__(self, rx_text: RxStr, **kwargs):
        super().__init__(**kwargs)
        self.text: RxStr = rx_text


class CounterPage(FletXPage):
    ctrl = CounterController()

    # @watch(ctrl.count)
    def my_counter_text(self):
        print("Counter updated:", self.ctrl.count.value)
        return ft.Text(
            f"Count: {self.ctrl.count.value}",
            size=30, 
            weight="bold",
            color=ft.Colors.RED
        )

    
    def build(self):
        return ft.Column(
            controls = [
                MyReactiveText(rx_text=self.ctrl.count, size=30, weight="bold"),
                MyReactiveText(rx_text=self.ctrl.count, size=30, weight="bold"),
                MyReactiveText(rx_text=self.ctrl.count, size=30, weight="bold"),
                # self.my_counter_text(),  # Reactive text that updates automatically
                ReactiveBuilder(
                    builder=self.my_counter_text,
                    dependencies=[self.ctrl.count]
                ),
                MyReactiveText(rx_text=self.ctrl.count, size=30, weight="bold"),
                ft.ElevatedButton(
                    "Increment",
                    on_click=lambda e: self.ctrl.count.increment()  # Auto UI update
                )
            ]
        )


def main(page: ft.Page):
    page.title = "Counter Example"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.add(CounterPage().build())  # Add the CounterPage to the FletX page
    app = FletXApp(routes={"/": CounterPage})
    app._main(page)  # Initialize the FletX application with the page

if __name__ == "__main__":
    ft.app(target=main)

