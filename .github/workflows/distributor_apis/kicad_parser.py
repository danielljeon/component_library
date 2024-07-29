"""KiCad custom library parsers.

"""

import os

from component_class import PCBComponent


def is_kicad_symbol_file(file_name: str) -> bool:
    """
    Determine if a given file is a KiCad symbol file.

    Args:
        file_name: The name of the file to check.

    Returns:
        bool: True if the file is a KiCad symbol file, False otherwise.
    """
    if file_name.endswith(".kicad_sym"):
        return True
    return False


def is_kicad_footprint_file(file_name: str) -> bool:
    """
    Determine if a given file is a KiCad footprint file.

    Args:
        file_name: The name of the file to check.

    Returns:
        bool: True if the file is a KiCad footprint file, False otherwise.
    """
    if file_name.endswith(".kicad_mod"):
        return True
    return False


def is_kicad_footprint_dir(directory: str) -> bool:
    """
    Determine if a given directory is a KiCad footprint directory.

    Args:
        directory: The name of the file to check.

    Returns:
        bool: True if the file is a KiCad footprint directory, False otherwise.
    """

    if directory.endswith(".pretty"):
        for root, dirs, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                if is_kicad_footprint_file(file_path):
                    return True
    return False


def find_kicad_libray_files(
    starting_dir: str = ".", exclude_dirs: list[str] = None
) -> dict[str, list[str]]:
    """Find all KiCad library files starting at a given directory.

    Args:
        starting_dir: Starting directory to search, defaults to current.
        exclude_dirs: List of directories to ignore.

    Returns:
        A dict with values of list os library files.
        Format:
        {
            "footprints": [],
            "symbols": [],
            ...
        }

    Notes:
        A maximum search directory search limit is set within the function.
    """

    def format_dict() -> dict[str, list[str]]:
        return {"footprints": footprint_files, "symbols": symbol_files}

    search_limit = 50  # Maximum number of directories to look in.

    if not isinstance(exclude_dirs, list):
        exclude_dirs = []  # Ensure a valid list.

    symbol_files = []
    footprint_files = []

    # Find all KiCad symbols in current directory.
    for i, (root, dirs, files) in enumerate(os.walk(starting_dir)):
        if i > search_limit:
            return format_dict()

        dirs[:] = [d for d in dirs if d not in exclude_dirs]  # Exclude dirs.

        for file in files:
            if not is_kicad_footprint_dir(root) and is_kicad_symbol_file(file):
                symbol_files.append(os.path.join(root, file))
            if is_kicad_footprint_dir(root) and is_kicad_footprint_file(file):
                footprint_files.append(os.path.join(root, file))

    return format_dict()


def parse_symbols() -> list[PCBComponent]:
    """Parse KiCad symbol files and create PCBComponent objects.

    Returns:
        List of PCBComponent objects.
    """
    symbols = []

    return symbols
