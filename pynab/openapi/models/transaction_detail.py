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


class TransactionDetail(object):
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
        'date': 'date',
        'amount': 'int',
        'memo': 'str',
        'cleared': 'str',
        'approved': 'bool',
        'flag_color': 'str',
        'account_id': 'str',
        'payee_id': 'str',
        'category_id': 'str',
        'transfer_account_id': 'str',
        'transfer_transaction_id': 'str',
        'matched_transaction_id': 'str',
        'import_id': 'str',
        'deleted': 'bool',
        'account_name': 'str',
        'payee_name': 'str',
        'category_name': 'str',
        'subtransactions': 'list[SubTransaction]'
    }

    attribute_map = {
        'id': 'id',
        'date': 'date',
        'amount': 'amount',
        'memo': 'memo',
        'cleared': 'cleared',
        'approved': 'approved',
        'flag_color': 'flag_color',
        'account_id': 'account_id',
        'payee_id': 'payee_id',
        'category_id': 'category_id',
        'transfer_account_id': 'transfer_account_id',
        'transfer_transaction_id': 'transfer_transaction_id',
        'matched_transaction_id': 'matched_transaction_id',
        'import_id': 'import_id',
        'deleted': 'deleted',
        'account_name': 'account_name',
        'payee_name': 'payee_name',
        'category_name': 'category_name',
        'subtransactions': 'subtransactions'
    }

    def __init__(self, id=None, date=None, amount=None, memo=None, cleared=None, approved=None, flag_color=None, account_id=None, payee_id=None, category_id=None, transfer_account_id=None, transfer_transaction_id=None, matched_transaction_id=None, import_id=None, deleted=None, account_name=None, payee_name=None, category_name=None, subtransactions=None, local_vars_configuration=None):  # noqa: E501
        """TransactionDetail - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._date = None
        self._amount = None
        self._memo = None
        self._cleared = None
        self._approved = None
        self._flag_color = None
        self._account_id = None
        self._payee_id = None
        self._category_id = None
        self._transfer_account_id = None
        self._transfer_transaction_id = None
        self._matched_transaction_id = None
        self._import_id = None
        self._deleted = None
        self._account_name = None
        self._payee_name = None
        self._category_name = None
        self._subtransactions = None
        self.discriminator = None

        self.id = id
        self.date = date
        self.amount = amount
        if memo is not None:
            self.memo = memo
        self.cleared = cleared
        self.approved = approved
        if flag_color is not None:
            self.flag_color = flag_color
        self.account_id = account_id
        if payee_id is not None:
            self.payee_id = payee_id
        if category_id is not None:
            self.category_id = category_id
        if transfer_account_id is not None:
            self.transfer_account_id = transfer_account_id
        if transfer_transaction_id is not None:
            self.transfer_transaction_id = transfer_transaction_id
        if matched_transaction_id is not None:
            self.matched_transaction_id = matched_transaction_id
        if import_id is not None:
            self.import_id = import_id
        self.deleted = deleted
        self.account_name = account_name
        if payee_name is not None:
            self.payee_name = payee_name
        if category_name is not None:
            self.category_name = category_name
        self.subtransactions = subtransactions

    @property
    def id(self):
        """Gets the id of this TransactionDetail.  # noqa: E501


        :return: The id of this TransactionDetail.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TransactionDetail.


        :param id: The id of this TransactionDetail.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def date(self):
        """Gets the date of this TransactionDetail.  # noqa: E501

        The transaction date in ISO format (e.g. 2016-12-01)  # noqa: E501

        :return: The date of this TransactionDetail.  # noqa: E501
        :rtype: date
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this TransactionDetail.

        The transaction date in ISO format (e.g. 2016-12-01)  # noqa: E501

        :param date: The date of this TransactionDetail.  # noqa: E501
        :type date: date
        """
        if self.local_vars_configuration.client_side_validation and date is None:  # noqa: E501
            raise ValueError("Invalid value for `date`, must not be `None`")  # noqa: E501

        self._date = date

    @property
    def amount(self):
        """Gets the amount of this TransactionDetail.  # noqa: E501

        The transaction amount in milliunits format  # noqa: E501

        :return: The amount of this TransactionDetail.  # noqa: E501
        :rtype: int
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this TransactionDetail.

        The transaction amount in milliunits format  # noqa: E501

        :param amount: The amount of this TransactionDetail.  # noqa: E501
        :type amount: int
        """
        if self.local_vars_configuration.client_side_validation and amount is None:  # noqa: E501
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def memo(self):
        """Gets the memo of this TransactionDetail.  # noqa: E501


        :return: The memo of this TransactionDetail.  # noqa: E501
        :rtype: str
        """
        return self._memo

    @memo.setter
    def memo(self, memo):
        """Sets the memo of this TransactionDetail.


        :param memo: The memo of this TransactionDetail.  # noqa: E501
        :type memo: str
        """

        self._memo = memo

    @property
    def cleared(self):
        """Gets the cleared of this TransactionDetail.  # noqa: E501

        The cleared status of the transaction  # noqa: E501

        :return: The cleared of this TransactionDetail.  # noqa: E501
        :rtype: str
        """
        return self._cleared

    @cleared.setter
    def cleared(self, cleared):
        """Sets the cleared of this TransactionDetail.

        The cleared status of the transaction  # noqa: E501

        :param cleared: The cleared of this TransactionDetail.  # noqa: E501
        :type cleared: str
        """
        if self.local_vars_configuration.client_side_validation and cleared is None:  # noqa: E501
            raise ValueError("Invalid value for `cleared`, must not be `None`")  # noqa: E501
        allowed_values = ["cleared", "uncleared", "reconciled"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and cleared not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `cleared` ({0}), must be one of {1}"  # noqa: E501
                .format(cleared, allowed_values)
            )

        self._cleared = cleared

    @property
    def approved(self):
        """Gets the approved of this TransactionDetail.  # noqa: E501

        Whether or not the transaction is approved  # noqa: E501

        :return: The approved of this TransactionDetail.  # noqa: E501
        :rtype: bool
        """
        return self._approved

    @approved.setter
    def approved(self, approved):
        """Sets the approved of this TransactionDetail.

        Whether or not the transaction is approved  # noqa: E501

        :param approved: The approved of this TransactionDetail.  # noqa: E501
        :type approved: bool
        """
        if self.local_vars_configuration.client_side_validation and approved is None:  # noqa: E501
            raise ValueError("Invalid value for `approved`, must not be `None`")  # noqa: E501

        self._approved = approved

    @property
    def flag_color(self):
        """Gets the flag_color of this TransactionDetail.  # noqa: E501

        The transaction flag  # noqa: E501

        :return: The flag_color of this TransactionDetail.  # noqa: E501
        :rtype: str
        """
        return self._flag_color

    @flag_color.setter
    def flag_color(self, flag_color):
        """Sets the flag_color of this TransactionDetail.

        The transaction flag  # noqa: E501

        :param flag_color: The flag_color of this TransactionDetail.  # noqa: E501
        :type flag_color: str
        """
        allowed_values = ["red", "orange", "yellow", "green", "blue", "purple"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and flag_color not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `flag_color` ({0}), must be one of {1}"  # noqa: E501
                .format(flag_color, allowed_values)
            )

        self._flag_color = flag_color

    @property
    def account_id(self):
        """Gets the account_id of this TransactionDetail.  # noqa: E501


        :return: The account_id of this TransactionDetail.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this TransactionDetail.


        :param account_id: The account_id of this TransactionDetail.  # noqa: E501
        :type account_id: str
        """
        if self.local_vars_configuration.client_side_validation and account_id is None:  # noqa: E501
            raise ValueError("Invalid value for `account_id`, must not be `None`")  # noqa: E501

        self._account_id = account_id

    @property
    def payee_id(self):
        """Gets the payee_id of this TransactionDetail.  # noqa: E501


        :return: The payee_id of this TransactionDetail.  # noqa: E501
        :rtype: str
        """
        return self._payee_id

    @payee_id.setter
    def payee_id(self, payee_id):
        """Sets the payee_id of this TransactionDetail.


        :param payee_id: The payee_id of this TransactionDetail.  # noqa: E501
        :type payee_id: str
        """

        self._payee_id = payee_id

    @property
    def category_id(self):
        """Gets the category_id of this TransactionDetail.  # noqa: E501


        :return: The category_id of this TransactionDetail.  # noqa: E501
        :rtype: str
        """
        return self._category_id

    @category_id.setter
    def category_id(self, category_id):
        """Sets the category_id of this TransactionDetail.


        :param category_id: The category_id of this TransactionDetail.  # noqa: E501
        :type category_id: str
        """

        self._category_id = category_id

    @property
    def transfer_account_id(self):
        """Gets the transfer_account_id of this TransactionDetail.  # noqa: E501

        If a transfer transaction, the account to which it transfers  # noqa: E501

        :return: The transfer_account_id of this TransactionDetail.  # noqa: E501
        :rtype: str
        """
        return self._transfer_account_id

    @transfer_account_id.setter
    def transfer_account_id(self, transfer_account_id):
        """Sets the transfer_account_id of this TransactionDetail.

        If a transfer transaction, the account to which it transfers  # noqa: E501

        :param transfer_account_id: The transfer_account_id of this TransactionDetail.  # noqa: E501
        :type transfer_account_id: str
        """

        self._transfer_account_id = transfer_account_id

    @property
    def transfer_transaction_id(self):
        """Gets the transfer_transaction_id of this TransactionDetail.  # noqa: E501

        If a transfer transaction, the id of transaction on the other side of the transfer  # noqa: E501

        :return: The transfer_transaction_id of this TransactionDetail.  # noqa: E501
        :rtype: str
        """
        return self._transfer_transaction_id

    @transfer_transaction_id.setter
    def transfer_transaction_id(self, transfer_transaction_id):
        """Sets the transfer_transaction_id of this TransactionDetail.

        If a transfer transaction, the id of transaction on the other side of the transfer  # noqa: E501

        :param transfer_transaction_id: The transfer_transaction_id of this TransactionDetail.  # noqa: E501
        :type transfer_transaction_id: str
        """

        self._transfer_transaction_id = transfer_transaction_id

    @property
    def matched_transaction_id(self):
        """Gets the matched_transaction_id of this TransactionDetail.  # noqa: E501

        If transaction is matched, the id of the matched transaction  # noqa: E501

        :return: The matched_transaction_id of this TransactionDetail.  # noqa: E501
        :rtype: str
        """
        return self._matched_transaction_id

    @matched_transaction_id.setter
    def matched_transaction_id(self, matched_transaction_id):
        """Sets the matched_transaction_id of this TransactionDetail.

        If transaction is matched, the id of the matched transaction  # noqa: E501

        :param matched_transaction_id: The matched_transaction_id of this TransactionDetail.  # noqa: E501
        :type matched_transaction_id: str
        """

        self._matched_transaction_id = matched_transaction_id

    @property
    def import_id(self):
        """Gets the import_id of this TransactionDetail.  # noqa: E501

        If the Transaction was imported, this field is a unique (by account) import identifier.  If this transaction was imported through File Based Import or Direct Import and not through the API, the import_id will have the format: 'YNAB:[milliunit_amount]:[iso_date]:[occurrence]'.  For example, a transaction dated 2015-12-30 in the amount of -$294.23 USD would have an import_id of 'YNAB:-294230:2015-12-30:1'.  If a second transaction on the same account was imported and had the same date and same amount, its import_id would be 'YNAB:-294230:2015-12-30:2'.  # noqa: E501

        :return: The import_id of this TransactionDetail.  # noqa: E501
        :rtype: str
        """
        return self._import_id

    @import_id.setter
    def import_id(self, import_id):
        """Sets the import_id of this TransactionDetail.

        If the Transaction was imported, this field is a unique (by account) import identifier.  If this transaction was imported through File Based Import or Direct Import and not through the API, the import_id will have the format: 'YNAB:[milliunit_amount]:[iso_date]:[occurrence]'.  For example, a transaction dated 2015-12-30 in the amount of -$294.23 USD would have an import_id of 'YNAB:-294230:2015-12-30:1'.  If a second transaction on the same account was imported and had the same date and same amount, its import_id would be 'YNAB:-294230:2015-12-30:2'.  # noqa: E501

        :param import_id: The import_id of this TransactionDetail.  # noqa: E501
        :type import_id: str
        """

        self._import_id = import_id

    @property
    def deleted(self):
        """Gets the deleted of this TransactionDetail.  # noqa: E501

        Whether or not the transaction has been deleted.  Deleted transactions will only be included in delta requests.  # noqa: E501

        :return: The deleted of this TransactionDetail.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this TransactionDetail.

        Whether or not the transaction has been deleted.  Deleted transactions will only be included in delta requests.  # noqa: E501

        :param deleted: The deleted of this TransactionDetail.  # noqa: E501
        :type deleted: bool
        """
        if self.local_vars_configuration.client_side_validation and deleted is None:  # noqa: E501
            raise ValueError("Invalid value for `deleted`, must not be `None`")  # noqa: E501

        self._deleted = deleted

    @property
    def account_name(self):
        """Gets the account_name of this TransactionDetail.  # noqa: E501


        :return: The account_name of this TransactionDetail.  # noqa: E501
        :rtype: str
        """
        return self._account_name

    @account_name.setter
    def account_name(self, account_name):
        """Sets the account_name of this TransactionDetail.


        :param account_name: The account_name of this TransactionDetail.  # noqa: E501
        :type account_name: str
        """
        if self.local_vars_configuration.client_side_validation and account_name is None:  # noqa: E501
            raise ValueError("Invalid value for `account_name`, must not be `None`")  # noqa: E501

        self._account_name = account_name

    @property
    def payee_name(self):
        """Gets the payee_name of this TransactionDetail.  # noqa: E501


        :return: The payee_name of this TransactionDetail.  # noqa: E501
        :rtype: str
        """
        return self._payee_name

    @payee_name.setter
    def payee_name(self, payee_name):
        """Sets the payee_name of this TransactionDetail.


        :param payee_name: The payee_name of this TransactionDetail.  # noqa: E501
        :type payee_name: str
        """

        self._payee_name = payee_name

    @property
    def category_name(self):
        """Gets the category_name of this TransactionDetail.  # noqa: E501


        :return: The category_name of this TransactionDetail.  # noqa: E501
        :rtype: str
        """
        return self._category_name

    @category_name.setter
    def category_name(self, category_name):
        """Sets the category_name of this TransactionDetail.


        :param category_name: The category_name of this TransactionDetail.  # noqa: E501
        :type category_name: str
        """

        self._category_name = category_name

    @property
    def subtransactions(self):
        """Gets the subtransactions of this TransactionDetail.  # noqa: E501

        If a split transaction, the subtransactions.  # noqa: E501

        :return: The subtransactions of this TransactionDetail.  # noqa: E501
        :rtype: list[SubTransaction]
        """
        return self._subtransactions

    @subtransactions.setter
    def subtransactions(self, subtransactions):
        """Sets the subtransactions of this TransactionDetail.

        If a split transaction, the subtransactions.  # noqa: E501

        :param subtransactions: The subtransactions of this TransactionDetail.  # noqa: E501
        :type subtransactions: list[SubTransaction]
        """
        if self.local_vars_configuration.client_side_validation and subtransactions is None:  # noqa: E501
            raise ValueError("Invalid value for `subtransactions`, must not be `None`")  # noqa: E501

        self._subtransactions = subtransactions

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
        if not isinstance(other, TransactionDetail):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TransactionDetail):
            return True

        return self.to_dict() != other.to_dict()
