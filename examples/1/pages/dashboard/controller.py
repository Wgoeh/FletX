from fletx.core import (
    FletXController,RxStr, RxList
)
from fletx.core.concurency import Priority
from fletx.decorators import worker_task
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
        @worker_task(priority = Priority.CRITICAL)
        def load():
            asyncio.sleep(1)
            self.username.value = "Admin"
            self.todos.value = [
                {
                    'task_id': '1',
                    'task_name': 'Ajouter @fletx.widgets.reactive_control',
                },
                {
                    'task_id': '2',
                    'task_name': 'Créer un exemple de Projet avec FletX',
                },
                {
                    'task_id': '3',
                    'task_name': 'Écrire la documentation',
                },
                {
                    'task_id': '4',
                    'task_name': 'Tester l\'application',
                },
                {
                    'task_id': '5',
                    'task_name': 'Déployer sur GitHub',
                },
                {
                    'task_id': '6',
                    'task_name': 'Faire une vidéo de présentation',
                },
                {
                    'task_id': '7',
                    'task_name': 'Partager sur les réseaux sociaux',
                },
                {
                    'task_id': '8',
                    'task_name': 'Répondre aux questions des utilisateurs',
                },
                {
                    'task_id': '9',
                    'task_name': 'Préparer la prochaine version',
                },
                {
                    'task_id': '10',
                    'task_name': 'Organiser une session de feedback',
                }
            ]
        
        load.run_and_wait()
    
    def logout(self):
        from fletx import FletX
        auth = FletX.find('AuthController')
        if auth:
            auth.logout()