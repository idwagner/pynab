import os

from pynab.openapi import Configuration
from pynab.openapi.api_client import ApiClient
from pynab.openapi.api import (
    AccountsApi,
    BudgetsApi,
    CategoriesApi,
    TransactionsApi,
    MonthsApi,
    PayeeLocationsApi,
    PayeesApi,
    ScheduledTransactionsApi,
    UserApi,
)
from pynab.exceptions import CredentialsNotFoundException


def get_credentials() -> Configuration:
    """
    Local credential handler
    """

    token = os.environ.get("YNAB_TOKEN")

    if not token:
        raise CredentialsNotFoundException

    creds = Configuration(
        api_key={"bearer": token}, api_key_prefix={"bearer": "Bearer"}
    )

    return creds


class YNABClient(object):

    def __init__(self, credentials: Configuration):

        self._api_client = ApiClient(configuration=credentials)

        self.accounts = AccountsApi(self._api_client)
        self.budgets = BudgetsApi(self._api_client)
        self.categories = CategoriesApi(self._api_client)
        self.months = MonthsApi(self._api_client)
        self.payee_locations = PayeeLocationsApi(self._api_client)
        self.payees = PayeesApi(self._api_client)
        self.scheduled_transactions = ScheduledTransactionsApi(self._api_client)
        self.transactions = TransactionsApi(self._api_client)
        self.user = UserApi(self._api_client)

    @staticmethod
    def from_env():
        return YNABClient(get_credentials())

    @staticmethod
    def from_token(token: str):
        creds = Configuration(
            api_key={"bearer": token}, api_key_prefix={"bearer": "Bearer"}
        )
        return YNABClient(creds)
