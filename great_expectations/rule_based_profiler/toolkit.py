import os
from typing import Optional

from great_expectations.data_context.types.base import DataContextConfigDefaults


def default_profilers_exist(directory_path: Optional[str]) -> bool:
    if not directory_path:
        return False

    profilers_directory_path: str = os.path.join(
        directory_path,
        DataContextConfigDefaults.DEFAULT_PROFILER_STORE_BASE_DIRECTORY_RELATIVE_NAME.value,
    )
    return os.path.isdir(profilers_directory_path)
