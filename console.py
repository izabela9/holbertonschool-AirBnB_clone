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

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in models.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key not in models.storage.all():
                print("** no instance found **")
            else:
                print(models.storage.all()[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in models.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key not in models.storage.all():
                print("** no instance found **")
            else:
                del models.storage.all()[key]
                models.storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        args = arg.split()
        if len(args) > 0 and args[0] not in models.classes:
            print("** class doesn't exist **")
        else:
            for key in models.storage.all():
                if len(args) > 0 and key.split('.')[0] != args[0]:
                    continue
                print(models.storage.all()[key])

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in models.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key not in models.storage.all():
                print("** no instance found **")
            elif len(args) == 2:
                print("** attribute name missing **")
            elif len(args) == 3:
                print("** value missing **")
            else:
                setattr(models.storage.all()[key], args[2], type(getattr(models.storage.all()[key], args[2]))(args[3]))
                models.storage.all()[key].save()


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
