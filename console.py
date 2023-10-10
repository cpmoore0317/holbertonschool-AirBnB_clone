#!/usr/bin/python3
'''
defines hbnb console
'''
import cmd
import models
import re
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    '''
    defines the hbnb command interpreter
    '''
    prompt = '(hbnb) '


    def do_create(self, arg):
        """ Creates an instance of BaseModel """
        if arg == "" or arg is None:
            print("** class name missing **")
        elif arg not in models.storage.classes():
            print("** class doesn't exist **")
        else:
            new_instance = models.storage.classes()[arg]()
            new_instance.save
            print(new_instance.id)

    def do_show(self, arg):
        args = arg.split()
        if not arg:
             print("** class name missing **")
        elif args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            all_objs = models.storage.all()
            if key in all_objs:
                print(all_objs[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        '''
         deletes instance based on class and id
        '''
        if arg == '' or arg is None:
            print('** class name missing **')
        else:
            args = arg.split(' ')
            if args[0] not in models.storage.classes():
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(args[0], args[1])
                if key not in models.storage.all():
                    print("** no instance found **")
                else:
                    del models.storage.all()[key]
                    models.storage.save()

    def do_EOF(self, line):
        '''
        handles eof char
        '''
        print()
        return True

    def do_quit(self, line):
        '''
        exit program
        '''
        return True

    def default(self, line):
        if line == "quit" or line == "EOF":
            return True
        return super().default(line)

    def emptyline(self):
        """ Determines behavior when empty line is passed """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
