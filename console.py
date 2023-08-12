#!/usr/bin/python3
"""
Defines HBNB console
"""
import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

class HBNBCommand(cmd.Cmd):
    """
    Defines the HBNB command interpreter.
    Attributes: prompt (str): The command prompt.
    """

     prompt = "(hbnb) "
    __classes = {
            "BaseModel",
            "User",
            "City",
            "State",
            "Place",
            "Amenity",
            "Review"
            }
def emptyline(self):
"""
Execute nothing on empty line
"""
pass

def default(self, arg):
    """
    Behaviour of cmd when input is invalid
    """
    argdict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
            }
match = re.search(r"\.", arg)
        if match is not None:
            argl = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", argl[1])
        if match is not None:
            command = [argl[1][:match.span()[0]], match.group()[1:-1]]
         if command[0] in argdict.keys():
                 call = "{} {}".format(argl[0], command[1])
                 return argdict[command[0]](call)
             print("*** Unknown syntax: {}".format(arg))
             return False

         def do_quit(self, arg):
             """
             Quit: command to exit the program.
             """
             return True
         def do_EOF(self, arg):
             """
             EOF: signal to exit the program.
             """
             print("")
             return True

         if __name__ == "__main__":
    HBNBCommand().cmdloop()

