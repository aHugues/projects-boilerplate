"""
Template for a simple Python project
"""

from pathlib import Path

from .base_template import BaseProjectTemplate
from .file_templates import (
    CoverageIniTemplate,
    DockerfileTemplate,
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

    def __init__(self, project_name: str, project_license: License, docker: bool, destination_dir: Path):
        super().__init__(project_name, project_license, docker, destination_dir)

        self._project_sources_dir = project_name.replace('-', '_')

        self.file_templates = [
            CoverageIniTemplate(),
            MypyTemplate(),
            PylintTemplate(),
            ManifestTemplate(),
            PytestTemplate(self._project_sources_dir),
            self.get_license_template(),
            RequirementsTemplate(),
            SetupCfgTemplate(),
            SetupPyTemplate(self._project_name, self._project_license, self._project_sources_dir),
            InitTemplate('tests'),
            MainFileTemplate(self._project_sources_dir),
            InitTemplate(self._project_sources_dir),
            PythonReadmeTemplate(self._project_name),
            TestsRequirementsTemplate(),
            SampleFileTemplate(self._project_sources_dir),
            SampleTestTemplate(self._project_sources_dir, 'tests'),
        ]

        self.dirs = [
            'tests',
            self._project_sources_dir,
        ]

        if self._docker_enabled:
            self.file_templates.append(DockerfileTemplate(self._project_name, self._project_sources_dir))

    def describe(self):
        print(f'Python project template\nPackage name: {self._project_name}')
        print(f'Project is running license {self._project_license.value}')
        print(f"Docker support is {'enabled' if self._docker_enabled else 'disabled'}")

    def get_license_template(self) -> LicenseTemplate:
        mapping = {
            License.APACHE: LicenseApacheTemplate(),
            License.GPL: LicenseGplTemplate(),
            License.MIT: LicenseMitTemplate(),
        }
        return mapping[self._project_license]
