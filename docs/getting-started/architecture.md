# 🏗️ FletX Architecture

FletX is built on a **modular and reactive architecture** designed to help developers structure Flet applications in a clean, maintainable, and scalable way. It is inspired by principles like separation of concerns and dependency injection.

---

## 📚 Overview

FletX architecture revolves around three **core components**:

1. **Pages (`FletXPage`)** – declarative, reactive UI components.
2. **Controllers (`FletXController`)** – business logic and state management.
3. **Services (optional)** – reusable utilities for API calls, database access, etc.

---

### 🔄 Typical Flow

A typical user interaction flows like this:

```plaintext
User Action → Controller Logic → State Update → UI Re-render
```

When routing/navigation happens, it flows like this:

```plaintext
Routing → Page Instantiation → Controller Injection → Build UI
```

---

## 🧱 Core Building Blocks

### 1. FletXPage

A **FletXPage** is a class that represents a visual page (screen) in your app. It inherits from `FletXPage` and defines a `build()` method that returns a reactive Flet UI.

#### Example:

```python
class HomePage(FletXPage):
    ctrl = HomeController()

    def build(self):
        return ft.Column([
            ft.Text(lambda: str(self.ctrl.counter()), size=40),
            ft.ElevatedButton("Increment", on_click=lambda e: self.ctrl.counter.increment())
        ])
```

---

### 2. FletXController

A **FletXController** handles **business logic**, manages **reactive state**, and is tied to a specific page. It uses observable values to trigger UI updates automatically.

#### Example:

```python
class HomeController(FletXController):
    def __init__(self):
        self.counter = RxInt(0)
        super().__init__()
```

`RxInt` is a reactive object provided by FletX. Updating it automatically refreshes all widgets that depend on it.

---

## 🔗 Navigation & Routing

FletX provides a centralized router configuration (`router_config`) for managing navigation across your app:

```python
router_config.add_route("/", HomePage)
router_config.add_route("/about", AboutPage)

# Or register a list of routes
router_config.add_routes([
    {"path": "/", "component": HomePage},
    {"path": "/settings", "component": SettingsPage}
])
```

> You can define dynamic routes like:

```python
router_config.add_route("/user/:id", UserPage)
router_config.add_route("/user/*category", CategoryPage)
```

In your page:

```python
def build(self):
    user_id = self.route_info.params["id"]
```

---

## 🧠 Reactive State Management

FletX provides **reactive variables**: `RxInt`, `RxStr`, `RxList`, etc., which track their values and trigger UI updates when modified.

#### Example:

```python
class CounterController(FletXController):
    def __init__(self):
        self.count = RxInt(0)
        super().__init__()

class CounterPage(FletXPage):
    ctrl = CounterController()

    def build(self):
        return MyReactiveText(rx_text=self.ctrl.count, size=200, weight="bold"),
```

> `lambda:` makes the widget reactive — it will re-render automatically when the value changes.

---

## 🧩 Services (Optional)

**Services** are reusable, testable classes used for accessing APIs, databases, or any shared logic. They can be injected into controllers.

#### Example:

```python
class UserService:
    def fetch_user(self, user_id):
        return {"id": user_id, "name": "John Doe"}
```

Used in a controller:

```python
class UserController(FletXController):
    def __init__(self):
        self.user_service = FletX.find(UserService)
        self.user = RxDict({})
        super().__init__()

    def load_user(self, user_id):
        self.user.value =  self.user_service.fetch_user(user_id)
```

---

## 🧪 Minimal Architecture Example

Here’s a minimal FletX app putting all the pieces together:

```python
# main.py
from fletx.app import FletXApp
from fletx.navigation import router_config
from .pages.counter import CounterPage

router_config.add_route("/", CounterPage)

app = FletXApp(title="Demo App")
app.run()
```

```python
# pages/counter.py
from fletx.core import FletXPage
from .controllers.counter import CounterController
from .components.reactive_text import MyReactiveText
import flet as ft

class CounterPage(FletXPage):
    ctrl = CounterController()

    def build(self):
        return ft.Column([
            MyReactiveText(rx_text=self.ctrl.count, size=40, weight="bold"),
            ft.ElevatedButton("Increment", on_click=lambda e: self.ctrl.count.increment())
        ])
```

```python
# components/reactive_text.py
import flet as ft
from fletx.decorators import simple_reactive

@simple_reactive(bindings={'value': 'text'})
class MyReactiveText(ft.Text):

    def __init__(self, rx_text: RxStr, **kwargs):
        self.text: RxStr = rx_text
        super().__init__(**kwargs)
```

```python
# controllers/counter.py
from fletx.core import FletXController, RxInt

class CounterController(FletXController):
    def __init__(self):
        self.count = RxInt(0)
        super().__init__()
```

---

## ✅ Summary Table

| Component         | Responsibility                           |
| ----------------- | ---------------------------------------- |
| `FletXPage`       | Builds the UI, binds to controller       |
| `FletXController` | Holds business logic and reactive state  |
| `Rx*` objects     | Reactive state (trigger UI rebuilds)     |
| `router_config`   | Defines app navigation routes            |
| Services          | Shared utilities for APIs, storage, etc. |


---


## 🧠 Next Steps

* Explore [reactive UI binding](ui/reactivity.md)
* Learn about the [Architecture](architecture.md)
* Dive into [dependency injection](guides/dependency-injection.md)