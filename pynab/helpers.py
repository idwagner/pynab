
import re

import click
from pynab.client import YNABClient, get_credentials
from pynab import exceptions

RE_UUID = re.compile(r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$')


def get_client():
    try:
        credentials = get_credentials()
        client = YNABClient(credentials)

    except exceptions.CredentialsNotFoundException:
        click.echo('ERROR: Credentials not found. Set your YNAB API token as environment '
                   'variable YNAB_TOKEN.')

    return client


def is_uuid(uuid: str):
    """Check if string is an UUID."""
    return True if RE_UUID.search(uuid) else False


def match_by_name_or_id(identifier: str, data: list) -> str:

    RE_BY_NAME = re.compile(identifier, re.IGNORECASE)
    identifier = identifier.lower()

    exact_match = [x for x in data if identifier == x.name.lower()]
    match = [x for x in data if RE_BY_NAME.search(x.name)]

    if len(exact_match) == 1:
        return exact_match[0].id

    if len(match) == 1:
        return match[0].id

    if exact_match or match:
        # There were multiple matches
        raise exceptions.AmbiguousBudgetException

    return None


def select_budget(identifier: str) -> str:

    if is_uuid(identifier):
        return identifier

    client = get_client()
    items = client.budgets.get_budgets()
    data = items.data.budgets

    return match_by_name_or_id(identifier, data)


def select_category(budget_id, identifier: str) -> str:

    data = []
    if is_uuid(identifier):
        return identifier

    client = get_client()
    items = client.categories.get_categories(budget_id=budget_id)
    for group in items.data.category_groups:
        data.extend([x for x in group.categories])

    return match_by_name_or_id(identifier, data)
