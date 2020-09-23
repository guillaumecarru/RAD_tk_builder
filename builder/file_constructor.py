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

