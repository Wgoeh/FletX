<p align = 'center'>
    <img src='assets/logo/fletx.png' height = '100' style='height:100px;'></img>
</p>

[![PyPI Version](https://img.shields.io/pypi/v/FletXr)](https://pypi.org/project/FletXr/)
[![Downloads](https://static.pepy.tech/badge/FletXr)](https://pepy.tech/project/FletXr)
[![License](https://img.shields.io/badge/license-MIT-blue)](LICENSE)
[![Discord](https://img.shields.io/discord/1381155066232176670)](https://discord.gg/GRez7BTZVy)
[![GitHub commit activity](https://img.shields.io/github/commit-activity/m/AllDotPy/FletX)]()

#  ✨ Welcome to FletX

<div class="grid cards" markdown>

-   :material-power:{ .lg .middle } __Get Started__

    ---

    Set up **EasySwitch** and make your first API call in minutes.

    [-> Installation Guide](getting-started/installation.md)

-   :material-api:{ .lg .middle } __API Reference__

    ---

    Complete reference for all available methods and configurations.

    [-> API Documentation](api-reference.md)

-   :material-cellphone-arrow-down:{ .lg .middle } __Payment Guides__

    ---

    Learn how to process mobile money payments across different providers.

    [-> Send Payments](guides/payments.md) | [-> Webhooks](guides/webhooks.md)

-   :material-github:{ .lg .middle } __Contribute__

    ---

    Help improve EasySwitch with your contributions and feedback.

    [-> Contribution Guide](contributing.md)

</div>

---

## :material-head-question-outline: ✨ What is FletX?

**FletX** is a lightweight, modular, and reactive architectural framework built on top of [Flet](https://flet.dev), designed to help you build scalable Python UI applications with clean code, structured layers, and modern development patterns.

Inspired by frameworks like **GetX** in the Flutter ecosystem, **FletX** brings separation of concerns, dependency injection, reactive state management, and declarative routing to Flet — without adding unnecessary complexity.


## :material-head-question-outline: ✨ Why FletX?

While Flet offers a powerful UI toolkit in Python, larger apps quickly become hard to maintain without a solid architecture. FletX solves that by introducing:

- ✅ **Reactive state management**  
- ✅ **Modular routing system** with dynamic parameters and guards  
- ✅ **Controllers and services** to separate logic from UI  
- ✅ **Global and local dependency injection**  
- ✅ **Lifecycle hooks** for pages and the app  
- ✅ **Unified configuration with fluent API**  
- ✅ **Built-in support for asynchronous programming**  

---

## 🧠 Philosophy

FletX is built on 3 principles:

1. **Simplicity** — Focus on code clarity and maintainability.
2. **Modularity** — Encourage component-based structure and reusable logic.
3. **Flexibility** — Allow full control over your app flow, while staying non-intrusive.

FletX is *not* a UI library. It doesn’t reinvent Flet’s widgets — it empowers you to use them better by providing a powerful and extensible application layer.

---

Explore further:

- [GitHub Repository](https://github.com/AllDotPy/FletX) for source code and issues
- [PyPI Package](https://pypi.org/project/fletx/) for latest releases
- [Community Forum](#) (coming soon) for support and discussions

## :material-lightning-bolt: Quick Example

```python
import flet as ft

from fletx.app import FletXApp
from fletx.core import (
    FletXPage, FletXController, RxInt, RxStr
)
from fletx.navigation import router_config
from fletx.decorators import (
    simple_reactive
)


class CounterController(FletXController):

    def __init__(self):
        count = RxInt(0)  # Reactive state
        super().__init__()


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


def main():

    # Defining route
    router_config.add_route(
        **{'path': '/', 'component': CounterPage}
    )
    app = FletXApp(
        title = "My Counter",
        initial_route = "/",
        debug = True
    ).with_window_size(400, 600).with_theme(
        ft.Theme(color_scheme_seed=ft.Colors.BLUE)
    )
    
    # Run sync
    app.run()

if __name__ == "__main__":
    main()

```