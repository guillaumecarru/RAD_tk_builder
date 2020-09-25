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
                list_for_current_iteration.append(self.arg_dict["object"]["id"])

                # Add class valor
                list_for_current_iteration.append(self.arg_dict["object"]["class"])

                # Add properties valors
                list_for_current_iteration.append(self.creating_properties_valors(self.arg_dict["object"]["property"]))
            #bla bla
            print("ok")
        for valor in self.arg_dict:
            if "version" in valor and "object" in valor:
                print("ok")

        print("ok")

    def creating_properties_valors(self, dict_or_list):
        '''
        This function converts dictionnary into writable code
        '''

        # list that will stock informations and give it to list_for_current_iteration
        creating_properties = []

        #check if dict_or_list is a dict or list
        if isinstance(dict_or_list, list):
            #If it's a list
            for properties in dict_or_list:
                # Need to change this
                creating_properties += self.loop_for_properties_valors(properties) + ", "
            return creating_properties

        #If it's a dict
        else:
            creating_properties += self.loop_for_properties_valors(dict_or_list)
        return creating_properties

    def loop_for_properties_valors(self, dictio_properties):
        '''
        This function is used by creating_properties_valors function
        It takes dictionnary, parses it, and returns a fonctionnal code
        out of it.
        '''
        # Creating temporary string
        temp_stock = ""
        temp_list = []

        for valors in dictio_properties:
            if valors["translatable"]:
                temp_stock = valors["name"] + " = "
                temp_list.append(temp_stock)
                temp_list.append(valors["property"])
                return temp_list
            else:
                temp_stock = valors["name"] + " = "
                temp_stock += valors["property"]
                temp_list.append(temp_stock)
                return temp_list

if __name__ == '__main__':
    pass
