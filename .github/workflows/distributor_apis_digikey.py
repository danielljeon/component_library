"""DigiKey API Script.

Docs / Swagger Docs: https://developer.digikey.com/.

Notes:
    OAuth Callback needs to be set to https://localhost:8139/digikey_callback.
"""

import os

import requests

# Base API url.
BASE_URL = "https://api.digikey.com"

# Load environment variables.
API_CLIENT_ID = os.getenv("DIGIKEY_API_CLIENT_ID")
assert API_CLIENT_ID is not None, "Missing DIGIKEY_API_CLIENT_ID from env."
API_CLIENT_SECRET = os.getenv("DIGIKEY_API_CLIENT_SECRET")
assert (
    API_CLIENT_SECRET is not None
), "Missing DIGIKEY_API_CLIENT_SECRET from env."


class DigiKeyAPI:  # TODO: This is stupid OOP usage, maybe setup for structure.
    @staticmethod
    def get_new_bearer_token() -> tuple[str, int]:
        """Get a new bearer token for DigiKey APIs.

        Returns: A tuple with (bearer_token_str, lifetime_in_seconds).
        """
        # Prepare URL and params.
        url = f"https://api.digikey.com/v1/oauth2/token"

        # Prepare headers and POST request data payload.
        headers = {
            "accept": "application/json",
            "Content-Type": "application/x-www-form-urlencoded",
        }

        # Make the POST request.
        response = requests.post(
            url,
            headers=headers,
            data={
                "client_id": API_CLIENT_ID,
                "client_secret": API_CLIENT_SECRET,
                "grant_type": "client_credentials",
            },
        )

        # Check if the request was successful.
        if response.status_code == 200:
            if (
                "access_token" in response.json().keys()
                and "expires_in" in response.json().keys()
            ):
                return (
                    response.json()["access_token"],
                    response.json()["expires_in"],
                )

        else:
            raise RuntimeWarning(
                f"Failed to fetch data: {response.status_code}"
            )

    @staticmethod
    def search_part(
        bearer_token: str,
        part_number: str,
        locale: str = "CA",
        langauge: str = "en",
        currency: str = "CAD",
    ) -> dict:
        """Search for a part number on the DigiKey API.

        Args:
            bearer_token: DigiKey API bearer token.
            part_number: DigiKey part number to search for.
            locale: Country locale, defaults to "CA" (Canada).
            langauge: Langauge, defaults to "en" (English).
            currency: Country currency, defaults to "CAD" (Canadian Dollar).

        Returns: Dict json of API response.
        """
        # Prepare URL and params.
        url = f"{BASE_URL}/products/v4/search/{part_number}/productdetails"

        # Prepare headers and POST request data payload.
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Authorization": f"Bearer {bearer_token}",
            "X-DIGIKEY-Client-Id": API_CLIENT_ID,
            "X-DIGIKEY-Locale-Site": locale,
            "X-DIGIKEY-Locale-Language": langauge,
            "X-DIGIKEY-Locale-Currency": currency,
        }

        # Make the POST request.
        response = requests.get(url, headers=headers)

        # Check if the request was successful.
        if response.status_code == 200:
            return response.json()
        else:
            raise RuntimeWarning(
                f"Failed to fetch data: {response.status_code}"
            )
