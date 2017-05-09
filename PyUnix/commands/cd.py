import os


def cd(lookup, *args):
    if os.path.exists(args[0]):
        os.chdir(args[0])
    else:
        return args[0] + " is not a valid directory"
