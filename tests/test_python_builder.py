import pytest
from builder.python_builder import ParseIntoCreate

class TestParseIntoCreate:
    '''
    Tests for ParseIntoCreate class
    '''

    def test_init_is_working(self):
        # This will test that __init__ is working properly
        # Testing that xml_converter class is converting properly
        parse = ParseIntoCreate("testdocument.py", "tests/file_xml_for_tests.ui")

        assert {'class': 'tk.Frame',
                'id': 'frame_1',
                'property': [{'name': 'height', 'property': '200'},
                             {'name': 'width', 'property': '200'}],
                'layout': {'manager': 'pack', 'property':
                           [{'name': 'propagate', 'property': 'True'},
                            {'name': 'side', 'property': 'top'}]},
                'child': {'object': {'class': 'tk.Button',
                                     'id': 'button_1',
                                     'property': {'name': 'text',
                                                  'translatable': 'yes',
                                                  'property': 'button_1'},
                                     'layout': {'manager': 'pack',
                                                'property':
                                                [{'name': 'propagate', 'property': 'True'},
                                                 {'name': 'side', 'property': 'top'}
                                                ]
                                               }
                                    }
                         }
               } == parse.realdict

    def test_init_launching_recursive(self):
        # This test makes sure __init__ is launching properly
        # recursive_packager once xml_converter created xmldict
        list_for_test = [
            [[], 'frame_1', 'tk.Frame', ["(height='200', width='200')"], ["pack(side='top')"]],
            ['frame_1', 'button_1', 'tk.Button', ['(text={})', 'button_1'], ["pack(side='top')"]]]

        parse = ParseIntoCreate("testdocument.py", "tests/file_xml_for_tests.ui")

        assert list_for_test == parse.real_list

    def test_creating_new_dicts(self):
        # This test makes sure creating_new_dicts
        # fonctions properly

        parse = ParseIntoCreate("testdocument.py", "tests/file_xml_for_tests.ui")
        assert type(parse.realdict) is dict

    def test_getting_widgets(self):
        # This test makes sure getting_master_widgets
        # is working properly

        parse = ParseIntoCreate("testdocument.py", "tests/file_xml_for_tests.ui")
        assert parse.getting_master_widgets() == [['frame_1', True]]

    ###############
    # Important
    # Tests that need to be created when functions are done :
    # creating_functions_for_new_file
    # creating_new_file
    ##############
