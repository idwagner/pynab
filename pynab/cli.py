
from pynab.helpers import get_client, select_budget
from pynab import exceptions
import click
from tabulate import tabulate
from colorama import init, Fore, Style

# colorama init
init()


def command_error(message):
    click.echo(f'ERROR: {message}')
    exit(1)


@click.group()
def main():
    pass


@click.group()
def budget_main():
    """Budget management"""
    pass


@click.command()
def budget_list():
    """List budgets"""

    client = get_client()
    budgets = client.budgets.get_budgets()
    for item in budgets.data.budgets:
        click.echo(f"{item.name} -- {item.id}")


@click.command()
@click.argument('budgetid')
def budget_avail(budgetid):
    """
    List current funds available for your budget. BUDGETID can be defined as:

    - The budget UUID taken from the 'budget list' command

    - A partial or full name of the budget. Multiple matches of a name will cause an error

    """

    try:
        bid = select_budget(budgetid)
    except exceptions.AmbiguousBudgetException:
        command_error('Named budget matched multiple budgets. Try matching by ID')

    if not bid:
        command_error(f'Could not find budget by reference "{budgetid}"')

    client = get_client()
    cat_list = client.categories.get_categories(budget_id=bid)

    data = []
    for group in cat_list.data.category_groups:

        if group.name == 'Hidden Categories':
            continue

        data.append([f'{Style.BRIGHT}{group.name}{Style.RESET_ALL}'])
        for category in group.categories:

            if category.balance == 0:
                continue
            data.append([
                f'{Style.BRIGHT}{Fore.GREEN}{category.name}{Style.NORMAL}{Fore.WHITE}',
                f'{category.balance/1000.0}'])

    print(tabulate(data, floatfmt=',.2f'))


@click.group()
def goal_main():
    """Goal management"""
    pass

@click.command()
@click.argument('budgetid')
def goal_list(budgetid):
    """List budgets"""

    try:
        bid = select_budget(budgetid)
    except exceptions.AmbiguousBudgetException:
        command_error('Named budget matched multiple budgets. Try matching by ID')

    if not bid:
        command_error(f'Could not find budget by reference "{budgetid}"')

    client = get_client()
    cat_list = client.categories.get_categories(budget_id=bid)

    data = []
    for group in cat_list.data.category_groups:

        if group.name == 'Hidden Categories':
            continue

        data.append([f'{Style.BRIGHT}{group.name}{Style.RESET_ALL}'])
        for category in group.categories:

            if category.balance == 0:
                continue
            print(category)
            data.append([
                f'{Style.BRIGHT}{Fore.GREEN}{category.name}{Style.NORMAL}{Fore.WHITE}',
                f'{category.balance/1000.0}'])

    print(tabulate(data, floatfmt=',.2f'))


main.add_command(budget_main, name='budget')
# main.add_command(goal_main, name='goal')
budget_main.add_command(budget_list, name='list')
budget_main.add_command(budget_avail, name='available')
# goal_main.add_command(goal_list, name='list')