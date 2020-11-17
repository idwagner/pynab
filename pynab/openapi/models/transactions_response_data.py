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


class TransactionsResponseData(object):
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
        'transactions': 'list[TransactionDetail]',
        'server_knowledge': 'int'
    }

    attribute_map = {
        'transactions': 'transactions',
        'server_knowledge': 'server_knowledge'
    }

    def __init__(self, transactions=None, server_knowledge=None, local_vars_configuration=None):  # noqa: E501
        """TransactionsResponseData - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._transactions = None
        self._server_knowledge = None
        self.discriminator = None

        self.transactions = transactions
        self.server_knowledge = server_knowledge

    @property
    def transactions(self):
        """Gets the transactions of this TransactionsResponseData.  # noqa: E501


        :return: The transactions of this TransactionsResponseData.  # noqa: E501
        :rtype: list[TransactionDetail]
        """
        return self._transactions

    @transactions.setter
    def transactions(self, transactions):
        """Sets the transactions of this TransactionsResponseData.


        :param transactions: The transactions of this TransactionsResponseData.  # noqa: E501
        :type transactions: list[TransactionDetail]
        """
        if self.local_vars_configuration.client_side_validation and transactions is None:  # noqa: E501
            raise ValueError("Invalid value for `transactions`, must not be `None`")  # noqa: E501

        self._transactions = transactions

    @property
    def server_knowledge(self):
        """Gets the server_knowledge of this TransactionsResponseData.  # noqa: E501

        The knowledge of the server  # noqa: E501

        :return: The server_knowledge of this TransactionsResponseData.  # noqa: E501
        :rtype: int
        """
        return self._server_knowledge

    @server_knowledge.setter
    def server_knowledge(self, server_knowledge):
        """Sets the server_knowledge of this TransactionsResponseData.

        The knowledge of the server  # noqa: E501

        :param server_knowledge: The server_knowledge of this TransactionsResponseData.  # noqa: E501
        :type server_knowledge: int
        """
        if self.local_vars_configuration.client_side_validation and server_knowledge is None:  # noqa: E501
            raise ValueError("Invalid value for `server_knowledge`, must not be `None`")  # noqa: E501

        self._server_knowledge = server_knowledge

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
        if not isinstance(other, TransactionsResponseData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TransactionsResponseData):
            return True

        return self.to_dict() != other.to_dict()
