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
    from builder.recursive_packager import RecursivePackager
except:
    from xml_converter import XmlDictConfig
    from conf import FILEERROR, ATTRIBERROR, DEFAULTTITLE
    from file_constructor import FileConstructor
    from recursive_packager import RecursivePackager

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

        # self.realdict is now a packaged list
        self.real_list = RecursivePackager(self.realdict)
        self.real_list = self.real_list.return_converted_list()

        # dictionnary of text for conf.py file
        # List valors goes like this : [["LABEL_FRAME_TEXT", "some text"],
        #                               ...
        #                              ]
        self.conf_text = []


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
        '''
        This function takes self.realdict datas
        and converts them into code, using conf.py file
        as database
        '''

        widget_list = self.getting_master_widgets()

        # Fullfilling self.newfile with data
        with open(self.newfile, "w") as newdoc:
            #Documentation
            newdoc.write(self.constructor.create_stock_class(self.defaultconf))

            #Creating class and init
            newdoc.write(self.constructor.create_class_and_init(DEFAULTTITLE))

            # Adding functions in init
            for widgets in widget_list:
                # If widget is master widget
                # and instanciates from tk()
                if widgets[1]:
                    newdoc.write(self.constructor.add_main_widget_function_to_init(widgets[0]))
                    newdoc.write(self.constructor.add_widgets_to_master_widgets_func(widgets[0]))
                else:
                    newdoc.write(self.constructor.add_widgets_to_master_widgets_func(widgets[0]))
            # Creating functions, fulfilling them

            # Know which widgets gets two functions passes
            for widgets in widget_list:
                # If widgets[0] is an instance of Tk()
                if widgets[1]:
                    # Create master widget in its own function
                    self.creating_function(self.who_s_your_master(widgets[0], True),
                                           newdoc,
                                           True)
                # Add slave widgets
                self.creating_function(self.who_s_your_master(widgets[0]),
                                       newdoc)

        newdoc.close()

    def who_s_your_master(self, arg1, master=False):
        '''
        This function takes arg1, parses self.real_list and
        returns a list only containing widgets that have arg1
        as master.

        Optionnal argument as "master" is given if we're looking
        for all informations of arg1 only.
        '''

        new_list = []

        # If arg1 is instance of Tk()
        if master:
            for widgets in self.real_list:
                if arg1 == widgets[1]:
                    new_list.append(widgets)

        # If we're looking for all widgets that arg1 has
        elif not master:
            for widgets in self.real_list:
                if arg1 == widgets[0]:
                    new_list.append(widgets)

        # Return new_list once completed
        return new_list


    def creating_function(self, list_widgets, document, master=False):
        '''
        This function helps creating_new_file function.
        It parses RecursivePackager result to create
        a function for the new file

        Change master to True ONLY if you need to create
        a master function.
        '''

        # If master = True
        # Unique case
        if master:
            document.write(self.constructor.add_master_function(list_widgets[0][1]))

        elif not master:
            document.write(self.constructor.add_widgets_function(list_widgets[0][0]))

        # Create loop, adding all widgets in list_widgets inside the function
        for widgets in list_widgets:
            # Add id and class for current widget
            # if master = True, no arg3
            if master:
                document.write(self.constructor.add_identify_id_class_master(widgets[1],
                                                                             widgets[2]))

            # Add arg3 if master = False
            elif not master:
                document.write(self.constructor.add_identify_id_class_master(widgets[1],
                                                                             widgets[2],
                                                                             widgets[0]))


            if widgets[3]:
                # if there is text in properties
                if len(widgets[3]) > 1:
                    self.conf_text.append([self.cap_text(widgets[1]), widgets[3][1]])
                    document.write(self.constructor.add_widget_conf(widgets[1],
                                                                    widgets[3][0].format(self.cap_text(widgets[1]))))

                elif len(widgets[3]) == 1:
                    document.write(self.constructor.add_widget_conf(widgets[1],
                                                                    widgets[3][0]))

            if widgets[4]:
                document.write(self.constructor.add_widget_loc(widgets[1],
                                                               widgets[4][0]))
                # If _propagate == False
                # Add place_propagate(0)
                if len(widgets[4]) > 1:
                    document.write(self.constructor.add_widget_loc(widgets[1],
                                                                   widgets[4][1]))

            # Add spaces between widgets / functions
            # for each iteration
            document.write("\n")


    def cap_text(self, arg):
        '''
        This function takes arg and converts it to ARG_TEXT

        This function is usefull for the conf.py text.
        '''

        return arg.upper() + "_TEXT"

    def getting_master_widgets(self):
        '''
        This function works with creating_functions_for_new_file
        It returns a list with all master widgets.
        Initial list is self.real_list

        Returns valors like this : [[example_widget, True]...]
        True means example_widget is a master widget that instanciates
        directly from tk()
        False means example_widget is an instance of another widget.

        '''

        return_list = []

        # Loop that gets all master widgets
        for valors in self.real_list:
            if valors[0]not in return_list:
                return_list.append(valors[0])

        list_valors = []

        # Checking which widget is main widget.
        for masters in return_list:
            for valors in self.real_list:
                # Do not count [] empty list
                if isinstance(masters, str):
                    if masters == valors[1] and not valors[0]:
                        list_valors.append([masters, True])
                    if masters == valors[1] and valors[0]:
                        list_valors.append([masters, False])

        return list_valors

if __name__ == '__main__':
    # test to make sure everything is working properly
    parser = ParseIntoCreate("newdocument.py", "tests/template_ui_file.ui")
