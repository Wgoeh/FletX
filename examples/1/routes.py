from pages.auth.login import LoginPage
from pages.dashboard.home import DashboardHomePage
from pages.dashboard.settings import DashboardSettingsPage

routes = {
    "/login": LoginPage,
    "/dashboard": DashboardHomePage,
    "/dashboard/settings": DashboardSettingsPage,
}

# DashboardHomePage().build()