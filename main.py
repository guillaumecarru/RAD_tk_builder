#######################################################
# Welcome to RAD_tk_builder                           #
# This program allows you to convert any .ui file     #
# into a constructed class in python                  #
#                                                     #
# For more informations on this program,              #
# please consult README.md file.                      #
#                                                     #
# Have fun !                                          #
#######################################################

import sys

# Import main class
from builder.python_builder import ParseIntoCreate

# To launch program, you should be in pipenv's shell
# Then type as following :
#
# python main.py arg1 arg2 arg3
#
# arg1 is the name of the python file that's going to be created.
# arg1 should not already exists, and should be a python file.
#
# arg2 is the name of the .ui file you want to convert.
# arg2 should be created from pygubu-designer.
#
# arg3 is the name of the conf file that's going to be created along with arg1.
# arg3 should not already exists, and should be a python file.
#
# WARNINGS : args should NOT have .ui or .py on top of them.
#
# Example:
# python main.py newdocument xmlfile conf_file

if __name__ == "__main__":
    NEW_FILE, UI_FILE, CONF_FILE = "", "", ""
    if len(sys.argv) >= 2:
        NEW_FILE = str(sys.argv[1])
    if len(sys.argv) >= 3:
        UI_FILE = str(sys.argv[2])
    if len(sys.argv) == 4:
        CONF_FILE = str(sys.argv[3])
    if len(sys.argv) == 1:
        print("you have to give arguments. Please check README.md\
for more informations")
    if len(sys.argv) > 1:
        while 1:
            try:
                if CONF_FILE:
                    PARSE = ParseIntoCreate(NEW_FILE, UI_FILE, CONF_FILE)
                    PARSE.creating_new_file()
                    print("Job done !")
                    break

                elif UI_FILE:
                    PARSE = ParseIntoCreate(NEW_FILE, UI_FILE)
                    PARSE.creating_new_file()
                    print("Job done !")
                    break

                elif NEW_FILE:
                    PARSE = ParseIntoCreate(NEW_FILE)
                    PARSE.creating_new_file()
                    print("Job done !")
                    break

            except:
                print("Oups !\n Something went wrong. Why don't you check\
README.md ?")
                break
