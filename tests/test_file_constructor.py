import pytest
import json

from builder.file_constructor import FileConstructor

class TestFileConstructor:

    def setup_method(self):
        self.ftest = FileConstructor()

    def test_create_stock_class(self):
        # test create_stock_class

        self.ftest.data = {"introduction": "{}"}
        assert self.ftest.create_stock_class("one") == "one"

    def test_create_class_and_init(self):
        #test create_class_and_init

        self.ftest.data = {"classcreation":"{}"}
        assert self.ftest.create_class_and_init("one") == "one"

    def test_create_class_no_arg(self):
        #test create_class_and_init with no arg

        self.ftest.data = {"classcreation": "{}"}
        assert self.ftest.create_class_and_init("") == ""

    def test_add_widget_func_to_init(self):
        # test add_main_widget_function_to_init
        # function
        self.ftest.data = {"addfunction":"{},{}"}
        assert self.ftest.add_main_widget_function_to_init("one") == "one,one"

    def test_add_widgets_to_master(self):
        # testing add_widgets_to_master_widgets_func

        self.ftest.data = {"addfuncmaster":"{},{}"}
        assert self.ftest.add_widgets_to_master_widgets_func("one") == "one,one"

    def test_add_master_function(self):
        # Testing add_master_function

        self.ftest.data = {"masterfunctionname":"{},{}"}
        assert self.ftest.add_master_function("one") == "one,one"

    def test_add_widgets_function(self):
        # Testing add_widgets_function

        self.ftest.data = {"widgetfunctionname":"{},{}"}
        assert self.ftest.add_widgets_function("one") == "one,one"

    def test_add_identify_id_class_master(self):
        # Testing add_identify_id_class_master

        self.ftest.data = {"functionidandclass":"{},{},{}"}
        assert self.ftest.add_identify_id_class_master("one", "two", "three") == "one,two,three"

    def test_add_widget_conf(self):
        # Testing add_widget_conf

        self.ftest.data = {"widgetconfig":"{},{}"}
        assert self.ftest.add_widget_conf("one", "two") == "one,two"

    def test_add_widget_loc(self):
        # Testing add_widget_loc

        self.ftest.data = {"widgetplace":"{},{}"}
        assert self.ftest.add_widget_loc("one", "two") == "one,two"

    def test_add_launch_function(self):
        # Testing add_launch_function

        self.ftest.data = {"launchfunction":"hey"}
        assert self.ftest.add_launch_function() == "hey"

    def test_add_name_eq_main(self):
        # Testing add_name_eq_main function

        self.ftest.data = {"ifnameeqmain":"hey"}
        assert self.ftest.add_name_eq_main() == "hey"

    def test_add_intro_conf(self):
        # Testing add_intro_conf function

        self.ftest.data = {"introconf":"{}"}
        assert self.ftest.add_intro_conf("one") == "one"

    def test_add_text(self):
        # Testing add_text function

        self.ftest.data = {"addtext":"{},{}"}
        assert self.ftest.add_text("one", "two") == "one,two"
