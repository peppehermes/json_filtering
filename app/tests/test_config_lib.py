from lib.config_lib import get_keep_path, get_remove_path

def test_get_remove_path_empty_dict():
    filter_data = {}
    expected = []
    assert get_remove_path(filter_data) == expected

def test_get_remove_path_single_key():
    filter_data = {"x": ["y"]}
    expected = ["x"]
    assert get_remove_path(filter_data) == expected

def test_get_remove_path_multiple_keys():
    filter_data = {"a": ["b", "c"], "d": ["e", "f"]}
    expected = ["a", "d"]
    assert get_remove_path(filter_data) == expected

def test_get_keep_path_multiple_keys():
    filter_data = {"a": ["b", "c"], "d": ["e", "f"]}
    expected = ["a.b", "a.c", "d.e", "d.f"]
    assert get_keep_path(filter_data) == expected

def test_get_keep_path_empty_sub_path():
    filter_data = {"a.b": []}
    expected = []
    assert get_keep_path(filter_data) == expected

def test_get_keep_path_empty_dict():
    filter_data = {}
    expected = []
    assert get_keep_path(filter_data) == expected

def test_get_keep_path_single_key():
    filter_data = {"x": ["y"]}
    expected = ["x.y"]
    assert get_keep_path(filter_data) == expected