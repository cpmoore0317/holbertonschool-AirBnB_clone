#!/usr/bin/python3
'''
defines hbnb console
'''
import cmd
import models
import re
import shlex
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class HBNBCommand(cmd.Cmd):
    '''
    defines the hbnb command interpreter
    '''
    prompt = '(hbnb) '
    class_list = ['BaseModel', 'User', 'State', 'City',
                  'Amenity', 'Place', 'Review']

    def do_create(self, args):
        """ Creates an instance of BaseModel """
        if len(args) == 0:
            print("** class name missing **")
            return False
        elif args in classes.keys():
            instance = classes[args]()
            print(instance.id)
            instance.save()
        else:
            print("** class doesn't exist **")

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

    def do_destroy(self, args):
        '''
         deletes instance based on class and id
        '''
        args = shlex.split(args)
        if len(args) == 0:
            print("** class name missing **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        classname = args[0]
        classid = args[1]
        objects = models.storage.all()
        try:
            eval(classname)
        except NameError:
            print("** class doesn't exist **")
            return
        key = classname + '.' + classid
        try:
            del objects[key]
        except KeyError:
            print("** no instance found **")
        models.storage.save()

    def do_all(self, args):
        '''
        prints all str represenations
        '''
        line = args.split()
        objects = models.storage.all()
        finalprint = []
        if len(line) == 0:
            for v in objects.values():
                finalprint.append(str(v))
        elif line[0] in HBNBCommand.class_list:
            for k, v in objects.items():
                if line[0] in k:
                    finalprint.append(str(v))
        else:
            print("** class doesn't exist **")
            return False
        print(finalprint)

    def do_update(self, args):
        """
        updates an instance based on the class name and id
        """
        args = shlex.split(args)
        if len(args) == 0:
            print("** class name missing **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        elif len(args) == 2:
            print("** attribute name missing **")
            return
        elif len(args) == 3:
            print("** value missing **")
            return
        try:
            eval(args[0])
        except NameError:
            print("** class doesn't exist **")
            return
        key = args[0] + "." + args[1]
        objects = models.storage.all()
        try:
            objectvalue = objects[key]
        except KeyError:
            print("** no instance found **")
            return
        try:
            attributetype = type(getattr(objectvalue, args[2]))
            args[3] = attr_type(args[3])
        except AttributeError:
            pass
        setattr(objectvalue, args[2], args[3])
        objectvalue.save()

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
