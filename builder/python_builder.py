#############################################################################################
# Class that gathers informations from XmlDictConfig class                                  #
# This class will parse all informations stacked up in XmlDictConfig instance               #
# and will create a file based of it.                                                       #
#############################################################################################

import xml.etree.ElementTree as ET
import errno

try:
    from builder.xml_converter import XmlDictConfig
    from builder.conf import FILEERROR, ATTRIBERROR, DEFAULTTITLE
    from builder.file_constructor import FileConstructor
except:
    from xml_converter import XmlDictConfig
    from conf import FILEERROR, ATTRIBERROR, DEFAULTTITLE
    from file_constructor import FileConstructor

class ParseIntoCreate:
    '''
    This class is meant to create a tkinter code.
    It takes as argument uifile a .ui file, created on pygubu-designer
    It will convert and create a new document coded in python in newfile

    if you don't give uifile any argument, it will load a default template
    you can consult in your target path.

    newfile is the file that's going to be created.

    defaultconf is the file that will include all variables for newfile.

    For more informations, please consult the README.md file.
    Have fun !
    '''

    def __init__(self, newfile, uifile="tests/template_ui_file.ui", defaultconf="conf.py"):
        # newfile is the file that this class will create
        self.newfile = newfile

        # ui file is the file that's going to be converted
        self.uifile = uifile

        # defaultconf is the file that will be created and will include all
        # variables for newfile
        self.defaultconf = defaultconf

        # getting all informations from ui file
        try:
            tree = ET.parse(self.uifile)
            root = tree.getroot()

        except OSError as er:
            #if file isn't an xml file
            if er.errno == errno.ENOENT:
                print(FILEERROR)
                return

        try:
            # Converting xml data into dictionnary
            self.xmldict = XmlDictConfig(root)

        except UnboundLocalError:
            # if file can't be read
            print(ATTRIBERROR)
            return

        # Loading constructor class
        self.constructor = FileConstructor()

        # Converting object into dictionnary
        self.creating_new_dicts()

    def creating_new_dicts(self):
        ''' This function is taking data inside xmldict
        and converts them into a new dictionnary.
        XmlDictConfig looks like a dictionnary, but it
        renders an object.
        This class also prevents the code from being spread
        out in the new file.
        '''

        # removing useless data
        self.xmldict = self.xmldict["object"]

        # Creating a new dictionnary from self.xmldict
        # xmldict is actually an instance of XmlDictConfig
        # class, and by no mean a dictionnary
        self.realdict = {}

        # Adding xmldict values to realdict
        # cant do for x, y for some reasons
        for keys in self.xmldict:
            self.realdict[keys] = self.xmldict[keys]

    def creating_new_file(self):
        '''This function takes self.realdict datas
        and converts them into code, using conf.py file
        as database
        '''

        # Fullfilling self.newfile with data
        with open(self.newfile, "w") as newdoc:
            #Documentation
            newdoc.write(self.constructor.create_stock_class(self.defaultconf))

            #Creating class and init
            newdoc.write(self.constructor.create_class_and_init(DEFAULTTITLE))

        newdoc.close()

    def testing_xmldict_working(self):
        '''
        Testing if init is working properly
        This test function should be deleted
        '''
        print(self.realdict)

if __name__ == '__main__':
    # test to make sure everything is working properly
    parser = ParseIntoCreate("newdocument.py", "tests/template_ui_file.ui")
    parser.testing_xmldict_working()
