#############################################################################################
#                                                                                           #
# Class that stocks constructor, works in synergy with ParseIntoCreate class                #
#                                                                                           #
#############################################################################################

import json

class FileConstructor:
    '''
    This class is meant to be called by ParseIntoCreate class
    '''

    def __init__(self):
        with open("builder/dao.json") as json_file:
            data = json.load(json_file)
            self.data = data

    def create_stock_class(self, arg1):
        '''
        This function adds tkinter module into the document
        It also adds variables with an import.

        arg1 = file of variables for new document
n
        '''

        return self.data["introduction"].format(arg1)

    def create_class_and_init(self, arg1):
        '''
        This function creates the name of the new class
        It also adds __init__() to the document.

        arg1 is the TITLE name

        '''
        if arg1:
            #if title exists
            return self.data["classcreation"].format(arg1)
        else:
            return self.data["classcreation"].format("")

    def add_main_widget_function_to_init(self, arg1):
        '''
        This function adds function in init so it launches itself at start

        arg1 is the name of the function.
        arg1 should look like : self.add_"function_name"

        '''

        return self.data["addfunction"].format(arg1, arg1)

    def add_widgets_to_master_widgets_func(self, arg1):
        '''
        This function adds function in init so it launches itself at start
        This function adds widgets to arg1.

        arg1 is the name of the function.
        arg1 should look like : self.add_"function_name"

        '''

        return self.data["addfuncmaster"].format(arg1, arg1)

    def add_master_function(self, arg1):
        '''
        This function adds master function arg1.

        Takes only one arg
        '''

        return self.data["masterfunctionname"].format(arg1, arg1)

    def add_widgets_function(self, arg1):
        '''
        This function adds widgets to arg1

        Takes only one arg as master widget of slave widgets
        '''

        return self.data["widgetfunctionname"].format(arg1, arg1)

    def add_identify_id_class_master(self, arg1, arg2, arg3=""):
        '''
        This function creates widget's name and instanciates it.

        It gives his name as arg1
        arg2 is his class
        If it is not a master widget (that doesn't instanciates from Tk()),
        you can give arg3 as his master widget
        '''

        return self.data["functionidandclass"].format(arg1, arg2, arg3)

    def add_widget_conf(self, arg1, arg2):
        '''
        This function adds config to the current widget.

        arg1 is the name of widget
        arg2 is the configuration.

        args should match this :
        self.{arg1}.config({arg2})
        '''

        return self.data["widgetconfig"].format(arg1, arg2)

    def add_widget_loc(self, arg1, arg2):
        '''
        This function adds placement to the current widget.

        arg1 is the name of widget
        arg2 is its placement

        args should match this:
        self.{arg1}.{arg2}

        '''

        return self.data["widgetplace"].format(arg1, arg2)

    def add_launch_function(self):
        '''
        This function adds the "launch" function in
        the new document. No args needed.
        '''

        return self.data["launchfunction"]

    def add_name_eq_main(self):
        '''
        This function adds if__name__ == '__main__'
        This allow the tkinter window to launch automatically if
        called from the name of document.

        No argument needed.
        '''

        return self.data["ifnameeqmain"]

    def add_intro_conf(self, arg1):
        '''
        This function adds intro to conf file

        Takes name of tk file as arg1
        '''

        return self.data["introconf"].format(arg1)

    def add_text(self, arg1, arg2):
        '''
        This function adds text in conf file
        for new_file configuration

        Takes arg1 as name of variable
        arg2 is the text

        '''

        return self.data["addtext"].format(arg1, arg2)

if __name__ == '__main__':
    print("This is a constructor class, made for ParseIntoCreate class. \
For more informations on how to use this program, please consult README.md \
file")
