from fletx.navigation import (
    ModuleRouter, TransitionType, RouteTransition
)
from fletx.decorators import register_router

from pages.auth.login import LoginPage
from pages.dashboard.home import DashboardHomePage
from pages.dashboard.settings import DashboardSettingsPage


routes = [
    {
        'path': '/login',
        'component': LoginPage,
        'meta':{
            'transition': RouteTransition(
                transition_type = TransitionType.FADE,
                duration = 350
            )
        }
    },
    {
        'path': '/dashboard',
        'component': DashboardHomePage,
        'meta':{
            'transition': RouteTransition(
                transition_type = TransitionType.SLIDE_LEFT,
                duration = 350
            )
        }
    },
    {
        'path': '/dashboard/settings',
        'component': DashboardSettingsPage
    }
]

@register_router
class MyAppRouter(ModuleRouter):
    """My Application Routing Module."""

    name = 'MyAppRouter'
    base_path = '/'
    is_root = True
    routes = routes
    sub_routers = []




# MyAppRouter.add_routes(routes = routes)

# {
#     "/login": LoginPage,
#     "/dashboard": DashboardHomePage,
#     "/dashboard/settings": DashboardSettingsPage,
# }

# DashboardHomePage().build()