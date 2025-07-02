# 💉 Dependency Injection (DI) with `FletX`

FletX provides a lightweight and flexible **manual dependency injection system**, inspired by `GetX`. It allows you to **register and retrieve singleton instances** of your services, repositories, and other dependencies from anywhere in your app.

---

### 🚀 Getting Started

All interactions with the DI container are done via the `FletX` class:

```python
from fletx import FletX
```

This exposes the following methods:

| Method                  | Description                            |
| ----------------------- | -------------------------------------- |
| `FletX.put(instance)`   | Registers a singleton instance         |
| `FletX.find(MyClass)`   | Retrieves the registered instance      |
| `FletX.delete(MyClass)` | Removes an instance from the container |
| `FletX.reset()`         | Clears the entire DI container         |

---

### ✅ Registering an Instance

```python
from fletx import FletX

class AuthService:
    def __init__(self):
        self.user = None

    def login(self, username):
        self.user = username

FletX.put(AuthService())
```

> This registers a **singleton** of `AuthService` that you can use throughout your app.

---

### 📦 Retrieving an Instance

```python
auth = FletX.find(AuthService)
auth.login("johndoe")
```

> This retrieves the instance you registered with `FletX.put()`.

---

### 🏷 Using Tags

If you need multiple versions of the same class:

```python
FletX.put(AuthService(), tag="admin")
FletX.put(AuthService(), tag="user")

admin_auth = FletX.find(AuthService, tag="admin")
user_auth = FletX.find(AuthService, tag="user")
```

---

### 🧹 Deleting and Resetting

```python
FletX.delete(AuthService)
FletX.reset()
```

> `delete()` removes a single instance; `reset()` clears the entire container.

---

### 🧪 Example Usage

#### Step 1: Register your service

```python
FletX.put(AuthService())
```

#### Step 2: Retrieve and use it in your view, route, or controller

```python
class Dashboard:
    def __init__(self):
        self.auth = FletX.find(AuthService)

    def do_stuff(self):
       ...
```

---

### ⚠️ Notes

* 🧠 FletX **does not support automatic dependency resolution** (e.g., constructor or function injection) yet.
* 💡 You must **manually retrieve your dependencies** using `FletX.find()`.

---

### 📝 Recap

| Task               | Code Example                      |
| ------------------ | --------------------------------- |
| Register a service | `FletX.put(MyService())`          |
| Retrieve a service | `FletX.find(MyService)`           |
| Register multiple  | `FletX.put(MyService(), tag="x")` |
| Retrieve with tag  | `FletX.find(MyService, tag="x")`  |
| Remove a service   | `FletX.delete(MyService)`         |
| Clear all services | `FletX.reset()`                   |

---

## 🧠 Next Steps

* Explore [sevices](services.md)
* Dive into [routing](routing.md)
* Learn about the [Architecture](architecture.md)
