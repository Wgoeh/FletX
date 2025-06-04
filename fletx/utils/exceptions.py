"""
FletX Exceptions 
"""

####
##      BASE EXCEPTION CLASS
#####
class FletXError(Exception):
    """Base exception for FletX"""

    pass


####
##      ROUTE NOT FOUND EXCEPTION CLASS
#####
class RouteNotFoundError(FletXError):
    """Exception raised when a route is not found"""

    pass


####
##      NAVIGATION EXCEPTION CLASS
#####
class NavigationError(FletXError):
    """Exception raised on navigation errors"""

    pass


####
##      NAVIGATION ABORTED EXCEPTION CLASS
#####
class NavigationAborted(FletXError):
    """Exception raised when navigation is cancelled"""

    pass


####
##      DEPENDENCY NOT FOUND EXCEPTION CLASS
#####
class DependencyNotFoundError(FletXError):
    """Exception raised when a dependency is not found"""

    pass


####
##      CONTROLLER EXCEPTION CLASS
#####
class ControllerError(FletXError):
    """Exception related to controllers"""

    pass


####
##      STATE EXCEPTION CLASS
#####
class StateError(FletXError):
    """Exception related to state management"""

    pass


####
##      BASE CLI EXCEPTION CLASS
#####
class FletXCLIError(FletXError):
    """Base class for all errors related to the Breeze CLI."""

    pass


####
##      COMMAND EXCEPTION CLASS
#####
class CommandError(FletXError):
    """
    Exception class indicating a problem while executing a command.
    """

    def __init__(self, *args, returncode=1, **kwargs):
        self.returncode = returncode
        super().__init__(*args, **kwargs)


####
##      COMMAND NOT FOUND EXCEPTION CLASS
#####
class CommandNotFoundError(CommandError):
    """Exception levée quand une commande n'est pas trouvée."""

    pass
        

####
##      COMMAND EXECUTION ERROR CLASS
#####
class CommandExecutionError(CommandError):
    """Exception levée lors d'une erreur d'exécution de commande."""
    
    pass
