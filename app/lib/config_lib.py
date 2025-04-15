def get_keep_path(filter_data: dict):
    return [
        f"{remove_path}.{keep_sub_path}"
        for remove_path, keep_sub_path_list in filter_data.items()
        for keep_sub_path in keep_sub_path_list
    ]

def get_remove_path(filter_data: dict):
    return list(filter_data.keys())