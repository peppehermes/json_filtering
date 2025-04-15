from dataclasses import dataclass
from typing import Any, Dict, List, Set
from lib.config_lib import get_keep_path, get_remove_path

@dataclass
class FilterConfig:
    keep_paths: Set[str]
    remove_paths: Set[str]

    def should_keep(self, path: str) -> bool:
        return any(path.startswith(k_path) for k_path in self.keep_paths)
    
    def should_remove(self, path: str) -> bool:
        return any(path.startswith(r_path) for r_path in self.remove_paths)

class JsonFilter:
    def __init__(self, config: FilterConfig):
        self.config = config

    def _build_path(self, parent: str, key: str) -> str:
        return f"{parent}.{key}" if parent else key

    def _should_remove_field(self, path: str) -> bool:
        return not self.config.should_keep(path) and self.config.should_remove(path)

    def _process_node(self, node: Any, path: str, json_node: Dict[str, Any], key: str) -> None:
        if isinstance(node, dict):
            self._filter_dict(node, path)
            if not node:
                json_node.pop(key)
        elif isinstance(node, list):
            self._filter_list(node, path)
        elif self._should_remove_field(path):
            json_node.pop(key)

    def _filter_list(self, items: List[Any], parent_path: str) -> None:
        for item in items:
            if isinstance(item, dict):
                self._filter_dict(item, parent_path)

    def _filter_dict(self, json_node: Dict[str, Any], parent_path: str = "") -> None:
        for key, node in list(json_node.items()):
            current_path = self._build_path(parent_path, key)
            self._process_node(node, current_path, json_node, key)

    def filter(self, data: Dict[str, Any]) -> Dict[str, Any]:
        filtered_data = data.copy()
        self._filter_dict(filtered_data)
        return filtered_data

def filter_json(json_data: Dict[str, Any], json_filter: Dict[str, List[str]]) -> Dict[str, Any]:
    config = FilterConfig(
        keep_paths=set(get_keep_path(json_filter)),
        remove_paths=set(get_remove_path(json_filter))
    )

    return JsonFilter(config).filter(json_data)
