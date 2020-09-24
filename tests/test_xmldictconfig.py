import pytest
import xml.etree.ElementTree as ET

from builder.xml_converter import XmlDictConfig

class TestOnXmlDictConfig():

    def test_returnsProperResult(self):
        tree = ET.parse("tests/file_xml_for_tests.ui")
        root = tree.getroot()

        xmldict = XmlDictConfig(root)

        assert{'class': 'tk.Frame', 'id': 'frame_1', 'property': [{'name':
                                                                   'height',
                                                                   'property':
                                                                   '200'},
                                                                  {'name':
                                                                   'width',
                                                                   'property':
                                                                   '200'}],
               'layout': {'manager': 'pack', 'property': [{'name': 'propagate',
                                                           'property': 'True'},
                                                          {'name': 'side',
                                                           'property':
                                                           'top'}]}, 'child':
               {'object': {'class': 'tk.Button', 'id': 'button_1', 'property':
                           {'name': 'text', 'translatable': 'yes', 'property':
                            'button_1'}, 'layout': {'manager': 'pack',
                                                    'property': [{'name':
                                                                  'propagate',
                                                                  'property':
                                                                  'True'},
                                                                 {'name':
                                                                  'side',
                                                                  'property':
                                                                  'top'}]}}}} == xmldict["object"]


if __name__ == "__main__":
    pytest.main()
