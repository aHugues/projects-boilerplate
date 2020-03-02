"""
Contains the base classes and methods for the templates
"""

import abc
import os

from pathlib import Path
from typing import (
    List,
    Optional,
)

from termcolor import (
    colored,
    cprint,
)

from .structs import License

ROOT_TEMPLATES_DIRECTORY = Path(os.path.abspath(__file__)).parent / 'templates'
SUCCESS = f"[{colored('🗸', color='green')}]"


class BaseFileTemplate(abc.ABC):
    """
    Base class for a file template
    """

    name: str = ''
    template_location: Path = Path()

    def __init__(self, subdir: str = '.'):
        self._subdir = subdir

    def _copy_to_destination(self, content: str, destination: Path, destination_filename: Optional[str] = None):
        if destination_filename is None:
            destination_complete_path = destination / self._subdir / self.file_name
        else:
            destination_complete_path = destination / self._subdir / destination_filename
        destination_complete_path.write_text(content)

    @property
    def file_name(self):
        return self.template_location.stem

    @property
    def full_name(self) -> str:
        return f'{self._subdir}/{self.name}'

    def read_base_content(self) -> str:
        """
        Read the raw content of the template and return it
        """
        return self.template_location.read_text()

    @abc.abstractmethod
    def build_template(self, destination: Path):
        """
        Build the selected template according to the class specifications
        """
        raise NotImplementedError()


class SimpleFileTemplate(BaseFileTemplate):
    """
    Template that does not take parameters
    """
    def build_template(self, destination: Path):
        content = self.template_location.read_text()
        self._copy_to_destination(content, destination)


class EmptyFileTemplate(BaseFileTemplate):
    """
    Template that will create an empty file
    """

    def build_template(self, destination: Path):
        self._copy_to_destination('', destination)

    @property
    @abc.abstractmethod
    def file_name(self):
        raise NotImplementedError()


class BaseProjectTemplate(abc.ABC):
    """
    Base class for templates
    """
    name: str = ''
    file_templates: List[BaseFileTemplate] = []
    dirs: List[str] = []

    def __init__(self, project_name: str, project_license: License, docker: bool, destination_dir: Path):
        self._project_name = project_name
        self._project_license = project_license
        self._docker_enabled = docker
        self._destination_dir = destination_dir

    def build_dir(self, dir_name: str):
        dir_full_path = self._destination_dir / dir_name
        dir_full_path.mkdir(exist_ok=True)

    @abc.abstractmethod
    def describe(self):
        raise NotImplementedError()

    def build(self):
        cprint('\nBuilding directories', attrs=['bold', 'underline'])
        self._destination_dir.mkdir(exist_ok=True)
        for destination_dir in self.dirs:
            self.build_dir(destination_dir)
            print(f'{SUCCESS} {destination_dir}')

        cprint('\nBuilding file templates', attrs=['bold', 'underline'])
        for template in self.file_templates:
            template.build_template(self._destination_dir)
            print(f'{SUCCESS} {template.full_name}')

        cprint('\nProject successfully built!', color='green')
