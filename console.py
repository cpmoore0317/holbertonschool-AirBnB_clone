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

    def do_create(self, line):
        """ Creates an instance of BaseModel """
        if line == "" or line is None:
            print("** class name missing **")
        elif line not in models.storage.classes():
            print("** class doesn't exist **")
        else:
            new_instance = models.storage.classes()[line]()
            new_instance.save
            print(new_instance.id)

    def do_show(self, line):
        lines = line.split()
        if not line:
            print("** class name missing **")
        elif lines[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
        elif len(lines) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(lines[0], lines[1])
            all_objs = models.storage.all()
            if key in all_objs:
                print(all_objs[key])
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        '''
         deletes instance based on class and id
        '''
        if line == '' or line is None:
            print('** class name missing **')
        else:
            lines = line.split(' ')
            if lines[0] not in models.storage.classes():
                print("** class doesn't exist **")
            elif len(lines) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(lines[0], lines[1])
                if key not in models.storage.all():
                    print("** no instance found **")
                else:
                    del models.storage.all()[key]
                    models.storage.save()

    def do_all(self, line):
        '''
        prints all str represenations
        '''
        if line != '':
            lines = line.split(' ')
            if lines[0] not in models.storage.classes():
                print("** class doesn't exist **")
            else:
                newlist1 = [str(obj) for key, obj in storage.all().items()
                            if type(obj).__name__ == lines[0]]
                print(newlist1)
        else:
            newlist2 = [str(obj) for key, obj in storage.all().items()]
            print(newlist2)

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
