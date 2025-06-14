from flet import *
from fletx.app import FletXApp
from fletx.decorators import (
    reactive_form, simple_reactive,
    two_way_reactive
)
from fletx.core import (
    RxBool, RxStr, FletXPage,
    FormFieldValidationRule, RxDict
)
from fletx.navigation import router_config

####
##      TWO WAY REACTIVE TEXT FIELD
####
@two_way_reactive({
    'value': 'rx_value',
    'visible': 'rx_visible',
    'disabled': 'rx_disabled'
})
class ReactiveTextField(TextField):
    """Example of two way Reactive TextField"""
    
    def __init__(
        self, 
        rx_value: RxStr = RxStr(""), 
        rx_visible: RxBool = RxBool(True),
        rx_disabled: RxBool = RxBool(False),
        **kwargs
    ):
        # Définir les propriétés réactives
        self.rx_value = rx_value
        self.rx_visible = rx_visible
        self.rx_disabled = rx_disabled
        
        super().__init__(**kwargs)


####
##      REACTIVE FORM
####
@reactive_form(
    form_fields={
        'username': 'rx_username',
        'email': 'rx_email',
        'password': 'rx_password',
        'confirm_password': 'rx_confirm_password'
    },
    validation_rules={
        'username': lambda x: len(x) >= 3 and x.isalnum(),
        'email': [
            FormFieldValidationRule(
                validate_fn = 'email_regex',
                err_message = 'Email does not match the wanted pattern'
            ),
            FormFieldValidationRule(
                validate_fn = lambda value: 10 < len(value) < 50,
                err_message = 'Email must contain at least 10 characters and 50 maximum'
            ),
            FormFieldValidationRule(
                validate_fn = lambda value: str(value).endswith('@alldotpy.com'),
                err_message = 'Only Alldotpy domain emails are accepted.'
            )
        ],
        'password': 'validate_pass',
        # 'confirm_password': lambda x: x == self.rx_password.value
    },
    on_submit = 'perform_submit',  # lambda form: print(f"Submitted Form: {form.get_values()}"),
    on_submit_failed = 'show_erros',
    auto_validate = True
)
class RegistrationForm(Column):
    """Example of Reactive Form"""
    
    def __init__(self):
        # Reactive Properties
        self.rx_username = RxStr("")
        self.rx_email = RxStr("")
        self.rx_password = RxStr("")
        self.rx_confirm_password = RxStr("")
        self.rx_is_valid = RxBool(False)
        self.form_errors = RxDict({})
        
        super().__init__(spacing=10)
        
        self.error_display = Markdown(
            '',
            selectable = True,
            expand = True,
            visible = False,
            extension_set = MarkdownExtensionSet.GITHUB_WEB,
            code_theme = MarkdownCodeTheme.DARCULA
            # on_tap_link=lambda e: page.launch_url(e.data),
        )
        # Now build the form
        self._build_form()
        

    def validate_pass(self,value:str):
        """Example of password validation function"""
        return len(value) >= 8
    
    def email_regex(self,value):
        """example of email validation function"""
        import re
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return re.match(pattern, value) is not None
    
    def perform_submit(self,form):
        """Perform submit action"""

        if form.is_valid:
            print(form.get_values())
        else:
            print(form.get_errors())

    def show_erros(self,errors):

        import json
        self.error_display.visible = True
        self.error_display.value = f"""```\n {json.dumps(errors,indent=4)}\n```"""
        self.update()
    
    def _build_form(self):
        """Build form Controls."""
        
        self.controls = [
            Text("Register Form", size = 24, weight = FontWeight.BOLD),
            
            ReactiveTextField(
                label = "Your username goes here",
                rx_value = self.rx_username
            ),
            
            ReactiveTextField(
                label = "Your email goes here",
                rx_value = self.rx_email
            ),
            
            ReactiveTextField(
                label = "Choose a password",
                password = True,
                rx_value = self.rx_password
            ),
            
            ReactiveTextField(
                label = "Confirm the password",
                password = True,
                rx_value = self.rx_confirm_password
            ),
            
            ElevatedButton(
                text = "Register for free",
                on_click = lambda _: self.submit(),
                disabled = lambda: not self.rx_is_valid.value
            ),

            self.error_display
        ]


class RegistrationPage(FletXPage):

    def build(self):
        return Column(
            controls = [
                RegistrationForm()
            ]
        )


def main(page: Page):
    page.title = "Reactive Forms Example"
    page.theme_mode = ThemeMode.LIGHT
    page.add(RegistrationPage().build())             # Add the CounterPage to the FletX page

    # Defining route
    router_config.add_route(
        **{
            'path': '/',
            'component': RegistrationPage
        }
    )
    app = FletXApp()
    app._main(page)                             # Initialize the FletX application with the page

if __name__ == "__main__":
    app(target=main)