from flet import *
from ..shared.components import ReactivePasswordField, ReactiveTextFieldProps
from fletx import FletX
from fletx.core.page import FletXPage
from fletx.core.router import FletXRouter
from fletx.core.state import RxBool
from fletx.decorators.reactive import computed
from .controller import AuthController
from .guards import AuthGuard

class LoginPage(FletXPage):
    default_radius = 30
    hide_password: RxBool = RxBool(True)


    def build(self):
        # Récupère le contrôleur
        self.controller = FletX.find(AuthController) or AuthController()
        FletX.put(self.controller)
        
        # Email or phone number field
        self.email_field = TextField(
            label = "email or phone number",
            height = 55,
            fill_color = Colors.GREY_900,
            bgcolor = Colors.with_opacity(
                color = Colors.GREY_900,
                opacity = .6
            ),
            content_padding = padding.symmetric(horizontal = 30),
            border_radius = self.default_radius,
            border = InputBorder.NONE,
            adaptive = True,
            filled = True,
            value = '',
            text_style = TextStyle(
                size = 14,
                weight = FontWeight.W_400
            ),
            label_style = TextStyle(
                size = 14,
                weight = FontWeight.W_400,
                color = Colors.GREY_500
            ),
            prefix = Container(
                margin = margin.only(left = 20),
            ),
            suffix = Container(
                margin = margin.only(right = 20),
            ),
        )

        # Passaord Field
        self.password_field = ReactivePasswordField(
            label = "Password", 
            hint_text = "Enter your password",
            height = 55,
            fill_color = Colors.GREY_900,
            bgcolor = Colors.with_opacity(
                color = Colors.GREY_900,
                opacity = .6
            ),
            content_padding = padding.symmetric(horizontal = 30),
            suffix = Container(
                on_click = lambda e: self.hide_password.toggle(),
                margin = margin.only(right = 20),
                # Content
                content = Icon(
                    Icons.PASSWORD_OUTLINED,
                    color = Colors.GREY_500,
                    size = 20
                )
            ),
            prefix = Container(
                margin = margin.only(left = 20),
            ),
            border_radius = self.default_radius,
            border = InputBorder.NONE,
            adaptive = True,
            filled = True,
            password = True,
            value = '',
            text_style = TextStyle(
                size = 14,
                weight = FontWeight.W_400
            ),
            label_style = TextStyle(
                size = 14,
                weight = FontWeight.W_400,
                color = Colors.GREY_500
            ),
            is_password = self.hide_password
        )
        
        return SafeArea(
            expand = True,
            content = Container(
                expand = True,
                padding = padding.symmetric(horizontal = 12),

                # Content
                content = Column(
                    expand = True,
                    alignment = MainAxisAlignment.SPACE_BETWEEN,
                    horizontal_alignment = CrossAxisAlignment.CENTER,
                    controls = [
                        Column(
                            expand = True,
                            # width = 350,
                            spacing = 20,
                            alignment = MainAxisAlignment.START,
                            horizontal_alignment = CrossAxisAlignment.CENTER,
                            
                            controls = [
                                Container(
                                    height = 35,
                                ),
                                Column(
                                    spacing = 5,
                                    alignment = MainAxisAlignment.CENTER,
                                    horizontal_alignment = CrossAxisAlignment.CENTER,
                                    controls = [
                                        Image(
                                            src = 'logos'
                                            '/ln_grad.svg',
                                            fit = ImageFit.CONTAIN,
                                            width = 90,
                                            height = 90
                                        ),
                                        # SPACER
                                        Container(
                                            height = 10
                                        ),
                                        # Welcome Text
                                        Text(
                                            value = "Welcome Back To Learnia", 
                                            style = TextStyle(
                                                size = 22,
                                                weight = FontWeight.W_600
                                            )
                                        ),
                                        Text(
                                            value = "Welcome Back To Learnia", 
                                            style = TextStyle(
                                                size = 14,
                                                weight = FontWeight.W_400
                                            )
                                        ),
                                    ]
                                ),

                                Container(
                                    height = 0
                                ),

                                # Email or phone number field
                                self.email_field,

                                # Password Field
                                self.password_field,

                                # BUTTON
                                GestureDetector(
                                    on_tap = self.on_login,
                                    mouse_cursor = MouseCursor.CLICK,
                                    # Content
                                    content = Container(
                                        # width = self.width,
                                        height = 55,
                                        border_radius = self.default_radius,
                                        bgcolor = Colors.BLUE_800,

                                        content = Row(
                                            alignment = MainAxisAlignment.CENTER,
                                            vertical_alignment = CrossAxisAlignment.CENTER,
                                            controls = [
                                                Text(
                                                    'Login',
                                                    text_align = TextAlign.CENTER,
                                                    style = TextStyle(
                                                        size = 16,
                                                        weight = FontWeight.W_600,
                                                        color = Colors.WHITE
                                                    )
                                                ),
                                            ],
                                        )
                                    ),
                                ),

                                # SEPARATOR
                                Row(
                                    expand = False,
                                    alignment = MainAxisAlignment.CENTER,

                                    # Contents
                                    controls = [
                                        Container(
                                            width = 100,
                                            height = 1,
                                            bgcolor = Colors.GREY_800
                                        ),
                                        Text(
                                            value = "or continue with",
                                            style = TextStyle(
                                                size = 12,
                                                weight = FontWeight.W_400,
                                                color = Colors.GREY_500
                                            ),
                                            text_align = TextAlign.CENTER
                                        ),
                                        Container(
                                            width = 100,
                                            height = 1,
                                            bgcolor = Colors.GREY_800
                                        )
                                    ]
                                ),
                                # TextButton(
                                #     "Accéder sans compte (demo)",
                                #     on_click=lambda e: FletXRouter.to("/dashboard")
                                # ),

                                # Spacer
                                Container(
                                    height = 15
                                ),

                                # Social auth buttons
                                Container(
                                    expand = False,
                                    padding = padding.all(8),
                                    width = 200,
                                    border_radius = self.default_radius,
                                    bgcolor = Colors.with_opacity(
                                        color = Colors.GREY_900,
                                        opacity = .6
                                    ),

                                    # Content
                                    content = Row(
                                        alignment = MainAxisAlignment.SPACE_EVENLY,
                                        vertical_alignment = CrossAxisAlignment.CENTER,
                                        controls = [
                                            # Google Button
                                            Container(
                                                height = 45,
                                                width = 45,
                                                bgcolor = Colors.BLACK,
                                                border_radius = self.default_radius,
                                                padding = padding.all(10),

                                                content = Image(
                                                    src = 'icons/google.svg',
                                                    fit = ImageFit.COVER,
                                                    # width = 10,
                                                    # height = 10
                                                )
                                            ),

                                            # Facebook Button
                                            Container(
                                                height = 45,
                                                width = 45,
                                                bgcolor = Colors.BLACK,
                                                border_radius = self.default_radius,
                                                padding = padding.all(10),

                                                content = Image(
                                                    src = 'icons/apple.svg',
                                                    fit = ImageFit.COVER,
                                                    # width = 10,
                                                    # height = 10
                                                )
                                            ),

                                            # Apple Button
                                            Container(
                                                height = 45,
                                                width = 45,
                                                bgcolor = Colors.BLACK,
                                                border_radius = self.default_radius,
                                                padding = padding.all(10),

                                                content = Image(
                                                    src = 'icons/facebook.svg',
                                                    fit = ImageFit.COVER,
                                                    # width = 10,
                                                    # height = 10
                                                )
                                            )
                                        ]
                                    )
                                ),                            
                            ],
                        ),

                        # Terms and Conditions text
                        Text(
                            value = "By continuing, you agree to our Terms of Service and Privacy Policy.",
                            style = TextStyle(
                                size = 12,
                                weight = FontWeight.W_400,
                                color = Colors.GREY_500
                            ),
                            text_align = TextAlign.CENTER
                        )
                    ],
                )
            )
        )
    def on_login(self, e):
        # Validation basique
        if not self.email_field.value or not self.password_field.value:
            return
        
        # Appel au contrôleur
        self.controller.login(
            self.email_field.value,
            self.password_field.value,
            on_success=lambda: FletXRouter.to("/dashboard"),
            on_failure=lambda: print("Échec de connexion")
        )