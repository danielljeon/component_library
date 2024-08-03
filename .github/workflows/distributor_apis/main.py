"""Custom KiCad library checker scripts.

Called as a GitHub actions script.
"""

from api_digikey import DigiKey
from api_mouser import Mouser
from kicad_parser import parse_library


def integrity_check():
    """Run integrity checks."""
    # Save running list of errors and risks found.
    errors = []
    risks = []

    # Parse the library files.
    library = parse_library(
        starting_dir=".", exclude_dirs=[".git", ".github", "venv", ".idea"]
    )

    # Current implementation just merges all types of components.
    library = [item for sublist in library.values() for item in sublist]

    # Create instances of API classes.
    digikey = DigiKey()
    mouser = Mouser()

    # Process each component found in the library.
    for component in library:
        api_result = None

        match component.distributor:
            case digikey.name:
                # DigiKey part number search.
                token, _ = digikey.get_new_bearer_token()
                api_result = digikey.search_part(
                    bearer_token=token,
                    part_number=component.distributor_part_number,
                )
            case mouser.name:
                # Mouser part number search.
                api_result = mouser.search_part(
                    part_number=component.distributor_part_number
                )
            case _:
                # Default.
                pass


def main():
    # integrity_check()
    pass


if __name__ == "__main__":
    main()
