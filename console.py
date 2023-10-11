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
        objectlist = []
        models.storage.reload()
        objects = models.storage.all()

        class_name = line.strip()

        if class_name not in models.storage.classes:
            print("** class doesn't exist **")
            return

        for key, val in objects.items():
            if val.__class__.__name__ == class_name:
                objectlist.append(val)
        for obj in objectlist:
            print(obj)

    def do_update(self, line):
        """
        updates an instance based on the class name and id
        """
        lines = shlex.split(line)
        if not lines:
            print("** class name missing **")
            return
        if not lines[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(lines) < 2:
            print("** instance id missing **")
            return
        obj_id = lines[1]
        key = lines[0] + "." + obj_id
        objects = models.storage.all()
        if key not in objects:
            print("** no instance found **")
            return
        if len(lines) < 3:
            print("** attribute name missing **")
            return
        if len(lines) < 4:
            print("** value missing **")
            return
        attribute_name = lines[2]
        attribute_value = lines[3]
        if hasattr(objects[key], attribute_name):
            attribute_value = eval(attribute_value)
            setattr(objects[key], attribute_name, attribute_value)
            objects[key].save()
        else:
            print("** attribute doesn't exist **")


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
