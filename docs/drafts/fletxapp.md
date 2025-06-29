# FletXApp Draft

## 🇫🇷 Documentation

### `FletXApp`

#### Description

La classe `FletXApp` est le point d’entrée principal d’une application FletX, offrant une configuration fluide, un support pour les modes synchrone et asynchrone, et des hooks pour le cycle de vie (`on_startup`, `on_shutdown`).

#### Paramètres du constructeur

| Paramètre       | Type                              | Description                                     |
| --------------- | --------------------------------- | ----------------------------------------------- |
| `initial_route` | `str`                             | Route initiale (ex: `/`)                        |
| `theme_mode`    | `ft.ThemeMode`                    | Mode du thème (`SYSTEM`, `LIGHT`, `DARK`)       |
| `debug`         | `bool`                            | Active le mode debug                            |
| `title`         | `str`                             | Titre de l’application                          |
| `theme`         | `Optional[ft.Theme]`              | Thème clair                                     |
| `dark_theme`    | `Optional[ft.Theme]`              | Thème sombre                                    |
| `window_config` | `Optional[Dict]`                  | Configuration de la fenêtre (largeur, hauteur…) |
| `middlewares`   | `...`                             | (Déprécié)                                      |
| `on_startup`    | `Union[Callable, List[Callable]]` | Hooks au démarrage                              |
| `on_shutdown`   | `Union[Callable, List[Callable]]` | Hooks à l’arrêt                                 |
| `**kwargs`      | `dict`                            | Arguments supplémentaires pour `ft.app()`       |

#### Méthodes clés

* `with_title(title: str)`: définit le titre (fluent).
* `with_theme(theme: ft.Theme)`: thème clair (fluent).
* `with_dark_theme(dark_theme: ft.Theme)`: thème sombre (fluent).
* `with_window_size(width: int, height: int)`: configure la fenêtre (fluent).
* `with_debug(debug: bool)`: active/désactive le debug (fluent).
* `add_startup_hook(hook: Callable)`: ajoute un hook au démarrage.
* `add_shutdown_hook(hook: Callable)`: ajoute un hook à la fermeture.
* `run(**kwargs)`, `run_async(**kwargs)`: exécution sync/async.
* `run_web(host, port, **kwargs)`, `run_desktop(**kwargs)`: modes web ou bureau.
* `is_initialized`, `page`: propriétés d’état.
* `get_context_data(key, default)`, `set_context_data(key, value)`: accès au `AppContext`.

#### Cycle de vie

1. Configuration de la fenêtre et du thème.
2. Exécution des hooks `on_startup`.
3. Initialisation du `AppContext` et du `FletXRouter`.
4. Passage en mode `is_initialized = True`.
5. À la fermeture, exécution des hooks `on_shutdown`.

#### Exemples d’utilisation

```python
from fletx.app import FletXApp
import flet as ft

# Exécution simple (mode sync)
app = (FletXApp(title="Ma Super App", initial_route="/home", debug=True)
       .with_window_size(450, 700)
       .with_theme(ft.Theme(color_scheme_seed=ft.Colors.BLUE)))
app.run()
```

```python
# Mode web asynchrone avec hooks
async def on_start(page: ft.Page):
    print("Démarrage")

def on_stop(page: ft.Page):
    print("Arrêt")

app = FletXApp(
    title="App Web",
    debug=False,
    on_startup=on_start,
    on_shutdown=on_stop
)
app.run_web(host="0.0.0.0", port=8080)
```

---

## 🇬🇧 Documentation

### `FletXApp`

#### Description

`FletXApp` is the main entry point for a FletX application. It provides fluent configuration, supports both synchronous and asynchronous execution modes, and lifecycle hooks (`on_startup`, `on_shutdown`).

#### Constructor Parameters

| Parameter       | Type                              | Description                            |
| --------------- | --------------------------------- | -------------------------------------- |
| `initial_route` | `str`                             | Initial route (e.g. `/`)               |
| `theme_mode`    | `ft.ThemeMode`                    | Theme mode (`SYSTEM`, `LIGHT`, `DARK`) |
| `debug`         | `bool`                            | Enable debug mode                      |
| `title`         | `str`                             | App title                              |
| `theme`         | `Optional[ft.Theme]`              | Light theme                            |
| `dark_theme`    | `Optional[ft.Theme]`              | Dark theme                             |
| `window_config` | `Optional[Dict]`                  | Window config (width, height…)         |
| `middlewares`   | `...`                             | (Deprecated)                           |
| `on_startup`    | `Union[Callable, List[Callable]]` | Startup hooks                          |
| `on_shutdown`   | `Union[Callable, List[Callable]]` | Shutdown hooks                         |
| `**kwargs`      | `dict`                            | Additional `ft.app()` params           |

#### Key Methods

* `with_title(title)`: set title (fluent).
* `with_theme(theme)`: set light theme (fluent).
* `with_dark_theme(dark_theme)`: set dark theme (fluent).
* `with_window_size(w,h)`: configure window (fluent).
* `with_debug(debug)`: toggle debug mode (fluent).
* `add_startup_hook(hook)`, `add_shutdown_hook(hook)` to add lifecycle hooks.
* `run()`, `run_async()`: synchronous/asynchronous execution.
* `run_web(host,port)`, `run_desktop()`: run in web or desktop mode.
* `is_initialized`, `page`: status properties.
* `get_context_data(key, default)`, `set_context_data(key, value)`: get/set context data.

#### Lifecycle Overview

1. Setup window and theme.
2. Execute `on_startup` hooks.
3. Initialize `AppContext` and `FletXRouter`.
4. Set `is_initialized` to `True`.
5. On exit, execute `on_shutdown` hooks.

#### Usage Examples

```python
from fletx.app import FletXApp
import flet as ft

# Simple sync run
app = (FletXApp(title="My App", initial_route="/home", debug=True)
       .with_window_size(450, 700)
       .with_theme(ft.Theme(color_scheme_seed=ft.Colors.BLUE)))
app.run()
```

```python
# Async web run with hooks
async def on_start(page: ft.Page):
    print("App started")

def on_stop(page: ft.Page):
    print("App stopped")

app = FletXApp(
    title="Web App",
    debug=False,
    on_startup=on_start,
    on_shutdown=on_stop
)
app.run_web(host="0.0.0.0", port=8080)
```

---

## 🇫🇷 Tests avec `pytest`

```python
# test_fletx_app.py

import pytest
import flet
from fletx.app import FletXApp
from fletx.utils.context import AppContext

@pytest.fixture(autouse=True)
def reset_context():
    AppContext._data.clear()
    yield
    AppContext._data.clear()

def test_sync_run_initializes(tmp_path, monkeypatch):
    calls = []

    def fake_app(target, **kwargs):
        class DummyPage:
            title = ""
            theme = None
            dark_theme = None
            window = type("W", (), {})()
            def update(self): pass
        page = DummyPage()
        target(page)
        calls.append(page)

    monkeypatch.setattr(flet, "app", fake_app)

    app = FletXApp(title="Test", debug=True, initial_route="/foo")
    app.run()

    assert app.is_initialized
    assert isinstance(app.page, object)
    assert AppContext.get_data("app") == app

def test_on_startup_and_shutdown_hooks(monkeypatch):
    calls = []
    async def async_hook(page): calls.append("start-async")
    def sync_hook(page): calls.append("start-sync")
    def shutdown_hook(page): calls.append("stop-sync")

    def fake_app(target, **kwargs):
        class Dummy:
            title = ""
            theme = None
            dark_theme = None
            window = type("W", (), {})()
            def update(self): pass
        page = Dummy()
        target(page)
        return

    monkeypatch.setattr(flet, "app", fake_app)

    app = FletXApp(on_startup=[async_hook, sync_hook], on_shutdown=shutdown_hook)
    app.run()

    assert "start-async" in calls
    assert "start-sync" in calls
    assert "stop-sync" in calls

def test_context_data_set_get():
    app = FletXApp()
    app.set_context_data("foo", 42)
    assert app.get_context_data("foo") == 42
    assert app.get_context_data("bar", "baz") == "baz"
```

---

## 🇬🇧 Tests with `pytest`

```python
# test_fletx_app.py

import pytest
import flet
from fletx.app import FletXApp
from fletx.utils.context import AppContext

@pytest.fixture(autouse=True)
def reset_context():
    AppContext._data.clear()
    yield
    AppContext._data.clear()

def test_sync_run_initializes(tmp_path, monkeypatch):
    calls = []

    def fake_app(target, **kwargs):
        class DummyPage:
            title = ""
            theme = None
            dark_theme = None
            window = type("W", (), {})()
            def update(self): pass
        page = DummyPage()
        target(page)
        calls.append(page)

    monkeypatch.setattr(flet, "app", fake_app)

    app = FletXApp(title="Test", debug=True, initial_route="/foo")
    app.run()

    assert app.is_initialized
    assert isinstance(app.page, object)
    assert AppContext.get_data("app") == app

def test_on_startup_and_shutdown_hooks(monkeypatch):
    calls = []
    async def async_hook(page): calls.append("start-async")
    def sync_hook(page): calls.append("start-sync")
    def shutdown_hook(page): calls.append("stop-sync")

    def fake_app(target, **kwargs):
        class Dummy:
            title = ""
            theme = None
            dark_theme = None
            window = type("W", (), {})()
            def update(self): pass
        page = Dummy()
        target(page)
        return

    monkeypatch.setattr(flet, "app", fake_app)

    app = FletXApp(on_startup=[async_hook, sync_hook], on_shutdown=shutdown_hook)
    app.run()

    assert "start-async" in calls
    assert "start-sync" in calls
    assert "stop-sync" in calls

def test_context_data_set_get():
    app = FletXApp()
    app.set_context_data("foo", 42)
    assert app.get_context_data("foo") == 42
    assert app.get_context_data("bar", "baz") == "baz"
```

---

💡 **À noter :** les tests simulent `flet.app()` pour forcer l’exécution de `target(page)`. Les hooks asynchrones sont correctement pris en charge. Si tu veux aller plus loin, je peux ajouter des tests pour `run_async`, `run_web`, `run_desktop`, etc. veux-tu que je m’en occupe ?





```python
"""
Exemples d'utilisation de la nouvelle FletXApp
"""

import flet as ft
from fletx.app import FletXApp

# ==============================
# EXEMPLE 1: Configuration Simple
# ==============================

def example_simple():
    """Exemple basique avec configuration simple"""
    
    app = FletXApp(
        title="Mon App FletX",
        initial_route="/",
        debug=True
    ).with_window_size(400, 600).with_theme(
        ft.Theme(color_scheme_seed=ft.Colors.BLUE)
    )
    
    # Run sync
    app.run()

# ==============================
# EXEMPLE 2: Configuration Avancée
# ==============================

def example_advanced():
    """Exemple avec configuration avancée"""
    
    # Hooks de démarrage et arrêt
    async def on_startup(page: ft.Page):
        print("App démarrée!")
        # Initialiser des services, base de données, etc.
    
    def on_shutdown(page: ft.Page):
        print("App fermée!")
        # Nettoyer les ressources
    
    # Middleware
    def auth_middleware(page: ft.Page):
        print("Vérification d'authentification...")
    
    app = FletXApp(
        title="App Avancée",
        initial_route="/dashboard",
        debug=True,
        theme=ft.Theme(color_scheme_seed=ft.Colors.GREEN),
        dark_theme=ft.Theme(
            color_scheme_seed=ft.Colors.BLUE_800,
            scaffold_bgcolor=ft.Colors.BLACK
        ),
        window_config={
            "width": 800,
            "height": 600,
            "resizable": True,
            "maximizable": True
        },
        middlewares=[auth_middleware],
        on_startup=on_startup,
        on_shutdown=on_shutdown
    )
    
    # Run async
    app.run_async()

# ==============================
# EXEMPLE 3: Style Fluent Interface
# ==============================

def example_fluent():
    """Exemple avec interface fluide"""
    
    def logging_middleware(page: ft.Page):
        print(f"Page: {page.title} - Route: {page.route}")
    
    async def setup_database(page: ft.Page):
        print("Configuration de la base de données...")
        # Simulation d'une tâche async
        import asyncio
        await asyncio.sleep(0.1)
    
    app = (FletXApp()
           .with_title("Interface Fluide")
           .with_window_size(1000, 700)
           .with_theme(ft.Theme(color_scheme_seed=ft.Colors.PURPLE))
           .with_debug(True)
           .add_middleware(logging_middleware)
           .add_startup_hook(setup_database))
    
    app.run_web(port=8080)

# ==============================
# EXEMPLE 4: Mode Web avec Hooks Multiples
# ==============================

def example_web_app():
    """Exemple d'application web avec hooks multiples"""
    
    async def init_services(page: ft.Page):
        print("Initialisation des services...")
    
    async def load_config(page: ft.Page):
        print("Chargement de la configuration...")
    
    def cleanup_temp_files(page: ft.Page):
        print("Nettoyage des fichiers temporaires...")
    
    app = FletXApp(
        title="Web App FletX",
        theme_mode=ft.ThemeMode.LIGHT,
        on_startup=[init_services, load_config],
        on_shutdown=cleanup_temp_files
    )
    
    app.run_web(host="0.0.0.0", port=3000)

# ==============================
# EXEMPLE 5: Usage avec ft.app (style classique amélioré)
# ==============================

def example_classic_style():
    """Exemple avec style classique mais amélioré"""
    
    app = FletXApp(
        title="Style Classique",
        initial_route="/home",
        debug=True,
        window_config={"width": 500, "height": 400}
    )
    
    def main(page: ft.Page):
        # Configuration personnalisée de la page si nécessaire
        page.bgcolor = ft.Colors.BLUE_50
        
        # Utiliser le handler de l'app
        app._sync_main(page)
    
    ft.app(target=main)

# ==============================
# EXEMPLE 6: Application Async Complète
# ==============================

def example_async_complete():
    """Exemple d'application complètement asynchrone"""
    
    async def async_main():
        app = FletXApp(title="App Async")
        
        async def main_handler(page: ft.Page):
            await app._async_main(page)
            
            # Logique async personnalisée après initialisation
            print("Application initialisée, démarrage des tâches de fond...")
        
        # Utiliser le handler async
        ft.app(target=lambda page: asyncio.run(main_handler(page)))
    
    import asyncio
    asyncio.run(async_main())

# ==============================
# EXEMPLE 7: Configuration Dynamique
# ==============================

def example_dynamic_config():
    """Exemple avec configuration dynamique"""
    
    # Configuration basée sur l'environnement
    import os
    is_production = os.getenv("ENV") == "production"
    
    app = FletXApp(
        debug=not is_production,
        theme_mode=ft.ThemeMode.DARK if is_production else ft.ThemeMode.LIGHT,
        window_config={
            "width": 1200 if is_production else 800,
            "height": 800 if is_production else 600
        }
    )
    
    # Configuration conditionnelle
    if not is_production:
        app.add_middleware(lambda page: print(f"DEBUG: Route = {page.route}"))
    
    app.run_desktop()

if __name__ == "__main__":
    # Lancer un des exemples
    example_fluent()
```