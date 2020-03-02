"""
Template for a simple Python project
"""

from pathlib import Path

from termcolor import (
    colored,
    cprint,
)

from .base_template import BaseProjectTemplate
from .file_templates import (
    CoverageIniTemplate,
    InitTemplate,
    LicenseApacheTemplate,
    LicenseGplTemplate,
    LicenseMitTemplate,
    LicenseTemplate,
    MainFileTemplate,
    ManifestTemplate,
    MypyTemplate,
    PylintTemplate,
    PytestTemplate,
    PythonDockerfileTemplate,
    PythonReadmeTemplate,
    RequirementsTemplate,
    SampleFileTemplate,
    SampleTestTemplate,
    SetupCfgTemplate,
    SetupPyTemplate,
    TestsRequirementsTemplate,
)
from .structs import License


class PythonProjectTemplate(BaseProjectTemplate):
    """
    Project template for a simple Python project
    """
    name = 'python'

    def __init__(self, project_name: str, project_license: License, docker: bool, destination_dir: Path, dry_run: bool):
        super().__init__(project_name, project_license, docker, destination_dir, dry_run)

        self._project_sources_dir = project_name.replace('-', '_')

        self.file_templates = [
            PythonReadmeTemplate(self._project_name),
            self.get_license_template(),
            SetupPyTemplate(self._project_name, self._project_license, self._project_sources_dir),
            SetupCfgTemplate(),
            ManifestTemplate(),
            RequirementsTemplate(),
            TestsRequirementsTemplate(),
            PytestTemplate(self._project_sources_dir),
            PylintTemplate(),
            CoverageIniTemplate(),
            MypyTemplate(),
        ]

        if self._docker_enabled:
            self.file_templates.append(PythonDockerfileTemplate(self._project_name, self._project_sources_dir))

        self.file_templates += [
            InitTemplate(self._project_sources_dir),
            MainFileTemplate(self._project_sources_dir),
            SampleFileTemplate(self._project_sources_dir),
            InitTemplate('tests'),
            SampleTestTemplate(self._project_sources_dir, 'tests'),
        ]

        self.dirs = [
            'tests',
            self._project_sources_dir,
        ]

    def describe(self):
        project_type = colored('Python project', attrs=['bold'])
        project_name_colored = colored(self._project_name, 'blue', attrs=['bold'])
        destination_dir_colored = colored(str(self._destination_dir), 'blue', attrs=['bold', 'underline'])
        cprint(f'Building {project_type} {project_name_colored} to directory {destination_dir_colored}')
        print(f"Project is running license {colored(self._project_license.value, attrs=['bold'])}")
        print(f"Docker support is {colored('enabled' if self._docker_enabled else 'disabled', attrs=['bold'])}")

        if self._dry_run:
            cprint('\nWarning: Dry-run is enabled, nothing will be done', color='yellow')

    def get_license_template(self) -> LicenseTemplate:
        mapping = {
            License.APACHE: LicenseApacheTemplate(),
            License.GPL: LicenseGplTemplate(),
            License.MIT: LicenseMitTemplate(),
        }
        return mapping[self._project_license]
