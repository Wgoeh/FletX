# Using Pages in FletX
### 🔷 What is a `FletXPage`?

A `FletXPage` represents **a single screen or view** in a FletX application. It is the fundamental building block of the user interface and typically corresponds to a page the user navigates to.

Each page is designed to:

* Define its UI layout using a `build()` method
* Respond to lifecycle events (`on_init`, `on_destroy`)
* React to state changes and side effects
* Add contextual keyboard shortcuts
* Interact with controllers using reactive data listening

---

### 🔁 Page Lifecycle in FletX

FletXPages go through a **structured lifecycle**, with each state representing a phase in the page’s existence. Understanding these states is crucial to managing page behavior correctly.

| State          | Description                                                                     |
| -------------- | ------------------------------------------------------------------------------- |
| `INITIALIZING` | The page is being initialized but not yet visible                               |
| `MOUNTED`      | The page has been mounted in the UI, but might not be active                    |
| `ACTIVE`       | The page is fully visible and has focus (can respond to input)                  |
| `INACTIVE`     | The page is still mounted but currently inactive (e.g., another page is active) |
| `UNMOUNTING`   | The page is about to be removed from the UI                                     |
| `DISPOSED`     | The page has been destroyed and its resources cleaned up                        |

---

### 🧩 Lifecycle Hook Methods

FletXPages provide lifecycle hooks that allow you to define behaviors when the page appears or disappears.

#### `on_init(self)`

This method is called **before the page becomes visible**. You should use it to:

* Initialize or fetch data
* Subscribe to signals from controllers
* Set up any one-time effects or listeners

#### `on_destroy(self)`

This method is called **just before the page is unmounted and destroyed**. It’s useful to:

* Unsubscribe from observers
* Cancel background tasks
* Clear resources

These methods give you control over the page's initialization and teardown logic.

---

### 🛠️ The `build()` Method – Defining the UI

Every `FletXPage` must define a `build()` method. This method returns the actual content of the page using Flet UI elements.

```python
def build(self):
    return ft.Column([
        ft.Text("Page Title"),
        ft.ElevatedButton("Click Me", on_click=self.handle_click)
    ])
```

This method is automatically called when the page is rendered. It should be fast, pure, and declarative.

---

### 🎯 Handling Side Effects with `EffectManager`

FletX provides a built-in effect manager to help you manage **reactive side effects**. These are actions triggered by changes in observable data or controller state.

You can add effects using listeners:

```python
# React to loading state
self.controller.is_loading.listen(self.show_loader)

# React to controller readiness
self.controller.is_ready.listen(self.load_data)
```

These effects are **automatically cleaned up** when the page is destroyed, making them safe and maintainable.

---

### ⌨️ Adding Keyboard Shortcuts

You can enable contextual **keyboard shortcuts** on a FletXPage by passing `enable_keyboard_shortcuts=True` in the constructor.

```python
self.add_keyboard_shortcut("ctrl+r", self.refresh, "Refresh the page")
self.add_keyboard_shortcut("ctrl+h", self.go_home, "Navigate home")
```

> ⚠️ Shortcuts are only active when the page is in `MOUNTED` or `ACTIVE` state.

This feature improves productivity and accessibility for power users.

---

### 🔗 Interacting with Controllers

A `FletXPage` can work with controllers to handle complex logic or manage data. Pages can:

* Observe reactive properties from the controller
* Listen to loading or error states
* Call controller methods to fetch or mutate data

```python
# Subscribe to reactive controller states
self.controller = HomeController()
self.controller.is_loading.listen(self.show_loader)
self.controller.error_message.listen(self.show_error)
```

This ensures your page stays in sync with the application logic and state.

---

### ✅ Complete Example of a `FletXPage`

```python
class HomePage(FletXPage):
    def __init__(self):
        super().__init__(
            padding=20,
            bgcolor=ft.colors.BLUE_GREY_50,
            border_radius=10,
            enable_keyboard_shortcuts=True
        )

        
        # Register keyboard shortcuts
        self.add_keyboard_shortcut("ctrl+r", self.refresh, "Refresh the page")
        self.add_keyboard_shortcut("ctrl+h", self.go_home, "Go to home page")

        # Inject HomeController
        self.controller = FletX.put(HomeController(),'home_conroller')
        # Connect to controller and listen for state changes
        self.controller.is_loading.listen(self.show_loader)

    def on_init(self):
        # Trigger actions when the page is initialized
        self.controller.load_data()
        self.controller.error_message.listen(self.show_snackbar)

    def on_destroy(self):
        print("HomePage is being destroyed...")

    def build(self):
        return ft.Column([
            ft.Text("Welcome to FletX!", size=24),
            ft.ElevatedButton("Show Dialog", on_click=self.show_sample_dialog),
            ft.ElevatedButton("Show Snackbar", on_click=self.show_snackbar)
        ])

    def refresh(self, _=None):
        self.controller.load_data()

    def go_home(self, _=None):
        self.router.go("/home")

    def show_sample_dialog(self, _=None):
        self.dialog("This is a sample dialog.")

    def show_snackbar(self, _=None):
        self.snackbar("Something went wrong.")

    def show_loader(self, is_loading):
        if is_loading:
            self.dialog("Loading, please wait...")
```

---

### 📌 Summary Table

| Feature                   | Purpose                                          |
| ------------------------- | ------------------------------------------------ |
| `on_init` / `on_destroy`  | Handle page initialization and cleanup           |
| `build()`                 | Define the UI layout using Flet widgets          |
| `add_keyboard_shortcut()` | Add contextual keyboard actions                  |
| `controller.listen(...)`  | React to observable changes from controllers     |
| `EffectManager`           | Manage side effects in a structured and safe way |

---

## 🧠 Next Steps

* Explore the [Routing System](pages.md)
* Learn about the [Architecture](architecture.md)
* Dive into [dependency injection](guides/dependency-injection.md)
