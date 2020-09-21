#############################################################################################
# Class that gathers informations from XmlDictConfig class                                  #
# This class will parse all informations stacked up in XmlDictConfig instance               #
# and will create a file based of it.                                                       #
#############################################################################################

import xml.etree.ElementTree as ET
import errno

try:
    from builder.xml_converter import XmlDictConfig
    from builder.conf import FILEERROR, ATTRIBERROR
except:
    from xml_converter import XmlDictConfig
    from conf import FILEERROR, ATTRIBERROR

class ParseIntoCreate(object):
    ''' Usage (write it down when it's all over)
    '''

    def __init__(self, uifile):
        # ui file is the file that's going to be converted
        self.uifile=uifile

        # getting all informations from ui file
        try:
            tree = ET.parse(self.uifile)
            root = tree.getroot()

        except OSError as er:
            #if file isn't an xml file
            if er.errno == errno.ENOENT:
                print(FILEERROR)

        try:
            # Converting xml data into dictionnary
            self.xmldict = XmlDictConfig(root)
            # Removing useless informations
            self.xmldict = self.xmldict["object"]

        except UnboundLocalError:
            # if file can't be read
            print(ATTRIBERROR)

    def creating_new_dicts(self):
        ''' This function is taking data inside xmldict
        and converts them into a new dictionnary.
        XmlDictConfig looks like a dictionnary, but it
        renders an object.
        This class also prevents the code from being spread
        out in the new file.
        '''

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



    def testing_xmldict_working(self):
        print(self.xmldict)

if __name__ == '__main__':
    # test to make sure everything is working properly
    parser = ParseIntoCreate("tests/template_ui_file.ui")
    parser.testing_xmldict_working()
