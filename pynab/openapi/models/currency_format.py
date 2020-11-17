# coding: utf-8

"""
    YNAB API Endpoints

    Our API uses a REST based design, leverages the JSON data format, and relies upon HTTPS for transport. We respond with meaningful HTTP response codes and if an error occurs, we include error details in the response body.  API Documentation is at https://api.youneedabudget.com  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import inspect
import pprint
import re  # noqa: F401
import six

from pynab.openapi.configuration import Configuration


class CurrencyFormat(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'iso_code': 'str',
        'example_format': 'str',
        'decimal_digits': 'int',
        'decimal_separator': 'str',
        'symbol_first': 'bool',
        'group_separator': 'str',
        'currency_symbol': 'str',
        'display_symbol': 'bool'
    }

    attribute_map = {
        'iso_code': 'iso_code',
        'example_format': 'example_format',
        'decimal_digits': 'decimal_digits',
        'decimal_separator': 'decimal_separator',
        'symbol_first': 'symbol_first',
        'group_separator': 'group_separator',
        'currency_symbol': 'currency_symbol',
        'display_symbol': 'display_symbol'
    }

    def __init__(self, iso_code=None, example_format=None, decimal_digits=None, decimal_separator=None, symbol_first=None, group_separator=None, currency_symbol=None, display_symbol=None, local_vars_configuration=None):  # noqa: E501
        """CurrencyFormat - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._iso_code = None
        self._example_format = None
        self._decimal_digits = None
        self._decimal_separator = None
        self._symbol_first = None
        self._group_separator = None
        self._currency_symbol = None
        self._display_symbol = None
        self.discriminator = None

        self.iso_code = iso_code
        self.example_format = example_format
        self.decimal_digits = decimal_digits
        self.decimal_separator = decimal_separator
        self.symbol_first = symbol_first
        self.group_separator = group_separator
        self.currency_symbol = currency_symbol
        self.display_symbol = display_symbol

    @property
    def iso_code(self):
        """Gets the iso_code of this CurrencyFormat.  # noqa: E501


        :return: The iso_code of this CurrencyFormat.  # noqa: E501
        :rtype: str
        """
        return self._iso_code

    @iso_code.setter
    def iso_code(self, iso_code):
        """Sets the iso_code of this CurrencyFormat.


        :param iso_code: The iso_code of this CurrencyFormat.  # noqa: E501
        :type iso_code: str
        """
        if self.local_vars_configuration.client_side_validation and iso_code is None:  # noqa: E501
            raise ValueError("Invalid value for `iso_code`, must not be `None`")  # noqa: E501

        self._iso_code = iso_code

    @property
    def example_format(self):
        """Gets the example_format of this CurrencyFormat.  # noqa: E501


        :return: The example_format of this CurrencyFormat.  # noqa: E501
        :rtype: str
        """
        return self._example_format

    @example_format.setter
    def example_format(self, example_format):
        """Sets the example_format of this CurrencyFormat.


        :param example_format: The example_format of this CurrencyFormat.  # noqa: E501
        :type example_format: str
        """
        if self.local_vars_configuration.client_side_validation and example_format is None:  # noqa: E501
            raise ValueError("Invalid value for `example_format`, must not be `None`")  # noqa: E501

        self._example_format = example_format

    @property
    def decimal_digits(self):
        """Gets the decimal_digits of this CurrencyFormat.  # noqa: E501


        :return: The decimal_digits of this CurrencyFormat.  # noqa: E501
        :rtype: int
        """
        return self._decimal_digits

    @decimal_digits.setter
    def decimal_digits(self, decimal_digits):
        """Sets the decimal_digits of this CurrencyFormat.


        :param decimal_digits: The decimal_digits of this CurrencyFormat.  # noqa: E501
        :type decimal_digits: int
        """
        if self.local_vars_configuration.client_side_validation and decimal_digits is None:  # noqa: E501
            raise ValueError("Invalid value for `decimal_digits`, must not be `None`")  # noqa: E501

        self._decimal_digits = decimal_digits

    @property
    def decimal_separator(self):
        """Gets the decimal_separator of this CurrencyFormat.  # noqa: E501


        :return: The decimal_separator of this CurrencyFormat.  # noqa: E501
        :rtype: str
        """
        return self._decimal_separator

    @decimal_separator.setter
    def decimal_separator(self, decimal_separator):
        """Sets the decimal_separator of this CurrencyFormat.


        :param decimal_separator: The decimal_separator of this CurrencyFormat.  # noqa: E501
        :type decimal_separator: str
        """
        if self.local_vars_configuration.client_side_validation and decimal_separator is None:  # noqa: E501
            raise ValueError("Invalid value for `decimal_separator`, must not be `None`")  # noqa: E501

        self._decimal_separator = decimal_separator

    @property
    def symbol_first(self):
        """Gets the symbol_first of this CurrencyFormat.  # noqa: E501


        :return: The symbol_first of this CurrencyFormat.  # noqa: E501
        :rtype: bool
        """
        return self._symbol_first

    @symbol_first.setter
    def symbol_first(self, symbol_first):
        """Sets the symbol_first of this CurrencyFormat.


        :param symbol_first: The symbol_first of this CurrencyFormat.  # noqa: E501
        :type symbol_first: bool
        """
        if self.local_vars_configuration.client_side_validation and symbol_first is None:  # noqa: E501
            raise ValueError("Invalid value for `symbol_first`, must not be `None`")  # noqa: E501

        self._symbol_first = symbol_first

    @property
    def group_separator(self):
        """Gets the group_separator of this CurrencyFormat.  # noqa: E501


        :return: The group_separator of this CurrencyFormat.  # noqa: E501
        :rtype: str
        """
        return self._group_separator

    @group_separator.setter
    def group_separator(self, group_separator):
        """Sets the group_separator of this CurrencyFormat.


        :param group_separator: The group_separator of this CurrencyFormat.  # noqa: E501
        :type group_separator: str
        """
        if self.local_vars_configuration.client_side_validation and group_separator is None:  # noqa: E501
            raise ValueError("Invalid value for `group_separator`, must not be `None`")  # noqa: E501

        self._group_separator = group_separator

    @property
    def currency_symbol(self):
        """Gets the currency_symbol of this CurrencyFormat.  # noqa: E501


        :return: The currency_symbol of this CurrencyFormat.  # noqa: E501
        :rtype: str
        """
        return self._currency_symbol

    @currency_symbol.setter
    def currency_symbol(self, currency_symbol):
        """Sets the currency_symbol of this CurrencyFormat.


        :param currency_symbol: The currency_symbol of this CurrencyFormat.  # noqa: E501
        :type currency_symbol: str
        """
        if self.local_vars_configuration.client_side_validation and currency_symbol is None:  # noqa: E501
            raise ValueError("Invalid value for `currency_symbol`, must not be `None`")  # noqa: E501

        self._currency_symbol = currency_symbol

    @property
    def display_symbol(self):
        """Gets the display_symbol of this CurrencyFormat.  # noqa: E501


        :return: The display_symbol of this CurrencyFormat.  # noqa: E501
        :rtype: bool
        """
        return self._display_symbol

    @display_symbol.setter
    def display_symbol(self, display_symbol):
        """Sets the display_symbol of this CurrencyFormat.


        :param display_symbol: The display_symbol of this CurrencyFormat.  # noqa: E501
        :type display_symbol: bool
        """
        if self.local_vars_configuration.client_side_validation and display_symbol is None:  # noqa: E501
            raise ValueError("Invalid value for `display_symbol`, must not be `None`")  # noqa: E501

        self._display_symbol = display_symbol

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = inspect.getargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CurrencyFormat):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CurrencyFormat):
            return True

        return self.to_dict() != other.to_dict()
