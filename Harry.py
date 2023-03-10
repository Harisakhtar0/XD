import os, platform

os.system("xdg-open https://www.facebook.com/groups/893149411835087/?ref=share")

os.system('git pull')

import requests

bit = platform.architecture()[0]

if bit == '64bit':

    from nonofix import menu

    menu()

elif bit == '32bit':

    print("NOT UPDATED YET BRO ")






