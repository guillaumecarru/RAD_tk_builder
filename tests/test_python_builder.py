'''
Tests for ParseIntoCreate Class
'''

import pytest
from builder.python_builder import ParseIntoCreate



class TestParseIntoCreate:
    """Tests for ParseIntoCreate class."""
    def setup_method(self):
        self.parse = ParseIntoCreate("testdocument.py", "tests/file_xml_for_tests.ui")

    def test_init_is_working(self):
        # This will test that __init__ is working properly
        # Testing that xml_converter class is converting properly

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
               } == self.parse.realdict

    def test_init_launching_recursive(self):
        # This test makes sure __init__ is launching properly
        # recursive_packager once xml_converter created xmldict
        list_for_test = [
            [[], 'frame_1', 'tk.Frame', ["(height='200', width='200')"], ["pack(side='top')"]],
            ['frame_1', 'button_1', 'tk.Button', ['(text={})', 'button_1'], ["pack(side='top')"]]]


        assert list_for_test == self.parse.real_list

    def test_creating_new_dicts(self):
        # This test makes sure creating_new_dicts
        # fonctions properly

        assert isinstance(self.parse.realdict, dict)

    def test_getting_widgets(self):
        # This test makes sure getting_master_widgets
        # is working properly

        assert self.parse.getting_master_widgets() == [['frame_1', True]]

    def test_who_s_your_master(self):
        # Testing that who_s_your_master function
        # works properly with valor = True

        assert self.parse.who_s_your_master('frame_1', True) == [[[],
                                                                  'frame_1',
                                                                  'tk.Frame',
                                                                  ["(height='200', width='200')"],
                                                                  ["pack(side='top')"]]]

    def test_who_s_your_master_false(self):
        # Testing that who_s_your_master function
        # works properly with valor = False

        assert self.parse.who_s_your_master('frame_1') == [['frame_1',
                                                            'button_1',
                                                            'tk.Button',
                                                            ['(text={})', 'button_1'],
                                                            ["pack(side='top')"]]]

    def test_cap_text(self):
        # Testing cap_text function

        assert self.parse.cap_text("NtestIng") == "NTESTING_TEXT"

    def test_getting_master_widgets(self):
        # Making sure getting_master_widgets returns True and False statements
        # in returned lists

        newparse = ParseIntoCreate("newdocument.py")
        assert newparse.getting_master_widgets() == [['frame_2', True], ['labelframe_2', False]]

    def test_creating_conf_file_works(self, tmpdir, monkeypatch):
        # Making sure creating_conf_file is working properly

        # changing valors of self.constructor
        class FakeConstructor:
            def __init__(self):
                pass
            def add_intro_conf(self, arg1):
                return "{}\n".format(arg1)
            def add_text(self, arg1, arg2):
                return "{}:{}".format(arg1, arg2)

        monkeypatch.setattr("builder.python_builder.FileConstructor",
                            FakeConstructor)

        # setup class
        self.parse = ParseIntoCreate("newdocument.py")

        # Setup for test
        self.parse.conf_text = [["hello", "there"]]
        # Setup for fake file
        self.parse.newfile = "file.py"
        # Open in temp dir
        file = tmpdir.join("output.py")
        self.parse.defaultconf = file.strpath

        # Run creating_conf_file function
        self.parse.creating_conf_file()

        # Test if creating_conf_file executed properly
        assert file.read() == "file.py\nhello:there"

    def test_creating_new_file(self, tmpdir, monkeypatch, mocker):
        # Making sure creating_new_file is working properly

        # changing valors of self.constructor
        class FakeConstructor:
            def __init__(self):
                pass
            def create_stock_class(self, arg1):
                return "{}\n".format(arg1)

            def create_class_and_init(self, arg1):
                return "{}\n".format(arg1)

            def add_launch_function(self):
                return "function\n"

            def add_name_eq_main(self):
                return "name\n"

        # Attr FakeConstructor to python_builder
        monkeypatch.setattr("builder.python_builder.FileConstructor",
                            FakeConstructor)

        #setup class
        self.parse = ParseIntoCreate("newdocument.py")

        # mock getting_master_widgets and creating_conf_file
        mocker.patch("builder.python_builder.ParseIntoCreate.getting_master_widgets",
                     return_value=[])
        mocker.patch("builder.python_builder.ParseIntoCreate.creating_conf_file",
                     return_value="")

        # Setup for test
        self.parse.defaultconf = "minus3.py"
        # Open in temp dir
        file = tmpdir.join("file.py")
        self.parse.newfile = file.strpath

        # Run creating_new_file function
        self.parse.creating_new_file()

        # Test if creating_new_file renders informations properly
        assert file.read() == "minus3\ntext.TITLE\nfunction\nname\n"

    def test_creating_widgets_list(self, tmpdir, monkeypatch, mocker):
        # Making sure creating_new_file is working properly
        # Testing with widget_list has some valors,
        # One is False (first one), second is True
        # True one should appear twice in results

        # changing valors of self.constructor
        class FakeConstructor:
            def __init__(self):
                pass
            def create_stock_class(self, arg1):
                return "{}\n".format(arg1)

            def create_class_and_init(self, arg1):
                return "{}\n".format(arg1)

            def add_widgets_to_master_widgets_func(self, arg1):
                return "{}\n".format(arg1)

            def add_main_widget_function_to_init(self, arg1):
                return "mast{}\n".format(arg1)

            def add_launch_function(self):
                return "function\n"

            def add_name_eq_main(self):
                return "name\n"

        # Attr FakeConstructor to python_builder
        monkeypatch.setattr("builder.python_builder.FileConstructor",
                            FakeConstructor)

        #setup class
        self.parse = ParseIntoCreate("newdocument.py")

        # mock getting_master_widgets and creating_conf_file
        mocker.patch("builder.python_builder.ParseIntoCreate.getting_master_widgets",
                     return_value=[["FalseOne", False],["TrueOne", True]])
        mocker.patch("builder.python_builder.ParseIntoCreate.creating_conf_file",
                     return_value="")
        # Mock creating_function
        mocker.patch("builder.python_builder.ParseIntoCreate.creating_function",
                     return_value="")

        # Setup for test
        self.parse.defaultconf = "minus3.py"
        # Open in temp dir
        file = tmpdir.join("file.py")
        self.parse.newfile = file.strpath

        # Run creating_new_file function
        self.parse.creating_new_file()

        # Test if creating_new_file renders informations properly
        assert file.read() == "minus3\ntext.TITLE\nFalseOne\nmastTrueOne\nTrueOne\nfunction\nname\n"

    def test_creating_function(self, monkeypatch, tmpdir):
        # Testing creating_function function.
        # Makes sure it writes properly informations
        # first test with master = False

        # changing valors of self.constructor
        class FakeConstructor:
            def __init__(self):
                pass
            def add_widgets_function(self, arg1):
                return "{}\n".format(arg1)

            def add_identify_id_class_master(self, arg1, arg2, arg3=""):
                return "{},{},{}\n".format(arg1, arg2, arg3)

            def add_widget_conf(self, arg1, arg2):
                return "{},{}\n".format(arg1, arg2)

            def add_widget_loc(self, arg1, arg2):
                return "{},{}\n".format(arg1, arg2)

        # Attr FakeConstructor to python_builder
        monkeypatch.setattr("builder.python_builder.FileConstructor",
                            FakeConstructor)

        #setup class
        self.parse = ParseIntoCreate("newdocument.py")

        # Open in temp dir
        file = tmpdir.join("file.py")
        self.parse.newfile = file.strpath

        # list that's given as arg for creating_function
        inc_list = [["padre", "id", "class", ["notext"], ["nopropagate"]]]

        # open file to test function
        with open(file, "w") as fileinc:
            # Run creating_function function
            self.parse.creating_function(inc_list, fileinc)
        fileinc.close()

        # Test if creating_new_file renders informations properly
        assert file.read() == 'padre\nid,class,self.padre\nid,notext\nid,nopropagate\n\n'

    def test_creating_function_master(self, monkeypatch, tmpdir):
        # Testing creating_function function.
        # Makes sure it writes properly informations
        # Test with master = True
        # text = False
        # propagate = False

        # changing valors of self.constructor
        class FakeConstructor:
            def __init__(self):
                pass

            def add_master_function(self, arg1):
                return "{}\n".format(arg1)

            def add_widgets_function(self, arg1):
                return "{}\n".format(arg1)

            def add_identify_id_class_master(self, arg1, arg2, arg3=""):
                return "{},{},{}\n".format(arg1, arg2, arg3)

            def add_widget_conf(self, arg1, arg2):
                return "{},{}\n".format(arg1, arg2)

            def add_widget_loc(self, arg1, arg2):
                return "{},{}\n".format(arg1, arg2)

        # Attr FakeConstructor to python_builder
        monkeypatch.setattr("builder.python_builder.FileConstructor",
                            FakeConstructor)

        #setup class
        self.parse = ParseIntoCreate("newdocument.py")

        # Open in temp dir
        file = tmpdir.join("file.py")
        self.parse.newfile = file.strpath

        # list that's given as arg for creating_function
        inc_list = [["padre", "id", "class", ["notext"], ["grid", "propa"]]]

        # open file to test function
        with open(file, "w") as fileinc:
            # Run creating_function function
            self.parse.creating_function(inc_list, fileinc, True)
        fileinc.close()

        # Test if creating_new_file renders informations properly
        assert file.read() == 'id\nid,class,\nid,notext\nid,grid\nid,propa\n\n'
