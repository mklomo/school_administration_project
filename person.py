"""
    This script implements the parent class for students and professors
"""

from address import Address


class Person:
    """
_first_name : str

_last_name : str

_date_of_birth : str

_phone_number : str

_address
    """

    def __init__(self, first_name, last_name, date_of_birth, phone_number, address):
        self._first_name = first_name
        self._last_name = last_name
        self._phone_number = phone_number
        self._date_of_birth = date_of_birth
        self._addresses = []
        # Note a Person can either have 1 or many addresses
        if isinstance(address, Address):
            self._address.append(address)

        elif isinstance(address, list):
            for entry_address in address:
                if not isinstance(entry_address, Address):
                    raise TypeError("Invalid Address...")
            self._address = address

        else:
            raise TypeError("Invalid Address..")

    def add_address(self, address):
        if not isinstance(address, Address):
            raise TypeError("Invalid Address...")
        else:
            self._address.append(address)

    def add_address_list(self, addresses):
        if isinstance(addresses, list):
            for entry_address in addresses:
                if not isinstance(entry_address, Address):
                    raise TypeError("Invalid Address...")

                self._address.append(entry_address)
