from distributor_apis_digikey import DigiKeyAPI
from distributor_apis_mouser import MouserAPI


def test_mouser_part_number_search():
    # Mouser part number search.
    mouser_part_number = ""
    mouser_result = MouserAPI.search_part(part_number=mouser_part_number)
    assert isinstance(
        mouser_result, list
    ), "Mouser API part number search failed"


def test_digikey_part_number_search():
    # DigiKey OAuth bearer token request.
    token, lifetime = DigiKeyAPI.get_new_bearer_token()
    assert (
        isinstance(lifetime, int) and lifetime > 0
    ), "DigiKey API bearer token request failed"

    # DigiKey part number search.
    digikey_part_number = "qwerty123456"
    digikey_result = DigiKeyAPI.search_part(
        bearer_token=token, part_number=digikey_part_number
    )
    assert isinstance(
        digikey_result, list
    ), "DigiKey API part number search failed"
