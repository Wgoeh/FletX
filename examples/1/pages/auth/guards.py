from fletx.core.routing.guards import RouteGuard
from fletx.core.routing.models import RouteInfo


class AuthGuard(RouteGuard):
    """Exemple de guard d'authentification"""
    
    def can_activate(self, route: RouteInfo) -> bool:
        from ... import find
        auth_service = find('AuthService')
        return auth_service.is_authenticated() if auth_service else False
    
    def redirect(self, route: RouteInfo) -> str:
        return "/login"

class RoleGuard(RouteGuard):
    """Vérification des rôles"""
    
    def __init__(self, required_roles: list):
        self.required_roles = required_roles
    
    def can_activate(self, route: RouteInfo) -> bool:
        from ... import find
        user_service = find('UserService')
        if not user_service:
            return False
        return any(role in user_service.roles for role in self.required_roles)
    
    def redirect(self, route: RouteInfo) -> str:
        return "/unauthorized"