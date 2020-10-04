import pytest
from builder.recursive_packager import RecursivePackager

class TestRecursivePackager:
    '''
    Tests for RecursivePackager class
    '''

    def test_return_converted_list(self):
        # This tests return_converted_list function
        # is working properly
        dictio = {'class': 'tk.Frame', 'id': 'frame_1', 'property': [{'name': 'height', 'property': '200'}, {'name': 'width', 'property': '200'}], 'layout': {'manager': 'pack', 'property': [{'name': 'propagate', 'property': 'True'}, {'name': 'side', 'property': 'top'}]}, 'child': {'object': {'class': 'tk.Button', 'id': 'button_1', 'property': {'name': 'text', 'translatable': 'yes', 'property': 'button_1'}, 'layout': {'manager': 'pack', 'property': [{'name': 'propagate', 'property': 'True'}, {'name': 'side', 'property': 'top'}]}}}}
        testing = RecursivePackager(dictio)
        assert testing.return_converted_list() == [[[], 'frame_1', 'tk.Frame', ["(height='200', width='200')"], ["pack(side='top')"]], ['frame_1', 'button_1', 'tk.Button', ['(text={})', 'button_1'], ["pack(side='top')"]]]

    def test_creating_layout(self):
        # This tests creating_layout_valors function
        # is working properly with list and dict
        dictio = {'class': 'tk.Frame', 'id': 'frame_1', 'property': [{'name': 'height', 'property': '200'}, {'name': 'width', 'property': '200'}], 'layout': {'manager': 'pack', 'property': [{'name': 'propagate', 'property': 'True'}, {'name': 'side', 'property': 'top'}]}, 'child': {'object': {'class': 'tk.Button', 'id': 'button_1', 'property': {'name': 'text', 'translatable': 'yes', 'property': 'button_1'}, 'layout': {'manager': 'pack', 'property': [{'name': 'propagate', 'property': 'True'}, {'name': 'side', 'property': 'top'}]}}}}
        testing = RecursivePackager(dictio)
        # Testing layout_data list is working properly
        valors = {'manager': 'pack', 'property': [{'name': 'propagate', 'property': 'True'}, {'name': 'side', 'property': 'top'}]}
        assert testing.creating_layout_valors(valors) == ["pack(side='top')"]
        # Testing layout_data dict is working properly
        valors2 = {'manager': 'pack', 'property': {'name': 'propagate', 'property': 'True'}}
        assert testing.creating_layout_valors(valors2) == ["pack()"]

    def test_creating_layout_other_vals(self):
        # This tests creating_layout_valors function
        # is working properly with propagate list and dict
        dictio = {'class': 'tk.Frame', 'id': 'frame_1', 'property': [{'name': 'height', 'property': '200'}, {'name': 'width', 'property': '200'}], 'layout': {'manager': 'pack', 'property': [{'name': 'propagate', 'property': 'True'}, {'name': 'side', 'property': 'top'}]}, 'child': {'object': {'class': 'tk.Button', 'id': 'button_1', 'property': {'name': 'text', 'translatable': 'yes', 'property': 'button_1'}, 'layout': {'manager': 'pack', 'property': [{'name': 'propagate', 'property': 'True'}, {'name': 'side', 'property': 'top'}]}}}}
        testing = RecursivePackager(dictio)
        # Testing propagate_false is working with list
        valors = {'manager': 'pack', 'property': [{'name': 'propagate', 'property': 'False'}, {'name': 'side', 'property': 'top'}]}
        assert testing.creating_layout_valors(valors) == ["pack(side='top')",
                                                          "pack_propagate(0)"]
        # Testing propagate_false is working with dict
        valors2 = {'manager': 'pack', 'property': {'name': 'propagate',
                                                   'property': 'False'}}
        assert testing.creating_layout_valors(valors2) == ["pack()","pack_propagate(0)"]

    def test_creating_properties(self):
        # This tests creating_properties_valors function
        # is working properly
        dictio = {'class': 'tk.Frame', 'id': 'frame_1', 'property': [{'name': 'height', 'property': '200'}, {'name': 'width', 'property': '200'}], 'layout': {'manager': 'pack', 'property': [{'name': 'propagate', 'property': 'True'}, {'name': 'side', 'property': 'top'}]}, 'child': {'object': {'class': 'tk.Button', 'id': 'button_1', 'property': {'name': 'text', 'translatable': 'yes', 'property': 'button_1'}, 'layout': {'manager': 'pack', 'property': [{'name': 'propagate', 'property': 'True'}, {'name': 'side', 'property': 'top'}]}}}}
        testing = RecursivePackager(dictio)
        # Testing creating_properties list is working properly
        properties = [{'name': 'height', 'property': '200'}, {'name': 'width',
                                                              'property':
                                                              '200'}]
        assert testing.creating_properties_valors(properties) == ["(height='200', width='200')"]

        # Testing creating_properties dict is working properly
        properties2 = {'name': 'height', 'property': '200'}
        assert testing.creating_properties_valors(properties2) == ["(height='200')"]

    def test_creating_properties_text(self):
        # This tests creating_properties_valors function
        # is working properly with texts
        dictio = {'class': 'tk.Frame', 'id': 'frame_1', 'property': [{'name': 'height', 'property': '200'}, {'name': 'width', 'property': '200'}], 'layout': {'manager': 'pack', 'property': [{'name': 'propagate', 'property': 'True'}, {'name': 'side', 'property': 'top'}]}, 'child': {'object': {'class': 'tk.Button', 'id': 'button_1', 'property': {'name': 'text', 'translatable': 'yes', 'property': 'button_1'}, 'layout': {'manager': 'pack', 'property': [{'name': 'propagate', 'property': 'True'}, {'name': 'side', 'property': 'top'}]}}}}
        testing = RecursivePackager(dictio)
        # Testing creating_properties list is working properly
        properties = [{'name': 'text', 'property': 'oui'}, {'name': 'width',
                                                              'property':
                                                              '200'}]
        assert testing.creating_properties_valors(properties) == ["(text={}, width='200')", "oui"]

        # Testing creating_properties dict is working properly
        properties = {'name': 'text', 'property': 'oui'}
        assert testing.creating_properties_valors(properties) == ["(text={})", "oui"]

    def test_widget_compacter(self):
        # This tests widget_list_compacter function
        # is working properly with texts
        dictio = {'class': 'tk.Frame', 'id': 'frame_1', 'property': [{'name': 'height', 'property': '200'}, {'name': 'width', 'property': '200'}], 'layout': {'manager': 'pack', 'property': [{'name': 'propagate', 'property': 'True'}, {'name': 'side', 'property': 'top'}]}, 'child': {'object': {'class': 'tk.Button', 'id': 'button_1', 'property': {'name': 'text', 'translatable': 'yes', 'property': 'button_1'}, 'layout': {'manager': 'pack', 'property': [{'name': 'propagate', 'property': 'True'}, {'name': 'side', 'property': 'top'}]}}}}
        testing = RecursivePackager(dictio)
        dictio2 = {'class': 'tk.Frame',
                   'id': 'frame_1',
                   'property': [{'name': 'height', 'property': '200'}, {'name': 'width', 'property': '200'}],
                   'layout': {'manager': 'pack', 'property': [{'name': 'propagate', 'property': 'True'}, {'name': 'side', 'property': 'top'}]},
                   'child': {'object': {'class': 'tk.Button',
                                        'id': 'button_1',
                                        'property': {'name': 'text', 'translatable': 'yes', 'property': 'button_1'},
                                        'layout': {'manager': 'pack', 'property': [{'name': 'propagate', 'property': 'True'}, {'name': 'side', 'property': 'top'}]}}
                            }
                  }
        assert testing.widget_list_compacter(dictio2) == ["frame_1",
                                                          "tk.Frame",
                                                         ["(height='200', width='200')"],
                                                         ["pack(side='top')"]]
