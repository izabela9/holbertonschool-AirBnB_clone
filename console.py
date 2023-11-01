#!/usr/bin/python3

import cmd


class HBNBCommand(cmd.Cmd):
    """
    Class HBNB
    """
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        exit(0)

    def do_EOF(self, arg):
        """
        EOF command to exit the program
        """
        exit(0)

    def emptyline(self):
        """
        Empty line + enter
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
