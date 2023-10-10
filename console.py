#!/usr/bin/python3
'''
defines hbnb console
'''
import cmd


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def empty_line(self):
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

        print('')
        return True

    if __name__ == '__main__':
        HBNBCommand().cmdloop()
