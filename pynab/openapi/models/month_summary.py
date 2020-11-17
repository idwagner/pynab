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


class MonthSummary(object):
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
        'month': 'date',
        'note': 'str',
        'income': 'int',
        'budgeted': 'int',
        'activity': 'int',
        'to_be_budgeted': 'int',
        'age_of_money': 'int',
        'deleted': 'bool'
    }

    attribute_map = {
        'month': 'month',
        'note': 'note',
        'income': 'income',
        'budgeted': 'budgeted',
        'activity': 'activity',
        'to_be_budgeted': 'to_be_budgeted',
        'age_of_money': 'age_of_money',
        'deleted': 'deleted'
    }

    def __init__(self, month=None, note=None, income=None, budgeted=None, activity=None, to_be_budgeted=None, age_of_money=None, deleted=None, local_vars_configuration=None):  # noqa: E501
        """MonthSummary - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._month = None
        self._note = None
        self._income = None
        self._budgeted = None
        self._activity = None
        self._to_be_budgeted = None
        self._age_of_money = None
        self._deleted = None
        self.discriminator = None

        self.month = month
        if note is not None:
            self.note = note
        self.income = income
        self.budgeted = budgeted
        self.activity = activity
        self.to_be_budgeted = to_be_budgeted
        if age_of_money is not None:
            self.age_of_money = age_of_money
        self.deleted = deleted

    @property
    def month(self):
        """Gets the month of this MonthSummary.  # noqa: E501


        :return: The month of this MonthSummary.  # noqa: E501
        :rtype: date
        """
        return self._month

    @month.setter
    def month(self, month):
        """Sets the month of this MonthSummary.


        :param month: The month of this MonthSummary.  # noqa: E501
        :type month: date
        """
        if self.local_vars_configuration.client_side_validation and month is None:  # noqa: E501
            raise ValueError("Invalid value for `month`, must not be `None`")  # noqa: E501

        self._month = month

    @property
    def note(self):
        """Gets the note of this MonthSummary.  # noqa: E501


        :return: The note of this MonthSummary.  # noqa: E501
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """Sets the note of this MonthSummary.


        :param note: The note of this MonthSummary.  # noqa: E501
        :type note: str
        """

        self._note = note

    @property
    def income(self):
        """Gets the income of this MonthSummary.  # noqa: E501

        The total amount of transactions categorized to 'Inflow: To be Budgeted' in the month  # noqa: E501

        :return: The income of this MonthSummary.  # noqa: E501
        :rtype: int
        """
        return self._income

    @income.setter
    def income(self, income):
        """Sets the income of this MonthSummary.

        The total amount of transactions categorized to 'Inflow: To be Budgeted' in the month  # noqa: E501

        :param income: The income of this MonthSummary.  # noqa: E501
        :type income: int
        """
        if self.local_vars_configuration.client_side_validation and income is None:  # noqa: E501
            raise ValueError("Invalid value for `income`, must not be `None`")  # noqa: E501

        self._income = income

    @property
    def budgeted(self):
        """Gets the budgeted of this MonthSummary.  # noqa: E501

        The total amount budgeted in the month  # noqa: E501

        :return: The budgeted of this MonthSummary.  # noqa: E501
        :rtype: int
        """
        return self._budgeted

    @budgeted.setter
    def budgeted(self, budgeted):
        """Sets the budgeted of this MonthSummary.

        The total amount budgeted in the month  # noqa: E501

        :param budgeted: The budgeted of this MonthSummary.  # noqa: E501
        :type budgeted: int
        """
        if self.local_vars_configuration.client_side_validation and budgeted is None:  # noqa: E501
            raise ValueError("Invalid value for `budgeted`, must not be `None`")  # noqa: E501

        self._budgeted = budgeted

    @property
    def activity(self):
        """Gets the activity of this MonthSummary.  # noqa: E501

        The total amount of transactions in the month, excluding those categorized to 'Inflow: To be Budgeted'  # noqa: E501

        :return: The activity of this MonthSummary.  # noqa: E501
        :rtype: int
        """
        return self._activity

    @activity.setter
    def activity(self, activity):
        """Sets the activity of this MonthSummary.

        The total amount of transactions in the month, excluding those categorized to 'Inflow: To be Budgeted'  # noqa: E501

        :param activity: The activity of this MonthSummary.  # noqa: E501
        :type activity: int
        """
        if self.local_vars_configuration.client_side_validation and activity is None:  # noqa: E501
            raise ValueError("Invalid value for `activity`, must not be `None`")  # noqa: E501

        self._activity = activity

    @property
    def to_be_budgeted(self):
        """Gets the to_be_budgeted of this MonthSummary.  # noqa: E501

        The available amount for 'To be Budgeted'  # noqa: E501

        :return: The to_be_budgeted of this MonthSummary.  # noqa: E501
        :rtype: int
        """
        return self._to_be_budgeted

    @to_be_budgeted.setter
    def to_be_budgeted(self, to_be_budgeted):
        """Sets the to_be_budgeted of this MonthSummary.

        The available amount for 'To be Budgeted'  # noqa: E501

        :param to_be_budgeted: The to_be_budgeted of this MonthSummary.  # noqa: E501
        :type to_be_budgeted: int
        """
        if self.local_vars_configuration.client_side_validation and to_be_budgeted is None:  # noqa: E501
            raise ValueError("Invalid value for `to_be_budgeted`, must not be `None`")  # noqa: E501

        self._to_be_budgeted = to_be_budgeted

    @property
    def age_of_money(self):
        """Gets the age_of_money of this MonthSummary.  # noqa: E501

        The Age of Money as of the month  # noqa: E501

        :return: The age_of_money of this MonthSummary.  # noqa: E501
        :rtype: int
        """
        return self._age_of_money

    @age_of_money.setter
    def age_of_money(self, age_of_money):
        """Sets the age_of_money of this MonthSummary.

        The Age of Money as of the month  # noqa: E501

        :param age_of_money: The age_of_money of this MonthSummary.  # noqa: E501
        :type age_of_money: int
        """

        self._age_of_money = age_of_money

    @property
    def deleted(self):
        """Gets the deleted of this MonthSummary.  # noqa: E501

        Whether or not the month has been deleted.  Deleted months will only be included in delta requests.  # noqa: E501

        :return: The deleted of this MonthSummary.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this MonthSummary.

        Whether or not the month has been deleted.  Deleted months will only be included in delta requests.  # noqa: E501

        :param deleted: The deleted of this MonthSummary.  # noqa: E501
        :type deleted: bool
        """
        if self.local_vars_configuration.client_side_validation and deleted is None:  # noqa: E501
            raise ValueError("Invalid value for `deleted`, must not be `None`")  # noqa: E501

        self._deleted = deleted

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
        if not isinstance(other, MonthSummary):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MonthSummary):
            return True

        return self.to_dict() != other.to_dict()
