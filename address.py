"""
    This script implements the address class for the school administration system
"""


class Address:
    """
This class keeps record of all the addresses of the Persons

country : str

state -> str

city -> str

street_address -> str

postal_code -> str

    """

    def __init__(self, country, state, city, street_address, postal_code):
        self._country = country
        self._state = state
        self._city = city
        self._street_address = street_address
        self._postal_code = postal_code
