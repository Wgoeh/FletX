from fletx.core.controller import FletXController
from fletx.core.state import RxStr, RxList
from fletx.decorators.reactive import computed
from fletx.core.effects import useEffect
from models.user import User

class DashboardController(FletXController):
    def __init__(self):
        super().__init__()
        self.username = RxStr("Invité")
        self.todos = RxList([])
        self._is_initialized = False
        
        # Effet auto-nettoyant
        self.add_effect(
            lambda: print("DashboardController prêt"),
            []
        )
    
    # @property
    @computed
    def todo_count(self) -> int:
        return len(self.todos.value)
    
    # @property
    @computed
    def welcome_message(self) -> str:
        return f"Bienvenue, {self.username.value}"
    
    def initialize(self):
        """Méthode séparée pour l'initialisation"""
        if not self._is_initialized:
            self.load_data()
            self._is_initialized = True
    
    def load_data(self):
        # Simulation chargement async
        import asyncio
        async def load():
            await asyncio.sleep(1)
            self.username.value = "Admin"
            self.todos.value = ["Tâche 1", "Tâche 2"]
        
        asyncio.run(load())
    
    def logout(self):
        from fletx import FletX
        auth = FletX.find('AuthController')
        if auth:
            auth.logout()