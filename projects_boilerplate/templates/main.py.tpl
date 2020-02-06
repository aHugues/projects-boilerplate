"""
Entrypoint for the application
"""

from argparse import ArgumentParser


def main():  # pragma: no cover
    parser = ArgumentParser()
    parser.parse_args()
    print("This is a sample project generated with projects_boilerplate")


if __name__ == '__main__':
    main()  # pragma: no cover
