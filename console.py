#!/usr/bin/python3
'''
defines hbnb console
'''
import cmd
import models


class HBNBCommand(cmd.Cmd):
    '''
    defines the hbnb command interpreter
    '''
    prompt = '(hbnb) '

    def emptyline(self):
        '''
        does nothing with empty line
        '''
        pass

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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
