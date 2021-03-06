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


class BudgetDetail(object):
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
        'id': 'str',
        'name': 'str',
        'last_modified_on': 'datetime',
        'first_month': 'date',
        'last_month': 'date',
        'date_format': 'DateFormat',
        'currency_format': 'CurrencyFormat',
        'accounts': 'list[Account]',
        'payees': 'list[Payee]',
        'payee_locations': 'list[PayeeLocation]',
        'category_groups': 'list[CategoryGroup]',
        'categories': 'list[Category]',
        'months': 'list[MonthDetail]',
        'transactions': 'list[TransactionSummary]',
        'subtransactions': 'list[SubTransaction]',
        'scheduled_transactions': 'list[ScheduledTransactionSummary]',
        'scheduled_subtransactions': 'list[ScheduledSubTransaction]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'last_modified_on': 'last_modified_on',
        'first_month': 'first_month',
        'last_month': 'last_month',
        'date_format': 'date_format',
        'currency_format': 'currency_format',
        'accounts': 'accounts',
        'payees': 'payees',
        'payee_locations': 'payee_locations',
        'category_groups': 'category_groups',
        'categories': 'categories',
        'months': 'months',
        'transactions': 'transactions',
        'subtransactions': 'subtransactions',
        'scheduled_transactions': 'scheduled_transactions',
        'scheduled_subtransactions': 'scheduled_subtransactions'
    }

    def __init__(self, id=None, name=None, last_modified_on=None, first_month=None, last_month=None, date_format=None, currency_format=None, accounts=None, payees=None, payee_locations=None, category_groups=None, categories=None, months=None, transactions=None, subtransactions=None, scheduled_transactions=None, scheduled_subtransactions=None, local_vars_configuration=None):  # noqa: E501
        """BudgetDetail - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._last_modified_on = None
        self._first_month = None
        self._last_month = None
        self._date_format = None
        self._currency_format = None
        self._accounts = None
        self._payees = None
        self._payee_locations = None
        self._category_groups = None
        self._categories = None
        self._months = None
        self._transactions = None
        self._subtransactions = None
        self._scheduled_transactions = None
        self._scheduled_subtransactions = None
        self.discriminator = None

        self.id = id
        self.name = name
        if last_modified_on is not None:
            self.last_modified_on = last_modified_on
        if first_month is not None:
            self.first_month = first_month
        if last_month is not None:
            self.last_month = last_month
        if date_format is not None:
            self.date_format = date_format
        if currency_format is not None:
            self.currency_format = currency_format
        if accounts is not None:
            self.accounts = accounts
        if payees is not None:
            self.payees = payees
        if payee_locations is not None:
            self.payee_locations = payee_locations
        if category_groups is not None:
            self.category_groups = category_groups
        if categories is not None:
            self.categories = categories
        if months is not None:
            self.months = months
        if transactions is not None:
            self.transactions = transactions
        if subtransactions is not None:
            self.subtransactions = subtransactions
        if scheduled_transactions is not None:
            self.scheduled_transactions = scheduled_transactions
        if scheduled_subtransactions is not None:
            self.scheduled_subtransactions = scheduled_subtransactions

    @property
    def id(self):
        """Gets the id of this BudgetDetail.  # noqa: E501


        :return: The id of this BudgetDetail.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BudgetDetail.


        :param id: The id of this BudgetDetail.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this BudgetDetail.  # noqa: E501


        :return: The name of this BudgetDetail.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BudgetDetail.


        :param name: The name of this BudgetDetail.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def last_modified_on(self):
        """Gets the last_modified_on of this BudgetDetail.  # noqa: E501

        The last time any changes were made to the budget from either a web or mobile client  # noqa: E501

        :return: The last_modified_on of this BudgetDetail.  # noqa: E501
        :rtype: datetime
        """
        return self._last_modified_on

    @last_modified_on.setter
    def last_modified_on(self, last_modified_on):
        """Sets the last_modified_on of this BudgetDetail.

        The last time any changes were made to the budget from either a web or mobile client  # noqa: E501

        :param last_modified_on: The last_modified_on of this BudgetDetail.  # noqa: E501
        :type last_modified_on: datetime
        """

        self._last_modified_on = last_modified_on

    @property
    def first_month(self):
        """Gets the first_month of this BudgetDetail.  # noqa: E501

        The earliest budget month  # noqa: E501

        :return: The first_month of this BudgetDetail.  # noqa: E501
        :rtype: date
        """
        return self._first_month

    @first_month.setter
    def first_month(self, first_month):
        """Sets the first_month of this BudgetDetail.

        The earliest budget month  # noqa: E501

        :param first_month: The first_month of this BudgetDetail.  # noqa: E501
        :type first_month: date
        """

        self._first_month = first_month

    @property
    def last_month(self):
        """Gets the last_month of this BudgetDetail.  # noqa: E501

        The latest budget month  # noqa: E501

        :return: The last_month of this BudgetDetail.  # noqa: E501
        :rtype: date
        """
        return self._last_month

    @last_month.setter
    def last_month(self, last_month):
        """Sets the last_month of this BudgetDetail.

        The latest budget month  # noqa: E501

        :param last_month: The last_month of this BudgetDetail.  # noqa: E501
        :type last_month: date
        """

        self._last_month = last_month

    @property
    def date_format(self):
        """Gets the date_format of this BudgetDetail.  # noqa: E501


        :return: The date_format of this BudgetDetail.  # noqa: E501
        :rtype: DateFormat
        """
        return self._date_format

    @date_format.setter
    def date_format(self, date_format):
        """Sets the date_format of this BudgetDetail.


        :param date_format: The date_format of this BudgetDetail.  # noqa: E501
        :type date_format: DateFormat
        """

        self._date_format = date_format

    @property
    def currency_format(self):
        """Gets the currency_format of this BudgetDetail.  # noqa: E501


        :return: The currency_format of this BudgetDetail.  # noqa: E501
        :rtype: CurrencyFormat
        """
        return self._currency_format

    @currency_format.setter
    def currency_format(self, currency_format):
        """Sets the currency_format of this BudgetDetail.


        :param currency_format: The currency_format of this BudgetDetail.  # noqa: E501
        :type currency_format: CurrencyFormat
        """

        self._currency_format = currency_format

    @property
    def accounts(self):
        """Gets the accounts of this BudgetDetail.  # noqa: E501


        :return: The accounts of this BudgetDetail.  # noqa: E501
        :rtype: list[Account]
        """
        return self._accounts

    @accounts.setter
    def accounts(self, accounts):
        """Sets the accounts of this BudgetDetail.


        :param accounts: The accounts of this BudgetDetail.  # noqa: E501
        :type accounts: list[Account]
        """

        self._accounts = accounts

    @property
    def payees(self):
        """Gets the payees of this BudgetDetail.  # noqa: E501


        :return: The payees of this BudgetDetail.  # noqa: E501
        :rtype: list[Payee]
        """
        return self._payees

    @payees.setter
    def payees(self, payees):
        """Sets the payees of this BudgetDetail.


        :param payees: The payees of this BudgetDetail.  # noqa: E501
        :type payees: list[Payee]
        """

        self._payees = payees

    @property
    def payee_locations(self):
        """Gets the payee_locations of this BudgetDetail.  # noqa: E501


        :return: The payee_locations of this BudgetDetail.  # noqa: E501
        :rtype: list[PayeeLocation]
        """
        return self._payee_locations

    @payee_locations.setter
    def payee_locations(self, payee_locations):
        """Sets the payee_locations of this BudgetDetail.


        :param payee_locations: The payee_locations of this BudgetDetail.  # noqa: E501
        :type payee_locations: list[PayeeLocation]
        """

        self._payee_locations = payee_locations

    @property
    def category_groups(self):
        """Gets the category_groups of this BudgetDetail.  # noqa: E501


        :return: The category_groups of this BudgetDetail.  # noqa: E501
        :rtype: list[CategoryGroup]
        """
        return self._category_groups

    @category_groups.setter
    def category_groups(self, category_groups):
        """Sets the category_groups of this BudgetDetail.


        :param category_groups: The category_groups of this BudgetDetail.  # noqa: E501
        :type category_groups: list[CategoryGroup]
        """

        self._category_groups = category_groups

    @property
    def categories(self):
        """Gets the categories of this BudgetDetail.  # noqa: E501


        :return: The categories of this BudgetDetail.  # noqa: E501
        :rtype: list[Category]
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        """Sets the categories of this BudgetDetail.


        :param categories: The categories of this BudgetDetail.  # noqa: E501
        :type categories: list[Category]
        """

        self._categories = categories

    @property
    def months(self):
        """Gets the months of this BudgetDetail.  # noqa: E501


        :return: The months of this BudgetDetail.  # noqa: E501
        :rtype: list[MonthDetail]
        """
        return self._months

    @months.setter
    def months(self, months):
        """Sets the months of this BudgetDetail.


        :param months: The months of this BudgetDetail.  # noqa: E501
        :type months: list[MonthDetail]
        """

        self._months = months

    @property
    def transactions(self):
        """Gets the transactions of this BudgetDetail.  # noqa: E501


        :return: The transactions of this BudgetDetail.  # noqa: E501
        :rtype: list[TransactionSummary]
        """
        return self._transactions

    @transactions.setter
    def transactions(self, transactions):
        """Sets the transactions of this BudgetDetail.


        :param transactions: The transactions of this BudgetDetail.  # noqa: E501
        :type transactions: list[TransactionSummary]
        """

        self._transactions = transactions

    @property
    def subtransactions(self):
        """Gets the subtransactions of this BudgetDetail.  # noqa: E501


        :return: The subtransactions of this BudgetDetail.  # noqa: E501
        :rtype: list[SubTransaction]
        """
        return self._subtransactions

    @subtransactions.setter
    def subtransactions(self, subtransactions):
        """Sets the subtransactions of this BudgetDetail.


        :param subtransactions: The subtransactions of this BudgetDetail.  # noqa: E501
        :type subtransactions: list[SubTransaction]
        """

        self._subtransactions = subtransactions

    @property
    def scheduled_transactions(self):
        """Gets the scheduled_transactions of this BudgetDetail.  # noqa: E501


        :return: The scheduled_transactions of this BudgetDetail.  # noqa: E501
        :rtype: list[ScheduledTransactionSummary]
        """
        return self._scheduled_transactions

    @scheduled_transactions.setter
    def scheduled_transactions(self, scheduled_transactions):
        """Sets the scheduled_transactions of this BudgetDetail.


        :param scheduled_transactions: The scheduled_transactions of this BudgetDetail.  # noqa: E501
        :type scheduled_transactions: list[ScheduledTransactionSummary]
        """

        self._scheduled_transactions = scheduled_transactions

    @property
    def scheduled_subtransactions(self):
        """Gets the scheduled_subtransactions of this BudgetDetail.  # noqa: E501


        :return: The scheduled_subtransactions of this BudgetDetail.  # noqa: E501
        :rtype: list[ScheduledSubTransaction]
        """
        return self._scheduled_subtransactions

    @scheduled_subtransactions.setter
    def scheduled_subtransactions(self, scheduled_subtransactions):
        """Sets the scheduled_subtransactions of this BudgetDetail.


        :param scheduled_subtransactions: The scheduled_subtransactions of this BudgetDetail.  # noqa: E501
        :type scheduled_subtransactions: list[ScheduledSubTransaction]
        """

        self._scheduled_subtransactions = scheduled_subtransactions

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
        if not isinstance(other, BudgetDetail):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BudgetDetail):
            return True

        return self.to_dict() != other.to_dict()
