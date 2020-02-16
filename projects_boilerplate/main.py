"""
Entrypoint for the boilerplate
"""

from pathlib import Path
from typing import Type

import click

from pyfiglet import Figlet

from .file_templates import License
from .python_template import (
    BaseProjectTemplate,
    PythonProjectTemplate,
)

# Allow using the -h argument to call the help function
CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])


def select_project_template_class(key: str) -> Type[BaseProjectTemplate]:
    mapping = {
        'python': PythonProjectTemplate,
    }
    return mapping[key.lower()]


def select_license(name_param: str) -> License:
    license_values = [license_name.value for license_name in License]
    for license_name in license_values:
        if name_param.lower().strip() == license_name.lower().strip():
            return License(license_name)
    raise ValueError(f'Invalid license name {name_param}')


def print_header():
    figlet = Figlet(font='slant')
    print(figlet.renderText('Projects-'))
    print(figlet.renderText('Boilerplate'))


def print_intro():
    print('Parsing arguments...\n\n')


@click.command(context_settings=CONTEXT_SETTINGS)
@click.argument('name')
@click.option(
    '--template', '-t',
    help='Project template to choose from', required=True,
    type=click.Choice(['python', 'flask'], case_sensitive=False))
@click.option(
    '--license_name', '-l',
    help='License to choose from', default='MIT',
    type=click.Choice(['MIT', 'GPL', 'Apache'], case_sensitive=False))
@click.option(
    '--output', '-o',
    help='Directory in which output will be stored',
    type=click.Path(exists=False), default='.'
)
@click.option(
    '--docker', '-d', is_flag=True,
    help='Add support for Dockerisation to destination project',  # pylint: disable=missing-function-docstring
)
def main(name, template, license_name, output, docker):  # pylint: disable=missing-function-docstring
    print_header()

    template_class = select_project_template_class(template)
    project_license = select_license(license_name)
    output = Path(output)
    template = template_class(name, project_license, docker, output)

    template.describe()
    template.build()


if __name__ == '__main__':
    main()  # pylint: disable=no-value-for-parameter # pragma: no cover
