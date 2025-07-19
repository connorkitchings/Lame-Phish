"""
Client for interacting with the elgoose.net API.

This module provides a client to fetch data related to Goose shows, setlists,
and songs. It handles the construction of API requests and returns the data
in a structured format.

[DOCS:elgoose.net API](https://elgoose.net/api/docs/)
"""

import requests


class ElGooseClient:
    """A client for the elgoose.net API."""

    BASE_URL = "https://elgoose.net/api/v2"

    def __init__(self):
        """Initializes the ElGooseClient."""
        pass

    def get_data(self, method: str, params: dict = None) -> dict:
        """Fetches data from a specified API method.

        Args:
            method: The API method to call (e.g., 'shows', 'setlists').
            params: A dictionary of query parameters.

        Returns:
            A dictionary containing the JSON response from the API.
        """
        url = f"{self.BASE_URL}/{method}.json"
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()  # Raise an exception for bad status codes
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None
