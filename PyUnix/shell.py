import sys
import os
import socket
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from PyUnix.commands import *

DEBUG = True
exitFlag = False

lookup = {"alias": alias.alias, "apropos": apropos.apropos, "cat": cat.cat, "cd": cd.cd, "exit": exit.pyexit, "ls": ls.ls}

welcomeMessage = """
 __          __  _                            _          _____       _    _       _      
 \ \        / / | |                          | |        |  __ \     | |  | |     (_)     
  \ \  /\  / /__| | ___ ___  _ __ ___   ___  | |_ ___   | |__) |   _| |  | |_ __  ___  __
   \ \/  \/ / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \  |  ___/ | | | |  | | '_ \| \ \/ /
    \  /\  /  __/ | (_| (_) | | | | | |  __/ | || (_) | | |   | |_| | |__| | | | | |>  < 
     \/  \/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/  |_|    \__, |\____/|_| |_|_/_/\_\ 
                                                                __/ |                    
                                                               |___/                     
"""

def excecute(command):
    return lookup[command[0]](lookup, *command[1::])


def parse(string):
    """
    Parse the user's input and return as a list of command tupples (function, *arg, **kwargs)
    :param string: the users input
    :return follows the form [(function, lookupKey, *args), (function, ...), ...]
    """
    return [tuple(string.split())]


def repl():
    print(welcomeMessage)
    while not exitFlag:
        userString = input("[" + os.getlogin() + "@" + socket.gethostname() +
                           " " + os.path.basename(os.getcwd()) + "]~$ ")
        for command in parse(userString):
            try:
                out = excecute(command)
                if out is not None: print(out)
            except KeyError as ke:
                print("Unrecognized command: " + ke.args[0])


if __name__ == "__main__":
    repl()
