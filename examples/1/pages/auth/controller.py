from fletx.core.controller import FletXController
from fletx.core.state import RxStr, RxBool
from models.user import User

class AuthController(FletXController):
    def __init__(self):
        super().__init__()
        self.current_user = RxStr("")
        self.is_authenticated = RxBool(False)
    
    def login(self, email: str, password: str, on_success: callable, on_failure: callable):
        # Simulation d'authentification
        if email == "a" and password == "a":
            self.current_user.value = email
            self.is_authenticated.value = True
            on_success()
        else:
            on_failure()
    
    def logout(self):
        self.current_user.value = ""
        self.is_authenticated.value = False