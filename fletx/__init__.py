"""
FletX - Mini framework inspiré de GetX pour Flet
"""

from fletx.core.di import DI


__version__ = "0.1.0"

# Alias pour faciliter l'utilisation
class FletX:
    """Interface principale pour l'injection de dépendances"""
    
    @staticmethod
    def put(instance, tag=None):
        """Enregistre une instance dans le DI container"""
        return DI.put(instance, tag)
    
    @staticmethod
    def find(cls, tag=None):
        """Récupère une instance du DI container"""
        return DI.find(cls, tag)
    
    @staticmethod
    def delete(cls, tag=None):
        """Supprime une instance du DI container"""
        return DI.delete(cls, tag)
    
    @staticmethod
    def reset():
        """Remet à zéro le DI container"""
        return DI.reset()

__all__ = [
    'FletX',
]