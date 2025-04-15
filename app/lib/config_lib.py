def get_keep_path(filter_data: dict):
    """
    Converts filter data to a list of paths to keep.
    Args:
        filter_data (dict): The filter data containing paths to keep.
    Returns:
        list: A list of paths to keep.
    """
    return [
        f"{filter_path}.{k_sub_path}"
        for filter_path, k_sub_path_list in filter_data.items()
        for k_sub_path in k_sub_path_list
    ]

def get_remove_path(filter_data: dict):
    """
    Converts filter data to a list of paths to remove.
    Args:
        filter_data (dict): The filter data containing paths to remove.
    Returns:
        list: A list of paths to remove.
    """
    return list(filter_data.keys())