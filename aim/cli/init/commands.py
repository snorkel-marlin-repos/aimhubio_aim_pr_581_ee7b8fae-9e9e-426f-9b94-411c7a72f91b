import click
import os

from aim.engine.repo import AimRepo


@click.command()
def init():
    """
    Initializes new repository in the current working directory:
     - Creates .aim directory
     - Adds .aim/config.json file with initial configuration
    """
    repo = AimRepo(os.getcwd())
    re_init = False

    # Check whether repo already exists
    if repo.exists():
        re_init = click.confirm('Aim repository is already initialized. ' +
                                'Do you want to re-initialize it?')
        if not re_init:
            return
        # Clear old repo
        repo.rm()

    # Init repo
    new_repo = AimRepo(os.getcwd())
    if new_repo.init():
        if re_init:
            click.echo(
                'Re-initialized empty Aim repository at {}'.format(new_repo))
        else:
            click.echo(('Initialized a new ' +
                        'Aim repository at {}').format(new_repo))
