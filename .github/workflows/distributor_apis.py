"""Custom KiCad library checker scripts.

Called as a GitHub actions script.
"""

# TODO: Uncomment and add API module functions.
# from distributor_apis_digikey import DigiKeyAPI
# from distributor_apis_mouser import MouserAPI


def main():
    # TODO: Develop script to parse component data.
    # mouser_part_number = "511-STM32L432KCU6"
    # digikey_part_number = "497-16578-ND"
    #
    # # Mouser part number search.
    # mouser_result = MouserAPI.search_part(part_number=mouser_part_number)
    # print(mouser_result)
    #
    # # DigiKey part number search.
    # token, _ = DigiKeyAPI.get_new_bearer_token()  # Return includes lifespan.
    # digikey_result = DigiKeyAPI.search_part(
    #     bearer_token=token, part_number=digikey_part_number
    # )
    # print(digikey_result)

    pass


if __name__ == "__main__":
    main()
