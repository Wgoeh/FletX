from fletx.app import FletXApp
import flet as ft
from home import HomePage

def main(page: ft.Page):
    # Configuration de la page
    page.title = "Mon App FletX"

    # Setting up theme
    page.theme = ft.Theme(
        color_scheme_seed = ft.Colors.GREEN
    )
    page.dark_theme = ft.Theme(
        color_scheme_seed = ft.Colors.AMBER_700,
        scaffold_bgcolor = '#090909',
        font_family = 'Bebas Neue, sans-serif',
    )
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = ft.padding.all(0)

    # Setting up window size
    page.window.height = 800
    page.window.width = 1200
    
    # Initialisation de l'application FletX
    app = FletXApp(
        routes = {"/": HomePage},
        debug = True
    )
    
    # Cette méthode initialise le router avec la page Flet
    app._main(page) 

if __name__ == "__main__":
    ft.app(target=main)