import pytest
import json

from builder.file_constructor import FileConstructor

#read_data = json.dumps({"introduction":"{}",
#                        "classcreation":"{}",
#                        "addfunction":"{}{}"
#                       })
#mock_open = mock.mock_open(read_data = read_data)
ftest = FileConstructor()

class TestFileConstructor:

    def test_create_stock_class(self):
        # test create_stock_class

        assert ftest.create_stock_class("one") == "import tkinter as tk\n\
\n# all strings are located in that file\nimport {} as text\n".format("one")

    def test_create_class_and_init(self):
        #test create_class_and_init

        assert ftest.create_class_and_init("one") == "\nclass \
ConvertedFile(tk.Tk):\n    \"\"\"To activate this tkinter window, \
instanciate it, then use the launch() function on\n    your \
object\"\"\"\n\n    def __init__(self):\n        # Building main \
window\n        tk.Tk.__init__(self)\n        \
self.title({})\n\n".format("one")

    def test_add_widget_func_to_init(self):
        # test add_main_widget_function_to_init
        # function

        assert ftest.add_main_widget_function_to_init("one") == "        # Add \
self.{} as master\n        self.add_{}()\n\n".format("one","one")
