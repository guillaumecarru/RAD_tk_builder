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

import click

# Import main class
from builder.python_builder import ParseIntoCreate

# To launch program, you should be in pipenv's shell
# Then type as following :
#
# python main.py arg1 --ui arg2 --conf arg3
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
# Example:
# python main.py newdocument.py --uifile file.ui --conf_file conf.py

@click.command()
@click.option("--uifile", "-ui", help="file xml that's going to be converted")
@click.option("--conf_file","-conf", help="file that contains all variables\
for newfile")
@click.argument("newfile")

def createdoc(newfile, uifile, conf_file):
    """
    \b
    This program works with pygubu-designer.
    For more informations on pygubu, please consult README.md

    \b
    This CLI takes as argument the file that's going to be created.
    It will contain the tkinter code.

    \b
    Example of how it should be writen:
        python main.py newdocument.py --uifile xmlfile.ui -conf conf.py

    \b
    NOTE: You can run the program with only one argument.
    You will somehow get an example of what you can expect from
    this RAD tool.

    \b
    NOTE: ADD .py and .ui at the end of your files, otherwise
    program will not work.
    """

    var_ended = "\nProgram process is done\n"

    # Displaying all cases
    if uifile and conf_file:
        parse = ParseIntoCreate(newfile, uifile, conf_file)
        click.echo(var_ended)
        return

    elif uifile:
        parse = ParseIntoCreate(newfile, uifile)
        click.echo(var_ended)
        return

    elif conf_file:
        parse = ParseIntoCreate(newfile, defaultconf=conf_file)
        click.echo(var_ended)
        return

    parse = ParseIntoCreate(newfile)
    click.echo(var_ended)
    return

if __name__ == '__main__':
    createdoc()
