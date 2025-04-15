from lib.json_lib import filter_json, FilterConfig, JsonFilter
import json

def test_filter_json():
    with open("app/tests/mock/data.json", "r") as data_file:
        json_data = json.load(data_file)

    with open("app/tests/mock/filter.json", "r") as filter_file:
        json_filter = json.load(filter_file)

    with open("app/tests/mock/output.json", "r") as output_file:
        expected_output = json.load(output_file)

    assert filter_json(json_data, json_filter) == expected_output

def test_filter_config():
    config = FilterConfig(keep_paths={"user", "settings.theme"}, remove_paths={"user.password", "temp"})

    assert config.should_keep("user.name") == True
    assert config.should_keep("settings.theme.color") == True
    assert config.should_keep("other.field") == False

    assert config.should_remove("user.password.hash") == True
    assert config.should_remove("temp.files") == True
    assert config.should_remove("other.field") == False

def test_build_path():
    json_filter = JsonFilter(FilterConfig(keep_paths=set(), remove_paths=set()))

    assert json_filter._build_path("", "key") == "key"
    assert json_filter._build_path("parent", "child") == "parent.child"
    assert json_filter._build_path("grand.parent", "child") == "grand.parent.child"

def test_simple_filtering():
    config = FilterConfig(
        keep_paths={"user.name"},
        remove_paths={"user.password", "temporary"}
    )
    json_filter = JsonFilter(config)

    data = {
        "user": {
            "name": "John",
            "password": "secret",
            "email": "john@example.com"
        },
        "temporary": {
            "cache": "data"
        }
    }

    expected = {
        "user": {
            "name": "John",
            "email": "john@example.com"
        }
    }

    assert json_filter.filter(data) == expected

def test_nested_structures():
    config = FilterConfig(
        keep_paths={"data.items.id", "data.items.visible"},
        remove_paths={"data.items"}
    )
    json_filter = JsonFilter(config)

    data = {
        "data": {
            "items": [
                {"id": 1, "secret": "hidden", "visible": True},
                {"id": 2, "secret": "hidden", "visible": False}
            ]
        }
    }

    expected = {
        "data": {
            "items": [
                {"id": 1, "visible": True},
                {"id": 2, "visible": False}
            ]
        }
    }

    assert json_filter.filter(data) == expected

def test_complex_filtering():
    config = FilterConfig(
        keep_paths={},
        remove_paths={"meta.internal", "data.public.secret", "data.private"}
    )
    json_filter = JsonFilter(config)

    data = {
        "meta": {
            "version": "1.0",
            "internal": {
                "debug": True
            }
        },
        "data": {
            "public": {
                "name": "Test",
                "secret": "hidden"
            },
            "private": {
                "key": "sensitive"
            }
        }
    }

    expected = {
        "meta": {
            "version": "1.0"
        },
        "data": {
            "public": {
                "name": "Test"
            }
        }
    }

    assert json_filter.filter(data) == expected