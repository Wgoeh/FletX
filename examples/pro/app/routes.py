"""
pro Application routing module.
Version: 0.1.0
"""


# Import your pages here
from fletx.navigation import (
    ModuleRouter, TransitionType, RouteTransition
)
from fletx.decorators import register_router

from .pages.counter import CounterPage

# Define Pro routes here
routes = [
    {
        'path': '/',
        'component': CounterPage,
    },
]

@register_router
class ProRouter(ModuleRouter):
    """pro Routing Module."""

    name = 'pro'
    base_path = '/'
    is_root = True
    routes = routes
    sub_routers = []