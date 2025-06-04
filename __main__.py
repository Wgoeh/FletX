# -*- coding: utf-8 -*-

""" MAIN ENTRY POINT FOR FLETX CLI
This module serves as the main entry point for the Breeze CLI. It handles command-line
arguments, initializes the command registry, and executes the specified command.
"""

import sys
from fletx.cli.commands.base import CommandRegistry

def main():
    """ 
    Main function to handle command-line arguments and execute commands.
    This function checks if any command is provided, retrieves the command class
    from the command registry, and executes the command with the provided arguments.
    If no command is provided, it lists all available commands.
    """
    
    argv = sys.argv[1:]
    if not argv:
        print("No command provided.")
        print("Available commands:")
        for command_cls in CommandRegistry.all():
            print(f"  {command_cls.command_name} - {command_cls().get_description()}")
        return

    command_name, *command_args = argv

    try:
        command_cls = CommandRegistry.get(command_name)
        command_instance = command_cls()
        command_instance.run_from_argv(command_args)
    except ValueError as e:
        print(str(e))

if __name__ == "__main__":
    main()
