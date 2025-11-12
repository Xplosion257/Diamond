# __init__.py
from . import core

# Import the main REPL runner
run = core.run
help = core.help

# Auto-import all commands from core.commands into the package namespace
for name, obj in core.commands.items():
    globals()[name] = obj

# Define __all__ dynamically so IDEs and `from diamond import *` work
__all__ = ["run", "help"] + list(core.commands.keys())

