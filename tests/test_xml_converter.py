import os
import sys

import unittest
import xml.etree.ElementTree as ET

main_app_dir =os.path.abspath(os.path.dirname(os.path.dirname(os.path.realpath(sys.argv[0]))))

if main_app_dir not in sys.path:
    sys.path.insert(0, main_app_dir)

from builder.xml_converter import XmlDictConfig

class TestXmlDictConfig(unittest.TestCase):
    def setUp(self):
        self.filexml = "file_xml_for_tests.ui"
        self.objectfilexml = {'class': 'tk.Frame', 'id': 'frame_1', 'property': [{'name': 'height', 'property': '200'}, {'name': 'width', 'property': '200'}], 'layout': {'manager': 'pack', 'property': [{'name': 'propagate', 'property': 'True'}, {'name': 'side', 'property': 'top'}]}, 'child': {'object': {'class': 'tk.Button', 'id': 'button_1', 'property': {'name': 'text', 'translatable': 'yes', 'property': 'button_1'}, 'layout': {'manager': 'pack', 'property': [{'name': 'propagate', 'property': 'True'}, {'name': 'side', 'property': 'top'}]}}}}

    def test_returnsProperResult(self):
        tree = ET.parse(self.filexml)
        root = tree.getroot()

        xmldict = XmlDictConfig(root)
        self.assertEqual(self.objectfilexml, root["object"])

if __name__ == "__main__":
    unittest.main()
