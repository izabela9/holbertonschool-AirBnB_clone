#!/usr/bin/python3
"""
Defines the HBNBCommand class.
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """
    Class HBNB
    """
    prompt = '(hbnb) '
    

    def __init__(self):
        self.commands = {
                "create": self.create,
                "show": self.show,
                "destroy": self.destroy,
                "all": self.all,
                "update": self.update
                }

    def create(self, args):
        """
        Create method
        """
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
        else:
            instance = BaseModel()
            instance = save()
            print(instance.id)

    def show(self, args):
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            instance_id = args[1]
            if instance_id not in storage.all(BaseModel):
                print("** no instance found **")
            else:
                instance = storage.all(BaseModel)[instamnce_id]
                print(str(instance))

    def destroy(self, args):


    def all(self, args):

    def update(self, args):

    def run(self, args):
        while True:
            command = input("$ ").split()
            if command[0] in self.commands:
                self.commands[comand[0]](command[1:])

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        exit(0)

    def do_EOF(self, arg):
        """
        EOF command to exit the program
        """
        print()
        exit(0)

    def emptyline(self):
        """
        Empty line + enter
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
