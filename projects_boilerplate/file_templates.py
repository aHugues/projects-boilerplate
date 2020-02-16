"""
Classes for the file templates
"""

from pathlib import Path
from string import Template

from .base_template import (
    ROOT_TEMPLATES_DIRECTORY,
    BaseFileTemplate,
    EmptyFileTemplate,
    SimpleFileTemplate,
)
from .structs import License


class MypyTemplate(SimpleFileTemplate):
    name = 'mypy.ini'
    template_location = ROOT_TEMPLATES_DIRECTORY / 'mypy.ini.tpl'


class PylintTemplate(SimpleFileTemplate):
    name = 'pylint.ini'
    template_location = ROOT_TEMPLATES_DIRECTORY / 'pylint.ini.tpl'


class ManifestTemplate(EmptyFileTemplate):
    name = 'MANIFEST.in'

    @property
    def file_name(self):
        return 'MANIFEST.in'


class LicenseTemplate(SimpleFileTemplate):
    name = 'LICENSE'
    licenses_location = ROOT_TEMPLATES_DIRECTORY / 'licenses'
    file_name = 'LICENSE'


class LicenseApacheTemplate(LicenseTemplate):
    def __init__(self):
        super().__init__()
        self.template_location = self.licenses_location / 'license_apache.tpl'


class LicenseMitTemplate(LicenseTemplate):
    def __init__(self):
        super().__init__()
        self.template_location = self.licenses_location / 'license_mit.tpl'


class LicenseGplTemplate(LicenseTemplate):
    def __init__(self):
        super().__init__()
        self.template_location = self.licenses_location / 'license_gpl.tpl'


class PytestTemplate(BaseFileTemplate):
    name = 'pytest.ini'
    template_location = ROOT_TEMPLATES_DIRECTORY / 'pytest.ini.tpl'

    def __init__(self, project_sources_dir: str):
        super().__init__()
        self._project_sources_dir = project_sources_dir

    def build_template(self, destination: Path):
        template = Template(self.read_base_content())
        self._copy_to_destination(template.substitute(project_sources_dir=self._project_sources_dir), destination)


class RequirementsTemplate(SimpleFileTemplate):
    name = 'requirements.txt'
    template_location = ROOT_TEMPLATES_DIRECTORY / 'requirements.txt.tpl'


class TestsRequirementsTemplate(SimpleFileTemplate):
    name = 'tests-requirements.txt'
    template_location = ROOT_TEMPLATES_DIRECTORY / 'test-requirements.txt.tpl'


class SetupCfgTemplate(SimpleFileTemplate):
    name = 'setup.cfg'
    template_location = ROOT_TEMPLATES_DIRECTORY / 'setup.cfg.tpl'


class CoverageIniTemplate(SimpleFileTemplate):
    name = 'coverage.ini'
    template_location = ROOT_TEMPLATES_DIRECTORY / 'coverage.ini.tpl'


class MainFileTemplate(SimpleFileTemplate):
    name = 'main.py'
    template_location = ROOT_TEMPLATES_DIRECTORY / 'main.py.tpl'


class SampleFileTemplate(SimpleFileTemplate):
    name = 'sample.py'
    template_location = ROOT_TEMPLATES_DIRECTORY / 'sample.py.tpl'


class SampleTestTemplate(BaseFileTemplate):
    name = 'test_sample.py'
    template_location = ROOT_TEMPLATES_DIRECTORY / 'test_sample.py.tpl'

    def __init__(self, project_sources_dir: str, subdir='.'):
        super().__init__(subdir=subdir)
        self._project_sources_dir = project_sources_dir

    def build_template(self, destination: Path):
        template = Template(self.read_base_content())
        self._copy_to_destination(template.substitute(sources_dir=self._project_sources_dir), destination)


class SetupPyTemplate(BaseFileTemplate):
    name = 'setup.py'
    template_location = ROOT_TEMPLATES_DIRECTORY / 'setup.py.tpl'

    def __init__(self, project_name: str, project_license: License, project_sources_dir: str):
        super().__init__()
        self._project_name = project_name
        self._license_name = project_license.value
        self._project_sources_dir = project_sources_dir

    def build_template(self, destination: Path):
        template = Template(self.read_base_content())
        self._copy_to_destination(
            template.substitute(
                project_name=self._project_name, license=self._license_name, sources_dir=self._project_sources_dir
            ), destination,
        )


class DockerfileTemplate(BaseFileTemplate):
    name = 'Dockerfile'
    template_location = ROOT_TEMPLATES_DIRECTORY / 'Dockerfile.tpl'

    def __init__(self, project_name: str, project_sources_dir: str):
        super().__init__()
        self._project_name = project_name
        self._project_sources_dir = project_sources_dir

    def build_template(self, destination: Path):
        template = Template(self.read_base_content())
        self._copy_to_destination(template.substitute(
            project_name=self._project_name,
            project_sources_dir=self._project_sources_dir
        ), destination)


class PythonReadmeTemplate(BaseFileTemplate):
    name = 'README.md'
    template_location = ROOT_TEMPLATES_DIRECTORY / 'README.md.tpl'

    def __init__(self, project_name: str):
        super().__init__()
        self._project_name = project_name

    def build_template(self, destination: Path):
        template = Template(self.read_base_content())
        self._copy_to_destination(template.substitute(project_name=self._project_name), destination)


class InitTemplate(EmptyFileTemplate):
    name = '__init__.py'

    @property
    def file_name(self):
        return '__init__.py'
