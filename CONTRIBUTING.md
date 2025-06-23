# Contributing to FletX

Thank you for your interest in FletX! 🎉 This comprehensive guide outlines how to contribute effectively.

## 📋 Table of Contents
1. [Getting Started](#-getting-started)
2. [Project Structure](#-project-structure)
3. [Development Workflow](#-development-workflow)
4. [Code Conventions](#-code-conventions)
5. [Testing & Quality](#-testing--quality)
6. [Documentation](#-documentation)
7. [Reporting Bugs](#-reporting-bugs)
8. [Feature Proposals](#-feature-proposals)
9. [Code of Conduct](#-code-of-conduct)

## 🚀 Getting Started

### Local Setup

1. **Clone the repository**
```bash
git clone https://github.com/AllDotPy/FletX.git
cd FletX
```

2. **Set up virtual environment** (Recommended: UV)
```bash
pip install uv
uv venv
source venv/bin/activate  # Linux/Mac
# or .\venv\Scripts\activate  # Windows
```

3. **Install dependencies**
```bash
uv pip install -e .[dev]  # Development mode
```

4. **Verify installation**
```bash
pytest tests/
```

## 🏗 Project Structure

```sh
.
├── CONTRIBUTING.md
├── LICENSE
├── README.md
├── architecture.svg
├── docs/
├── examples/
├── fletx
│   ├── __init__.py
│   ├── app.py
│   ├── core
│   │   ├── __init__.py
│   │   ├── controller.py
│   │   ├── di.py
│   │   ├── effects.py
│   │   ├── factory.py
│   │   ├── navigation
│   │   │   ├── guards.py
│   │   │   ├── middleware.py
│   │   │   └── transitions.py
│   │   ├── observer.py
│   │   ├── page.py
│   │   ├── route_config.py
│   │   ├── router.py
│   │   ├── state.py
│   │   ├── types.py
│   │   └── widget.py
│   ├── decorators
│   │   ├── controllers.py
│   │   ├── reactive.py
│   │   └── route.py
│   ├── utils
│   │   ├── __init__.py
│   │   ├── context.py
│   │   ├── exceptions.py
│   │   └── logger.py
│   └── widgets
│       ├── __init__.py
│       └── text.py
├── main.py
├── pyproject.toml
└── setup.py
```

## Roadmap 🗺️

- [x] **Step 1** — **Fondation**
    > ⚙️ **Goal** : build thechnical bases and essential abstractions. 
- [x] **Step 2** — **State Management + DI**
    > 🎯 **Goal** : Enable reactive state management.
- [x] **Step 3** — **Advanced navigation**
    > 🧭 **Goal** : Add support for modular and nested routing, middlewares and Guards.
- [x] **Step 4** — **Utilities & CLI**
    > 🛠️ **Goal** : Add tools to boost DX (developer experience).
- [ ] **Step 5** — **UI Components**
    > 🧱 **Goal** : Add ready to use reactive UI components (enabling extensibility).
- [ ] **Step 6** — **Write Documentation**
    > 📚 **Goal** : Write FletX's documentation.

### Currently Working on

- [x] Add @reactive_control to allow converting flet Controls into a FletX reactive Widgets
- [x] FletX CLI tool Eg: `fletx new my_project`; `fletx generate module my_project/my_module`
- [x] Improve Actual routing system (enabling devs to create subrouters for modules)
- [x] FLetXPage enhancement (hooks, events and more)
- [x] Improve `FletXController` class making it more flexible
- [x] Improve worker system (Actually can't correctly share same worker pool between worker tasks).
- [x] Fix Route Transition Issues 
- [x] Add Http Wrapper (using `httpx` or `aiohttp`)
- [x] Add A FletX Application Service Base class.

### Todo

- [ ] Add Services generation template and command to the CLI
- [ ] Add Ready to use Reactive Widgets or components
- [ ] Add Screen Management System for Page Widgets 
- [ ] Write Documentation
- [ ] Enhanced dev tools

---

## 🔄 Development Workflow

1. **Create a branch**  
   Branch from `master` with descriptive naming:
   ```bash
   git checkout -b feat/new-reactive-component
   ```

2. **Implement changes**  
   - Keep commits atomic
   - Document new features

3. **Run tests**
```bash
uv pip install -e .[test]
pytest tests/
```

4. **Submit a Pull Request**
   - Clearly describe changes
   - Reference related issues
   - Address code review feedback

## ✨ Code Conventions

### Style Guide
- Follow PEP 8 (88 chars max line length)
- Type hints for all public functions
- Google-style docstrings for key modules

### Reactivity Pattern
```python
# Good
class ReactiveButton(ft.ElevatedButton, FletXWidget):
    """ My Reactive Button which.... """

    def __init__(self, text: RxStr, **kwargs):
        super().__init__(**kwargs)
        # Create a reactive object
        self.rx_text: RxStr = RxStr('')
        # And bind it to self (@ft.ElevatedButton) text attribute
        self.bind('text', self.rx_text)
```

### Widget Standards
- Prefix reactive widgets with `Reactive`
- Isolate state logic in dedicated classes

## 🧪 Testing & Quality

### Running Tests
```bash
pytest tests/ --cov=fletx --cov-report=html
```

### Quality Standards
- Maintain >90% code coverage
- All new widgets require:
  - Unit tests
  - Functional example
  - Documentation

## 📚 Documentation

### Writing Docs
```python
class ReactiveText(ft.Text, FletXWidget):
    """Text widget with reactive value binding.
    
    Args:
        value: RxStr to bind to text value
        color: RxStr for text color (optional)
    """
```

### Building Documentation
```bash
cd docs/
make html
```

## 🐛 Reporting Bugs

1. Check existing issues for duplicates
2. Include:
   - Steps to reproduce
   - Expected vs actual behavior
   - FletX/Python versions
   - Minimal reproducible example

## 💡 Feature Proposals

1. Clearly describe the use case
2. Suggest technical approach
3. Outline potential impacts
4. Attach mockups if applicable

## 🤝 Code of Conduct

We adhere to the [Contributor Covenant Code of Conduct](CODE_OF_CONDUCT.md). By participating:
- Be kind and open-minded
- Respect differing viewpoints
- Assume good faith

---

Thank you for helping build FletX! Together we're creating the best reactive framework for Flet. 🚀