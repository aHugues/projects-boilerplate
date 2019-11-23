"""
Entrypoint for the boilerplate
"""

import click

# Allow using the -h argument to call the help function
CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])


@click.command(context_settings=CONTEXT_SETTINGS)
@click.argument('name')
@click.option(
    '--template', '-t',
    help='Project template to chose from', required=True,
    type=click.Choice(['python', 'flask'], case_sensitive=False))
@click.option(
    '--output', '-o',
    help='Directory in which output will be stored',
    type=click.Path(exists=True), default='.'
)
@click.option(
    '--docker', '-d', is_flag=True,
    help='Add support for Dockerisation to destination project',
)
def main(name, template, output, docker):
    print("Projects boilerplate")
    print("#"*15, '\n\n')
    print(f"Generating template {template} for project {name} to directory {output}")
    print(f"Support for Docker is {'enabled' if docker else 'disabled'}")


if __name__ == '__main__':
    main()  # pylint: disable=no-value-for-parameter # pragma: no cover
