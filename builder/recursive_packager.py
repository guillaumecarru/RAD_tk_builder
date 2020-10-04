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

        # This list contains all widgets that are on the same tree place.
        # It first contains self.arg_dict, then will contain any child
        # arg_dict has.
        self.running_list = [arg_dict]
        # self.master_list works with self.running_list.
        # It helps giving master widget to recursive_list_creator function
        self.master_list = [""]
        #Launching recursive function
        self.recursive_list_creator(self.running_list[0], self.master_list)

    def recursive_list_creator(self, curr_dict_iteration, master_widget):
        '''
        This is the main function of the class.
        It allows to convert curr_iteration into a list.

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

        # Check if it's dictionnary or list
        if isinstance(curr_dict_iteration, list):
            for args in curr_dict_iteration:

                # List for current iteration
                current_iteration = []

                # Adding master's widget. Default = none
                current_iteration.append(master_widget)

                # If it's a dict
                list_temp = self.widget_list_compacter(args["object"])

                for val in list_temp:
                    current_iteration.append(val)

                # Adding informations to returned_list
                self.returned_list.append(current_iteration)

        elif isinstance(curr_dict_iteration, dict):
            if "object" in curr_dict_iteration:
                curr_dict_iteration = curr_dict_iteration["object"]
            list_temp = self.widget_list_compacter(curr_dict_iteration)

            # List for current iteration
            current_iteration = []

            # Adding master's widget. Default = none
            current_iteration.append(master_widget)


            for val in list_temp:
                current_iteration.append(val)
            # Adding informations to returned_list
            self.returned_list.append(current_iteration)

        # deleting current iteration
        del self.running_list[0]
        del self.master_list[0]
        # Recursive loop launched
        while self.running_list:
            self.recursive_list_creator(self.running_list[0], self.master_list[0])

    def widget_list_compacter(self, dictio):
        '''
        This function take dictio as arg, and creates a fully fonctionnal list
        out of it

        dictio should be one full instance of a widget and contain "id" and
        "layout" valors.
        '''
        # Temporary list that will stock informations and return them once
        # gathered
        list_for_current_iteration = []

        # Add id valor
        if "id" not in dictio:
            list_for_current_iteration.append("")
        elif "id" in dictio:
            list_for_current_iteration.append(dictio["id"])

        # Add class valor
        list_for_current_iteration.append(dictio["class"])

        # Add properties valors
        if "property" in dictio:
            list_for_current_iteration.append(self.creating_properties_valors(dictio["property"]))
        elif not "property" in dictio:
            list_for_current_iteration.append([])

        if "layout" in dictio:
            list_for_current_iteration.append(self.creating_layout_valors(dictio["layout"]))

        # Adding to running_list and master_list dictionnaries / lists to
        # continue the recursive loop
        if "child" in dictio:
            self.running_list.append(dictio["child"])
            self.master_list.append(dictio["id"])


        # Returning temporary dictionnary
        return list_for_current_iteration

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
                    creating_properties[0] += ", " + properties["name"] + "='{}'"
                    creating_properties.append(properties["property"])

                # If list is empty and properties does NOT contain text
                elif not creating_properties and properties["name"] != "text":
                    creating_properties.append("({}='{}'".format(properties["name"],
                                                                 properties["property"]))

                #if list is empty and properties contains text
                elif not creating_properties and properties["name"] == "text":
                    creating_properties.append("(" + properties["name"] + "={}")
                    creating_properties.append(properties["property"])

            #After the loop, returns the list
            creating_properties[0] += ")"
            return creating_properties

        # if dict_or_list is a dict and name contains text
        if dict_or_list["name"] == "text":
            creating_properties.append("(" + dict_or_list["name"] + "={})")
            creating_properties.append(dict_or_list["property"])

        # if dict_or_list is a dict and name does NOT contains text
        else:
            creating_properties.append("({}='{}')".format(dict_or_list["name"],
                                                          dict_or_list["property"]))

        #After giving all informations from the dict, returning the list
        return creating_properties

    def creating_layout_valors(self, layout_data):
        '''
        This function converts dictionnary "valors" into writable code
        '''

        # list that will stock informations and give it to
        # list_for_current_iteration
        creating_layout = []

        # Adding grid, place or pack on top of returning list
        creating_layout.append(layout_data["manager"])

        if "property" in layout_data:
            if isinstance(layout_data["property"], list):
                creating_layout[0] += "("
                for properties in layout_data["property"]:
                    if properties["name"] == "propagate":
                        if properties["property"] == "False":
                            creating_layout.append("{}_propagate(0)".format(layout_data["manager"]))
                    elif properties["name"] != "propagate":
                        if creating_layout:
                            creating_layout[0] += "{}='{}', ".format(properties["name"],
                                                                     properties["property"])
                # Finally close ) of creating_layout[0]
                # Remove , and space from loop above
                creating_layout[0] = creating_layout[0][:-2] + ")"

            elif isinstance(layout_data["property"], dict):
                if layout_data["property"]["name"] == "propagate":
                    # If propagate = True
                    if layout_data["property"]["property"] == "True":
                        creating_layout[0] += "()"
                    # If propagate = False
                    elif layout_data["property"]["property"] == "False":
                        creating_layout[0] += "()"
                        creating_layout.append("{}_propagate(0)".format(layout_data["manager"]))
                # If name is not propagate
                elif layout_data["property"]["name"] != "propagate":
                    creating_layout[0] += "({}='{}')".format(layout_data["property"]["name"],
                                                             layout_data["property"]["property"])

        # If no properties for layout, then close args
        if not "property" in layout_data:
            creating_layout[0] += "()"

        # After fulfilling informations, returning the list
        return creating_layout

    def return_converted_list(self):
        '''
        This function returns self.returned_list
        '''

        return self.returned_list

if __name__ == '__main__':
    pass
