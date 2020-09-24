import pytest

from builder.python_builder import ParseIntoCreate

class TestParseIntoCreate:

    def test_InitIsWorking(self):
        #This will test that __init__ is working properly
        parse = ParseIntoCreate("testdocument.py", "tests/file_xml_for_tests.ui")

        assert {'class': 'tk.Frame',
                'id': 'frame_1',
                'property': [{'name': 'height', 'property': '200'}, {'name': 'width', 'property': '200'}],
                'layout': {'manager': 'pack', 'property': [{'name': 'propagate', 'property': 'True'}, {'name': 'side', 'property': 'top'}]},
                'child': {'object': {'class': 'tk.Button',
                                     'id': 'button_1',
                                     'property': {'name': 'text',
                                                  'translatable': 'yes',
                                                  'property': 'button_1'},
                                     'layout': {'manager': 'pack',
                                                'property': [{'name': 'propagate', 'property': 'True'},
                                                             {'name': 'side', 'property': 'top'}
                                                            ]
                                               }
                                    }
                         }
               } == parse.realdict

    def test_InitClosesIfWrongDocument(self):
        # This test will show if class stops processus if given file isn't
        # in the good langage
        error_message = "The file you added isn't a .ui file. \n \
Consider reading the README.md file for more informations."

        assert error_message == ParseIntoCreate("testdocument.py", "builder/xml_converter.py")

