from command import Command 
import Commands
import importlib
import inspect
import pkgutil
from collections import namedtuple

def build_command_map():
    '''
        In order to decouple the commands from the rest of the codebase, 
        this util dynamically imports the commands classes from the Commands package.
        This allows us to build and store a map from command to functionality 
    '''
    for (module_loader, name, ispkg) in pkgutil.iter_modules(['Commands/']):
        importlib.import_module('Commands.' + name,package=Commands)

    command_classes = [cls() for cls in Command.__subclasses__()]

    cmd_map = {}
    [
        [
            cmd_map.update({keyword: cl.get_response}) 
            for keyword in cl.get_keywords()
        ] for cl in command_classes
    ]

    cmd_list = [
        '[{cmds}] : {definition}'.format(
            cmds=', '.join([cmd for cmd in cl.get_keywords()]),
            definition=cl.get_description()
        ) for cl in command_classes
    ]

    return cmd_map, cmd_list