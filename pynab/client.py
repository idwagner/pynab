

import os

from pynab.openapi import Configuration
from pynab.openapi.api_client import ApiClient
from pynab.openapi import AccountsApi, BudgetsApi, CategoriesApi, TransactionsApi
from pynab.exceptions import CredentialsNotFoundException


def get_credentials() -> Configuration:
    """
    Local credential handler
    """

    token = os.environ.get('YNAB_TOKEN')

    if not token:
        raise CredentialsNotFoundException

    creds = Configuration(
        api_key={'bearer': token},
        api_key_prefix={'bearer': 'Bearer'}
    )

    return creds


class YNABClient(object):

    def __init__(self, credentials: Configuration):

        self._api_cient = ApiClient(configuration=credentials)

        self.accounts = AccountsApi(self._api_cient)
        self.budgets = BudgetsApi(self._api_cient)
        self.categories = CategoriesApi(self._api_cient)
        self.transactions = TransactionsApi(self._api_cient)
