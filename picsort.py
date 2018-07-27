#  Matthew Scozzafava
#  picture sorting program for physics seminar project
#
#
# linux and windows
# checks for folders and creates them
# then scans for jpgs' and gifs' and sorts them in the correct folder
# prompts user when completed 
#

import os     # used to locate directories and make it work in windows and linux file systems 
import glob   # used to search directory for files with * wild card 
import shutil # used to move and over write files 

# check/create folders for both linux and windows

if os.path.isdir('jpg'):
    print('jpg folder exists \n' + os.path.abspath('jpg'))
else:
     os.makedirs(os.getcwd() + os.sep + 'jpg')
     print('jpg folder created \n' + os.path.abspath('jpg'))


if os.path.isdir('gif'):
    print('gif folder exists \n' + os.path.abspath('gif'))
else:
    os.makedirs(os.getcwd() + os.sep + 'gif')
    print('gif folder created \n' + os.path.abspath('gif'))




# sort for jpg files

write = True
skip = True

for x in glob.glob('*.jpg'):
   
    if os.path.isfile(x) and os.path.isfile('jpg' + os.sep + x) and write and skip:
       
        print('To overwrite '+ x +'\n type y and press enter or a and press enter to overwrite all\n type s to skip this file or e to skip all\n')
       
       while True: # takes some user input
            over = input()
            if over == 'a':
                write = False
                shutil.move(x ,'jpg'+ os.sep + x)
                break
            elif over == 'y':
                shutil.move(x ,'jpg'+ os.sep + x)
                break
            elif over == 's':
                break
            elif over == 'e':
                skip = False
                break
            else:
                print('type either y, a, s, or e')

    elif not skip and os.path.isfile('jpg'+ os.sep + x):
        pass
    elif not write:
        shutil.move(x, 'jpg' + os.sep + x)
    else:
        shutil.move(x ,'jpg')
else:
    print('no more jpgs\' to sort')


# sort gif files

write = True
skip = True
for x in glob.glob('*.gif'):
    if os.path.isfile(x) and os.path.isfile('gif' + os.sep + x) and write and skip:
        print('To overwrite '+ x +'\n type one of the following letters \ny to overwrite this file\na to overwrite all files\n type s to skip this file\ne to skip all\n and press enter once one has been typed')
        while True:
            over = input()
            if over == 'a':
                write = False
                shutil.move(x ,'gif'+ os.sep + x)
                break
            elif over == 'y':
                shutil.move(x ,'gif'+ os.sep + x)
                break
            elif over == 's':
                break
            elif over == 'e':
                skip = False
                break
            else:
                print('type either y, a, s, or e')

    elif not skip and os.path.isfile('gif'+ os.sep + x):
        pass
    elif not write:
        shutil.move(x, 'gif' + os.sep + x)
    else:
        shutil.move(x ,'gif')
else:
    print('no more gifs\' to sort')


