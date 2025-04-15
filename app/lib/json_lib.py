from lib.config_lib import get_keep_path, get_remove_path

def recursive_path(path: str, key: str):
    if path == "":
        path = f"{key}"
    else:
        path = f"{path}.{key}"

    return path

def pop_node(node: dict, key: str, path: str, keep_path: list = [], remove_path: list = []):    
    for k_path in keep_path:
        if k_path in path:
            return
    
    for r_path in remove_path:
        if r_path in path:
            node.pop(key)
            return

def filter_node(node: dict, key: str, val: str, path: str, keep_path: list, remove_path: list):
    path = recursive_path(path, key)

    if isinstance(val, list):
        for item in val:
            for sub_key, sub_val in item.copy().items():
                filter_node(item, sub_key, sub_val, path, keep_path, remove_path)
    elif isinstance(val, dict):
        for sub_key, sub_val in val.copy().items():
            filter_node(val, sub_key, sub_val, path, keep_path, remove_path)
    else:
        # leaf node
        path = recursive_path(path, val)
        pop_node(node, key, path, keep_path, remove_path)

def filter_json(json_data: dict, json_filter: dict):
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

    for key, val in json_data.items():
        filter_node(node=json_data, key=key, val=val, path="", keep_path=keep_path, remove_path=remove_path)

    return json_data
