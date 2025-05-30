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
    can_show_password = RxBool(False)


    def build(self):
        # Récupère le contrôleur
        self.controller = FletX.find(AuthController) or AuthController()
        FletX.put(self.controller)
        
        # Éléments UI
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
            )
        )
        self.password_field = ReactivePasswordField(
            reactives = ReactivePasswordField(
                can_reveal_password = self.can_show_password,
                # value = '',
                # label = 'Password',
                # hint_text = 'Enter your password',
                password = self.can_show_password
            ),
            label = "Password", 
            height = 55,
            fill_color = Colors.GREY_900,
            bgcolor = Colors.with_opacity(
                color = Colors.GREY_900,
                opacity = .6
            ),
            content_padding = padding.symmetric(horizontal = 30),
            suffix = Container(
                on_click = lambda e: self.can_show_password.toggle(),
                # Content
                content = Icon(
                    Icons.PASSWORD_OUTLINED,
                    color = Colors.GREY_500,
                    size = 20
                )
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
            )
        )
        
        return Container(
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
                        alignment = MainAxisAlignment.CENTER,
                        horizontal_alignment = CrossAxisAlignment.CENTER,
                        
                        controls = [
                            # Container(
                            #     height = 10
                            # ),
                            Column(
                                spacing = 5,
                                alignment = MainAxisAlignment.CENTER,
                                horizontal_alignment = CrossAxisAlignment.CENTER,
                                controls = [
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
                                height = 10
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
                                    bgcolor = Colors.TEAL,

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

                            TextButton(
                                "Accéder sans compte (demo)",
                                on_click=lambda e: FletXRouter.to("/dashboard")
                            ),

                            # Social auth buttons
                            Container(
                                expand = False,
                                padding = padding.all(8),
                                border_radius = 15,
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
                                            border_radius = 8
                                        ),

                                        # Facebook Button
                                        Container(
                                            height = 45,
                                            width = 45,
                                            bgcolor = Colors.BLACK,
                                            border_radius = 8
                                        ),

                                        # Apple Button
                                        Container(
                                            height = 45,
                                            width = 45,
                                            bgcolor = Colors.BLACK,
                                            border_radius = 8
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