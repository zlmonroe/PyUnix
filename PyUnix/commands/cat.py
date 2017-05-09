import os


def cat(lookup, *args):
    if os.path.isfile(args[0]):
        with open(args[0], "r") as file:
            return file.read()
