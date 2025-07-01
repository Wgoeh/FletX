<!-- # 📘 **FletX Controllers** – Complete and Thorough Guide -->

## 🔰 Introduction

In FletX, the `FletXController` is the **core unit for business logic and state management**. It connects:

* The **reactive UI components** (Flet widgets turned reactive),
* The **application state** (data, events, and global contexts),
* The **external services** (APIs, databases, auth systems, etc.).

The controller’s goal is to **separate business logic from UI logic**, promoting a **clean, testable, and reactive architecture**.

---

## 🧩 Why Controllers?

Let’s say you’re building an application with:

* A login screen,
* A user dashboard,
* A shared todo system.

Each of these views can have its own **controller**, which:

* Maintains local **reactive variables**,
* Responds to **user interactions** (clicks, input changes),
* **Emits or listens to events** across components,
* Shares or reads **global context values** (user info, theme),
* Manages **side effects** (notifications, redirections, loading states, etc.).

---

## 🏗️ Controller Structure Overview

```python
class MyController(FletXController):
    def __init__(self):
        super().__init__()

        # Reactive states
        self.username = self.create_rx_str("")
        self.is_loading = self.create_rx_bool(False)
        self.error_message = self.create_rx_str("")

        # Reactive effect
        self.use_effect(self.handle_username_change, deps=[self.username])

    def handle_username_change(self):
        print(f"Username changed to: {self.username.value}")

    def on_ready(self):
        print("Controller is ready!")
```

---

## 🧠 1. Built-in Reactive Variables

Controllers offer convenient helpers to generate reactive variables that automatically clean up with the controller’s lifecycle.

```python
# Create reactive values
username = controller.create_rx_str("John")
age = controller.create_rx_int(30)
is_logged_in = controller.create_rx_bool(False)
tasks = controller.create_rx_list([])
profile = controller.create_rx_dict({"email": "john@example.com"})
```

### 🔁 Computed Properties

Computed properties are reactive values **derived from other reactive variables**:

```python
full_info = controller.create_computed(
    lambda: f"{username.value} ({age.value} years old)"
)
```

These are automatically re-evaluated when their dependencies change.

---

## 🎯 2. Reactive Effects

You can attach reactive **effects** to the controller. These functions automatically execute when one or more reactive dependencies change:

```python
controller.use_effect(
    lambda: print(f"Username is now: {username.value}"),
    deps=[username]
)
```

These are useful for:

* Triggering API calls,
* Syncing values between views,
* Automatically persisting changes to storage, etc.

---

## 🔄 3. Built-in Reactive State

Each controller includes **predefined states** for common usage:

| Property        | Description                               |
| --------------- | ----------------------------------------- |
| `is_loading`    | Indicates if a loading process is ongoing |
| `error_message` | Holds an error message to show in the UI  |
| `state`         | General purpose reactive state object     |

```python
controller.is_loading.listen(lambda: print("Loading..."))
controller.error_message.value = "Invalid credentials"
```

---

## 📡 4. Local and Global Event Bus

Each controller includes a **reactive Event Bus**, allowing you to **emit and listen to custom events**, either:

* **Locally** (within the same controller instance),
* Or **Globally** (across all controllers in the app).

### ✅ Emit Events

```python
controller.emit_local("user_updated", {"name": "Alice"})
controller.emit_global("theme_changed", {"dark_mode": True})
```

### 🎧 Listen to Events

```python
events = controller.listen_reactive_local("user_updated")
events.listen(lambda: print(f"User events: {len(events.value)}"))

# You can access:
print(controller.event_bus.event_history.value)
print(controller.event_bus.last_event.value)
```

---

## 🌐 5. Local and Global Context

FletXController provides a **reactive context system** to store and share values:

* Between views (global),
* Within the current controller (local).

### 📥 Set Context

```python
controller.set_context("current_user", {"id": 1, "name": "John"})
```

### 📤 Get Context (reactively or not)

```python
# Reactive version
rx_user = controller.get_context_reactive("current_user")
rx_user.listen(lambda: print(f"User updated: {rx_user.value}"))

# Reactive check
has_user = controller.has_context_reactive("current_user")
has_user.listen(lambda: print("User exists" if has_user.value else "No user"))

# Non-reactive version
user = controller.get_context("current_user")
```

This system helps decouple logic between parts of your app.

---

## ⏳ 6. Lifecycle Hooks

FletXController includes three lifecycle hooks to help you run code at different stages:

```python
class MyController(FletXController):

    def on_initialized(self):
        # Called during controller instantiation
        print("Controller initialized")

    def on_ready(self):
        # Called when UI is mounted and ready
        print("Controller is ready")

    def on_disposed(self):
        # Called when the controller is destroyed
        print("Controller disposed")
```

These hooks help with initialization logic, data fetching, or cleanup.

---

## 🧪 Full Example

```python
class LoginController(FletXController):
    def __init__(self):
        super().__init__()
        self.username = self.create_rx_str("")
        self.password = self.create_rx_str("")
        self.login_error = self.create_rx_str("")

    def on_ready(self):
        self.username.listen(self.validate_form)
        self.password.listen(self.validate_form)

    def validate_form(self):
        if self.username.value and self.password.value:
            self.login_error.value = ""
        else:
            self.login_error.value = "All fields are required"
```

---

## 📝 Summary Table

| Feature            | Description                                              |
| ------------------ | -------------------------------------------------------- |
| Reactive Variables | Easy-to-create reactive values (`RxBool`, `RxStr`, etc.) |
| Computed Values    | Derived state from other variables                       |
| Reactive Effects   | Triggers logic when values change                        |
| Event Bus          | Reactive local & global events                           |
| Context System     | Shared state (reactive) across or within controllers     |
| Built-in State     | Common states like `is_loading`, `error_message`, etc.   |
| Lifecycle Hooks    | `on_initialized`, `on_ready`, `on_disposed`              |

---

## 🧠 Next Steps

* Explore [Page (Views)](pages.md)
* Learn about the [Architecture](architecture.md)
* Dive into [dependency injection](guides/dependency-injection.md)
