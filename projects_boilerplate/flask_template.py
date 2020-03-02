"""
Template for a Flask server
"""

from pathlib import Path

from termcolor import (
    colored,
    cprint,
)

from .base_template import BaseProjectTemplate
from .file_templates import (
    CoverageIniTemplate,
    FlaskAppTemplate,
    FlaskDockerfileTemplate,
    FlaskInitTemplate,
    FlaskReadmeTemplate,
    FlaskRequirementsTemplate,
    FlaskTestAppTemplate,
    FlaskTestRequirementsTemplate,
    FlaskViewsTemplate,
    InitTemplate,
    LicenseApacheTemplate,
    LicenseGplTemplate,
    LicenseMitTemplate,
    LicenseTemplate,
    MypyTemplate,
    PylintTemplate,
    PytestTemplate,
    SetupCfgTemplate,
    WsgiTemplate,
)
from .structs import License


class FlaskProjectTemplate(BaseProjectTemplate):
    """
    Project template for a simple Flask server
    """
    name = 'flask'

    def __init__(self, project_name: str, project_license: License, docker: bool, destination_dir: Path):
        super().__init__(project_name, project_license, docker, destination_dir)

        self._project_sources_dir = project_name.replace('-', '_')

        self.file_templates = [
            FlaskReadmeTemplate(self._project_name),
            self.get_license_template(),
            FlaskAppTemplate(self._project_sources_dir),
            WsgiTemplate(self._project_sources_dir),
            FlaskRequirementsTemplate(),
            FlaskTestRequirementsTemplate(),
            SetupCfgTemplate(),
            PylintTemplate(),
            PytestTemplate(self._project_sources_dir),
            MypyTemplate(),
            CoverageIniTemplate(),
        ]

        if self._docker_enabled:
            self.file_templates.append(FlaskDockerfileTemplate(self._project_sources_dir))

        self.file_templates += [
            FlaskInitTemplate(self._project_sources_dir),
            FlaskViewsTemplate(self._project_sources_dir),
            InitTemplate('tests'),
            InitTemplate('tests/unit'),
            FlaskTestAppTemplate(self._project_sources_dir, 'tests/unit'),
            InitTemplate('tests/integration'),
        ]

        self.dirs = [
            'tests',
            self._project_sources_dir,
            'tests/integration',
            'tests/unit',
        ]

    def describe(self):
        project_type = colored('Flask project', attrs=['bold'])
        project_name_colored = colored(self._project_name, 'blue', attrs=['bold'])
        destination_dir_colored = colored(str(self._destination_dir), 'blue', attrs=['bold', 'underline'])
        cprint(f'Building {project_type} {project_name_colored} to directory {destination_dir_colored}')
        print(f"Project is running license {colored(self._project_license.value, attrs=['bold'])}")
        print(f"Docker support is {colored('enabled' if self._docker_enabled else 'disabled', attrs=['bold'])}")

    def get_license_template(self) -> LicenseTemplate:
        mapping = {
            License.APACHE: LicenseApacheTemplate(),
            License.GPL: LicenseGplTemplate(),
            License.MIT: LicenseMitTemplate(),
        }
        return mapping[self._project_license]
