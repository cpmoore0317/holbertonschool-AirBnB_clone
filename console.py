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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
