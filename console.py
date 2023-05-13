#!/usr/bin/python3
"""Defines AirBnB console"""
import cmd


class HBNBCommand(cmd.Cmd):
    """DEfines AirBN command iintepreter

    Attrinutes:
        prompt (str): the command propmpt
    """

    prompt = "(hbnb)"

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF signal to quit program"""
        print("")
        return True

    def emptyline(self):
        """Does nothing incase of empty line"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
