## FletX - Services

### Overview

**FletX services** are optional components used to **offload responsibilities** from controllers, especially when interacting with external systems like APIs, databases, hardware, or other services.

> 🔸 Business logic **can still be implemented directly in controllers**.
> Services are designed to improve **separation of concerns**, keep controllers lightweight, and make the codebase easier to test and maintain.

---

### 🔌 Integrated HTTP Client

Every service includes an HTTP client (`http_client`) that simplifies remote requests.

```python
from fletx.core import HTTPClient
from fletx.service import FletXService

class UserAPIService(FletXService):
    def __init__(self):
        super().__init__(http_client=HTTPClient("https://api.example.com"))

    def get_users(self):
        return self.http_client.get("/users").json()
```

---

### 🔄 Service Lifecycle

You can override the following lifecycle methods in your service class:

| Method               | Description                            |
| -------------------- | -------------------------------------- |
| `on_start()`         | Called when the service starts         |
| `on_start_async()`   | Async version                          |
| `on_ready()`         | Called when the service is ready       |
| `on_stop()`          | Called when stopping the service       |
| `on_stop_async()`    | Async version                          |
| `on_dispose()`       | Called during final cleanup            |
| `on_state_changed()` | Called when the internal state changes |
| `on_error(error)`    | Triggered when an error occurs         |

Use these hooks to handle service-specific behavior when needed.

---

### 🚦 Service States

A FletX service can be in one of the following states:

* `IDLE`: Initial state
* `LOADING`: A task is running
* `READY`: Service is ready to be used
* `ERROR`: An error occurred
* `DISPOSED`: Service has been disposed from memory

Check `self.state` to access the current status.

---

### ⚙️ Control Methods

| Method            | Description          |
| ----------------- | -------------------- |
| `start()`         | Starts the service   |
| `start_async()`   | Async version        |
| `stop()`          | Stops the service    |
| `stop_async()`    | Async version        |
| `restart()`       | Restarts the service |
| `restart_async()` | Async version        |

---

### 🧪 Full Example

```python
from fletx.core import HTTPClient
from fletx.service import FletXService

class UserAPIService(FletXService):
    def __init__(self):
        super().__init__(http_client=HTTPClient("https://api.example.com"))

    def on_ready(self):
        print("UserAPIService is ready!")

    def get_users(self):
        try:
            return self.http_client.get("/users").json()
        except Exception as e:
            self.set_error(e)
```

---

* Dive into [dependency injection](dependency-injection.md)
* Explore [Controllers](controllers.md)
* Learn about the [Architecture](architecture.md)