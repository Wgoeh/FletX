import asyncio
import flet as ft
from fletx.app import FletXApp
from routes import MyAppRouter

def main():#(page: ft.Page):
    # Configuration de la page
    # page.title = "Mon App FletX"

    # # Setting up theme
    # page.theme = ft.Theme(
    #     color_scheme_seed = ft.Colors.GREEN
    # )
    # page.dark_theme = ft.Theme(
    #     color_scheme_seed = ft.Colors.BLUE_800,
    #     scaffold_bgcolor = ft.Colors.BLACK,
    #     font_family = 'Bebas Neue, sans-serif',
    # )
    # page.theme_mode = ft.ThemeMode.DARK

    # # Setting up window size
    # page.window.height = 810
    # page.window.width = 400
    
    # Initialisation de l'application FletX
    app = FletXApp(
        initial_route = "/login",
        debug = True,
        theme_mode = ft.ThemeMode.DARK,
        theme = ft.Theme(
            color_scheme_seed = ft.Colors.GREEN
        ),
        dark_theme = ft.Theme(
            color_scheme_seed = ft.Colors.BLUE_800,
            scaffold_bgcolor = ft.Colors.BLACK,
            font_family = 'Bebas Neue, sans-serif',
        )
    ).with_window_size(400,810)
    
    # Cette méthode initialise le router avec la page Flet
    # app._main(page) 

    app.run_async()

if __name__ == "__main__":
    main()
    # ft.app(target=main)