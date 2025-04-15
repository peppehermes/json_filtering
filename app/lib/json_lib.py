from lib.config_lib import get_keep_path, get_remove_path

def recursive_path(path: str, key: str) -> str:
    return f"{path}.{key}" if path else key

def should_keep(path: str, keep_path: list) -> bool:
    return any(k_path in path for k_path in keep_path)

def should_remove(path: str, remove_path: list) -> bool:
    return any(r_path in path for r_path in remove_path)

def pop_node(node: dict, key: str, path: str, keep_path: list, remove_path: list):
    if not should_keep(path, keep_path) and should_remove(path, remove_path):
        node.pop(key, None)

def filter_node(node: dict, key: str, val, path: str, keep_path: list, remove_path: list):
    path = recursive_path(path, key)

    if isinstance(val, list):
        for item in val:
            if isinstance(item, dict):
                for sub_key, sub_val in item.copy().items():
                    filter_node(item, sub_key, sub_val, path, keep_path, remove_path)
            else:
                pop_node(node, key, path, keep_path, remove_path)
    elif isinstance(val, dict):
        for sub_key, sub_val in val.copy().items():
            filter_node(val, sub_key, sub_val, path, keep_path, remove_path)
    else:
        pop_node(node, key, path, keep_path, remove_path)

def filter_json(json_data: dict, json_filter: dict) -> dict:
    """
    Filters a JSON object based on the provided filter data.
    Args:
        json_data (dict): The JSON object to be filtered.
        json_filter (dict): The filter data containing paths to keep or remove.
    Returns:
        dict: The filtered JSON object.
    """
    keep_path = get_keep_path(json_filter)
    remove_path = get_remove_path(json_filter)
    root_path = ""

    for key, val in json_data.copy().items():
        filter_node(json_data, key, val, root_path, keep_path, remove_path)

    return json_data
