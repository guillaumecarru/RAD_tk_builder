'''
class taken from stackoverflow topic
https://stackoverflow.com/questions/2148119/how-to-convert-an-xml-string-to-a-dictionary
inspired by Adam Clark, wrote by "tiger"
Special thanks to him for letting me use it for my program
'''

class XmlDictConfig(dict):
    '''
    Note: need to add a root into if no exising
    Example usage:
    tree = ElementTree.parse('your_file.xml')
    root = tree.getroot()
    xmldict = XmlDictConfig(root)
    Or, if you want to use an XML string:
    root = ElementTree.XML(xml_string)
    xmldict = XmlDictConfig(root)
    And then use xmldict for what it is... a dict.
    '''
    def __init__(self, parent_element):
        if parent_element.items():
            self.updateShim( dict(parent_element.items()) )
        for element in parent_element:
            if len(element):
                aDict = XmlDictConfig(element)
            #   if element.items():
            #   aDict.updateShim(dict(element.items()))
                self.updateShim({element.tag: aDict})
            elif element.items():    # items() is specialy for attribtes
                elementattrib= element.items()
                if element.text:
                    elementattrib.append((element.tag,element.text ))     # add tag:text if there exist
                self.updateShim({element.tag: dict(elementattrib)})
            else:
                self.updateShim({element.tag: element.text})

    def updateShim (self, aDict ):
        for key in aDict.keys():   # keys() includes tag and attributes
            if key in self:
                value = self.pop(key)
                if type(value) is not list:
                    listOfDicts = []
                    listOfDicts.append(value)
                    listOfDicts.append(aDict[key])
                    self.update({key: listOfDicts})
                else:
                    value.append(aDict[key])
                    self.update({key: value})
            else:
                self.update({key:aDict[key]})  # it was self.update(aDict)

if __name__ == "__main__":
    import xml.etree.ElementTree as ET

    tree = ET.parse("tests/template_ui_file.ui")
    root = tree.getroot()

    xmldict = XmlDictConfig(root)

    print(" \n this is an example from tests/template_ui_file.ui file. You can \
take a look at it, for more informations of how it works. \n")
    print(xmldict)
