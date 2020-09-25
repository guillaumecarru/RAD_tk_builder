#############################################################################################
# This class takes a dictionnary as arg                                                     #
# Converts it into a list                                                                   #
# This list will contain args that will be given to FileConstructor class                   #
# This list allows to build the core of the new file                                        #
#############################################################################################

class RecursivePackager:
    '''

    arg_dict argument = dictionnary

    This dictionnary has to be built by ParseIntoCreate.creating_new_dicts function
    '''

    def __init__(self, arg_dict):
        # arg_dict is self.realdict that comes from ParseIntoCreate.creating_new_dicts function
        self.arg_dict = arg_dict

        # This list is going to be returned with all informations parsed
        self.returned_list = []

    def recursive_list_creator(self, master_widget=""):
        '''
        This is the main function of the class.
        It allows to convert arg_dict into a list.

        master_widget is the master's widget id. Usefull for writing objects.

        List datas renders like this:

        returned_list = [["master_id",
                          "id",
                          "class_valor",
                          ["properties_valors"],
                          ["layout_valors"]],
                          [etc...]
                        ]

        properties_valors comes like this : ["borderwidth='3', height='100',
                                            text={},
                                            width='465'", "text_of_property",
                                            "some text"]

        layout_valors comes like this : ["grid(column='0', row='4', sticky='w')",
                                         "grid_propagate(0)"]

        layout_valors are always lists, even if there is only one valor
        properties_valors are always lists, even if there is no text.
        '''

        # This list will be fulfilled during that iteration
        # And added to
        list_for_current_iteration = []

        # Adding master's widget. Default = none
        list_for_current_iteration.append(master_widget)

        # Check if it's dictionnary or list
        if isinstance(self.arg_dict["object"], list):
            for widgets in self.arg_dict["object"]:
                # Add id valor
                if "id" not in widgets:
                    list_for_current_iteration.append("")
                elif "id" in widgets:
                    list_for_current_iteration.append(widgets["id"])

                # Add class valor
                list_for_current_iteration.append(widgets["class"])

                # Add properties valors
                if "properties" in widgets:
                    list_for_current_iteration.append(self.creating_properties_valors(widgets["property"]))

                if "layout" in self.arg_dict["object"]:
                    list_for_current_iteration.append(self.creating_layout_valors(widgets["layout"]))
            #bla bla
        for valor in self.arg_dict:
            if "version" in valor and "object" in valor:
                print("ok")

        print("ok")

    def creating_properties_valors(self, dict_or_list):
        '''
        This function converts dictionnary "properties" into writable code
        '''

        # list that will stock informations and give it to list_for_current_iteration
        creating_properties = []

        #check if dict_or_list is a dict or list
        if isinstance(dict_or_list, list):
            #If it's a list
            for properties in dict_or_list:
                # if list is not empty and properties does NOT contain text
                if creating_properties and properties["name"] != "text":
                    creating_properties[0] += ", {}='{}'".format(properties["name"],
                                                                 properties["property"])

                # if list is not empty and properties does contain text
                elif creating_properties and properties["name"] == "text":
                    creating_properties[0] = properties["name"] + "={}, " + creating_properties[0]
                    creating_properties.append(properties["property"])

                # If list is empty and properties does NOT contain text
                elif not creating_properties and properties["name"] != "text":
                    creating_properties.append("{}='{}'".format(properties["name"],
                                                                properties["property"]))

                #if list is empty and properties contains text
                elif not creating_properties and properties["name"] == "text":
                    creating_properties.append(properties["name"] +"={}")
                    creating_properties.append(properties["property"])

            #After the loop, returns the list
            return creating_properties

        # if dict_or_list is a dict and name contains text
        if dict_or_list["name"] == "text":
            creating_properties.append(dict_or_list["name"] + "={}")
            creating_properties.append(dict_or_list["property"])

        # if dict_or_list is a dict and name does NOT contains text
        else:
            creating_properties.append("{}='{}'".format(dict_or_list["name"],
                                                        dict_or_list["property"]))

        #After giving all informations from the dict, returning the list
        return creating_properties

    def creating_layout_valors(self, dict_or_list):
        '''
        This function converts dictionnary "valors" into writable code
        '''

        # list that will stock informations and give it to
        # list_for_current_iteration
        creating_layout = []

        

if __name__ == '__main__':
    pass
