from lib.json_lib import recursive_path, filter_json
import json

def test_recursive_path_empty_path():
    path = ""
    key = "key"
    expected = "key"
    assert recursive_path(path, key) == expected

def test_recursive_path_non_empty_path():
    path = "parent"
    key = "child"
    expected = "parent.child"
    assert recursive_path(path, key) == expected

def test_recursive_path_special_characters():
    path = "parent"
    key = "child@123"
    expected = "parent.child@123"
    assert recursive_path(path, key) == expected

def test_recursive_path_empty_key():
    path = "parent"
    key = ""
    expected = "parent."
    assert recursive_path(path, key) == expected

def test_recursive_path_empty_path_and_key():
    path = ""
    key = ""
    expected = ""
    assert recursive_path(path, key) == expected

def test_recursive_path_nested_keys():
    path = "parent.child"
    key = "grandchild"
    expected = "parent.child.grandchild"
    assert recursive_path(path, key) == expected

def test_filter_json():
    with open("app/tests/mock/data.json", "r") as data_file:
        json_data = json.load(data_file)

    with open("app/tests/mock/filter.json", "r") as filter_file:
        json_filter = json.load(filter_file)

    with open("app/tests/mock/output.json", "r") as output_file:
        expected_output = json.load(output_file)

    assert filter_json(json_data, json_filter) == expected_output