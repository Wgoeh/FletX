import flet as ft
from fletx import FletX
from fletx.core.page import FletXPage
from fletx.core.router import FletXRouter
from fletx.decorators.controllers import page_controller
from .controller import DashboardController

# @page_controller  # Injection automatique du contrôleur
class DashboardHomePage(FletXPage):
    def __init__(self):
        super().__init__()
        self.controller = FletX.find(DashboardController) or DashboardController()
        
    def build(self):
        # Initialisation sécurisée
        if not hasattr(self, '_built'):  # Protection contre les appels multiples
            self.controller.initialize()
            self._built = True
            
            return ft.Column(
                controls=[
                    ft.Text(self.controller.welcome_message, size=24),
                    ft.ElevatedButton(
                        "Actualiser",
                        on_click=self._safe_refresh  # Méthode sécurisée
                    )
                ],
                expand=True,
                alignment="center"
            )
        return ft.ProgressRing()  # Fallback UI
    
    def _safe_refresh(self, e):
        """Méthode sécurisée sans risque de récursion"""
        if not hasattr(self, '_refreshing'):
            self._refreshing = True
            self.controller.load_data()
            del self._refreshing
    
    def on_logout(self, e):
        self.controller.logout()
        FletXRouter.to("/login", replace=True)
    
    def did_mount(self):
        # Charge les données quand la page est montée
        self.controller.load_data()