import flet as ft
from fletx.core.page import FletXPage
from fletx.decorators.controllers import page_controller
from fletx.core.router import FletXRouter
from .controller import DashboardController

@page_controller
class DashboardSettingsPage(FletXPage):
    def build(self):
        return ft.Column(
            controls=[
                ft.Text("Paramètres", size=24, weight="bold"),
                ft.Switch(
                    label="Mode sombre",
                    value=self.controller.dark_mode.value,
                    on_change=self.toggle_theme
                ),
                ft.Text(f"Nombre de tâches: {self.controller.todo_count}"),
                ft.ElevatedButton(
                    "Retour",
                    on_click=lambda e: FletXRouter.back()
                )
            ],
            spacing=20,
            expand=True,
            alignment="center"
        )
    
    def toggle_theme(self, e):
        self.controller.dark_mode.value = e.control.value
        # Ici vous pourriez aussi mettre à jour le thème Flet