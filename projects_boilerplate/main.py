"""
Entrypoint for the boilerplate
"""

from argparse import ArgumentParser
from pathlib import Path
from typing import (
    Dict,
    Type,
)

from pyfiglet import Figlet

from .base_template import BaseProjectTemplate
from .file_templates import License
from .flask_template import FlaskProjectTemplate
from .python_template import PythonProjectTemplate


def select_project_template_class(key: str) -> Type[BaseProjectTemplate]:
    mapping: Dict[str, Type[BaseProjectTemplate]] = {
        'flask': FlaskProjectTemplate,
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


def main():  # pylint: disable=missing-function-docstring
    print_header()

    parser = ArgumentParser()
    parser.add_argument(
        'name', type=str, help='Name of the project'
    )
    parser.add_argument(
        '--template', '-t', type=str, choices=['python', 'flask'], required=True,
        help='Project template to choose from',
    )
    parser.add_argument(
        '--license', '-l', type=str, choices=['MIT', 'GPL', 'Apache'], dest='license_name',
        help='License to choose from', default='MIT',
    )
    parser.add_argument(
        '--output', '-o', type=Path, default=Path('.'),
        help='Directory in which output will be stored',
    )
    parser.add_argument(
        '--docker', action='store_true',
        help='Add support for Docker to destination project',
    )
    parser.add_argument(
        '--dry-run', '-d', action='store_true',
        help='Describe the package without actually building it',
    )

    args = parser.parse_args()

    template_class = select_project_template_class(args.template)
    project_license = select_license(args.license_name)
    template = template_class(args.name, project_license, args.docker, args.output, args.dry_run)

    template.describe()
    template.build()


if __name__ == '__main__':
    main()  # pylint: disable=no-value-for-parameter # pragma: no cover
