#!/usr/bin/python3
'''
defines hbnb console
'''
import cmd
import models
import re


class HBNBCommand(cmd.Cmd):
    '''
    defines the hbnb command interpreter
    '''
    prompt = '(hbnb) '


    def do_quit(self, arg):
        '''
        quit command for exit
        '''
        return True

    def do_eof(self, arg):
        '''
        eof signal to exit
        '''
        return True

    def emptyline(self):
        '''
        does nnothing with empty line
        '''
        pass

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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
