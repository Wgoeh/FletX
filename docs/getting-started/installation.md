# 🚀 Getting Started with FletX

Welcome to the official getting started guide for **FletX** — the reactive and modular application architecture for [Flet](https://flet.dev) in Python.

This guide will walk you through:

* Installation
* Creating your first FletX app
* Directory structure
* CLI usage and commands

---

## 🧱 Prerequisites

Before starting, make sure you have:

* Python 3.12
* `pip` (Python package manager)

---

## 📦 Installation

```bash
pip install flet fletxr
```

> ✅ This will install both Flet and FletX. `fletxr` is the official package name on PyPI.

---

## 🧪 Creating Your First App

You can either start manually or use the FletX CLI. Let’s explore both options:

### Option 1: Manual Setup

Create a file `main.py`:

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
        self.count = RxInt(0)
        super().__init__()


@simple_reactive(bindings={'value': 'text'})
class MyReactiveText(ft.Text):

    def __init__(self, rx_text: RxStr, **kwargs):
        self.text: RxStr = rx_text
        super().__init__(**kwargs)


class CounterPage(FletXPage):
    ctrl = CounterController()

    def build(self):
        return ft.Column(
            controls=[
                MyReactiveText(rx_text=self.ctrl.count, size=200, weight="bold"),
                ft.ElevatedButton(
                    "Increment",
                    on_click=lambda e: self.ctrl.count.increment()
                )
            ]
        )


def main():
    router_config.add_route(path='/', component=CounterPage)
    app = FletXApp(
        title="My Counter",
        initial_route="/",
        debug=True
    ).with_window_size(400, 600).with_theme(
        ft.Theme(color_scheme_seed=ft.Colors.BLUE)
    )

    app.run()


if __name__ == "__main__":
    main()
```

Run the app:

```bash
# Standard way
python main.py

# Or using flet
flet run main.py
```

### Option 2: Using the CLI

Use the FletX CLI to scaffold a new project:

```bash
fletx new my_app

# Navigate into the project folder
cd my_app

# Run the project
fletx run 
```

---

## 📁 Project Structure

```
my_project/
├── app/
│   ├── controllers/     # Business logic controllers
│   ├── services/       # Business services and API calls
│   ├── models/         # Data models
│   ├── components/     # Reusable widgets
│   ├── pages/          # Application pages
│   └── routes.py       # App routing modules
├── assets/             # Static assets (images, fonts, etc.)
├── tests/              # Test files
├── .python-version     # Python version
├── pyproject.toml      # Python dependencies
├── README.md           # Quick start README
└── main.py            # Application entry point
```

---

## ⚙️ CLI Documentation

The **FletX CLI** (`fletx`) is a command-line tool that makes it easy to manage **FletX** projects. It lets you:

* Create a new FletX project
* Generate components (controllers, services, pages, etc.)
* Run your project with various options

---

## Main command

```bash
fletx <command> [options]
```

---

## Available commands

| Category               | Command    | Description                                          |
| ---------------------- | ---------- | ---------------------------------------------------- |
| **Project Management** | `new`      | Create a new FletX project from template             |
| **Code Generation**    | `generate` | Generate components like controllers, services, etc. |
| **Utilities**          | `run`      | Run a FletX project with various options             |

👉 **Specific help :**

```bash
fletx <command> --help
fletx help <command>
```

---

## `fletx new`

Create a new FletX project.

```bash
fletx new <project_name> [options]
```

### Options

| Option                            | Description                                           | Default           |
| --------------------------------- | ----------------------------------------------------- | ----------------- |
| `--template TEMPLATE`             | Template to use for the project                       | `project`         |
| `--directory DIRECTORY`           | Directory where the project will be created           | current directory |
| `--author AUTHOR`                 | Author name for the project                           |                   |
| `--description DESCRIPTION`       | Project description                                   |                   |
| `--version VERSION`               | Initial version of the project                        | `0.1.0`           |
| `--python-version PYTHON_VERSION` | Minimum required Python version                       | `3.12`            |
| `--overwrite`                     | Overwrite existing files if they exist                |                   |
| `--no-install`                    | Don't install dependencies after creating the project |                   |

---

## `fletx generate`

Generate a component for your project.

```bash
fletx generate <type> <name> [options]
```

where `<type>` can be: `controller`, `service`, `model`, `component`, `page`

### Options

| Option                    | Description                            | Default       |
| ------------------------- | -------------------------------------- | ------------- |
| `--output-dir OUTPUT_DIR` | Output directory                       | based on type |
| `--template TEMPLATE`     | Specific template to use               | based on type |
| `--overwrite`             | Overwrite existing files               |               |
| `--with-test`             | Generate a test file for the component |               |

---

## `fletx run`

Run your FletX project.

```bash
fletx run [target] [options]
```

where `target` is the Python file to run (default: `main.py`)

### Options

| Option                        | Description                         | Default     |
| ----------------------------- | ----------------------------------- | ----------- |
| `--host HOST`                 | Host to bind to                     | `localhost` |
| `--port PORT`                 | Port to bind to                     | `8550`      |
| `--debug`                     | Run in debug mode                   |             |
| `--watch`                     | Enable hot reload (directory watch) |             |
| `--web`                       | Open in a web browser               |             |
| `--desktop`                   | Force desktop mode                  |             |
| `--android`                   | Open on an Android device           |             |
| `--ios`                       | Open on an iOS device               |             |
| `--assets-dir ASSETS_DIR`     | Path to assets directory            |             |
| `--ignore-dir IGNORE_DIR`     | Path to ignore directory            |             |
| `--env ENV`                   | Environment variables `KEY=VALUE`   |             |
| `--requirements REQUIREMENTS` | Path to `requirements.txt` file     |             |
| `--install-deps`              | Install dependencies before running |             |
| `--verbose`                   | Verbose output                      |             |

---

## Example: Create and run

```bash
# Create a project
fletx new my_project --author "John Doe" --description "My FletX app"

# Generate a controller
fletx generate controller MyController --with-test

# Run the project
fletx run --web --debug
```

---

## 🧠 Next Steps

* Learn about [state management](state-management.md)
* Explore [reactive UI binding](ui/reactivity.md)
* Dive into [dependency injection](guides/dependency-injection.md)

---

FletX makes architecture clean — so you can focus on building features, not structure.

Happy coding! 🚀
