#!c:\python27\python.py -u

import os
import sys

strings = {'path': '', 'old_string': '', 'new_string': ''}

print 'Copyright 2012 - Bradley Moore\n\n'
print '\nLet\'s rename some files, Yo!'

def format_path(string):
    if string.startswith('"'):
        string = string[1:]
    if string.endswith('"'):
        string = string[:-1]

    if string.endswith('\\'):
        return string
    elif '.' not in string[-5:]:
        return string + '\\'
    else:
        string_reversed = string[::-1]
        last_slash = string_reversed.find('\\')
        string_reversed = string_reversed[last_slash:]
        string = string_reversed[::-1]
        return string

def get_info():
    valid_path_input = False
    while valid_path_input == False:
        try:
            strings['path'] = raw_input('\nPath: ')
            strings['path'] = format_path(strings['path'])
            fnames = os.listdir(strings['path'])
            valid_path_input = True
        except OSError:
            print 'Invalid path'
            continue

    strings['old_string'] = raw_input('Old string: ')
    strings['new_string'] = raw_input('New string: ')

    return fnames

def rename_files(fnames):
    print '\n'
    for fname in fnames:
        if strings['old_string'] in fname:
            try:
                os.rename(strings['path'] + fname, strings['path'] + 
                          fname.replace(strings['old_string'], 
                                        strings['new_string'], 1))
                print 'Renaming %s to %s.....Success!' % (fname, fname.replace(
                                                          strings['old_string'], 
                                                          strings['new_string']))
            except (WindowsError, OSError):
                print 'Error renaming "%s" to "%s"' % (fname, fname.replace(
                                                       strings['old_string'], 
                                                       strings['new_string']))
                print sys.exc_info()[1]
    return

def rename_another():
    again = raw_input('\nRename more files (yes or no): ')
    if again == 'yes' or again == 'y':
        pass
    else:
        sys.exit()
    return

if __name__ == '__main__':
    while True:
        rename_files(get_info())
        rename_another()