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


class PythonDockerfileTemplate(BaseFileTemplate):
    name = 'Dockerfile'
    template_location = ROOT_TEMPLATES_DIRECTORY / 'python_Dockerfile.tpl'

    def __init__(self, project_name: str, project_sources_dir: str):
        super().__init__()
        self._project_name = project_name
        self._project_sources_dir = project_sources_dir

    def build_template(self, destination: Path):
        template = Template(self.read_base_content())
        self._copy_to_destination(template.substitute(
            project_name=self._project_name,
            project_sources_dir=self._project_sources_dir
        ), destination, 'Dockerfile')


class FlaskDockerfileTemplate(BaseFileTemplate):
    name = 'Dockerfile'
    template_location = ROOT_TEMPLATES_DIRECTORY / 'flask_Dockerfile.tpl'

    def __init__(self, project_sources_dir: str):
        super().__init__()
        self._project_sources_dir = project_sources_dir

    def build_template(self, destination: Path):
        template = Template(self.read_base_content())
        self._copy_to_destination(template.substitute(
            project_sources_dir=self._project_sources_dir
        ), destination, 'Dockerfile')


class FlaskAppTemplate(BaseFileTemplate):
    name = 'app.py'
    template_location = ROOT_TEMPLATES_DIRECTORY / 'flask_app.py.tpl'

    def __init__(self, project_sources_dir: str):
        super().__init__()
        self._project_sources_dir = project_sources_dir

    def build_template(self, destination: Path):
        template = Template(self.read_base_content())
        self._copy_to_destination(template.substitute(
            project_sources_dir=self._project_sources_dir
        ), destination, 'app.py')


class WsgiTemplate(BaseFileTemplate):
    name = 'wsgi.py'
    template_location = ROOT_TEMPLATES_DIRECTORY / 'wsgi.py.tpl'

    def __init__(self, project_sources_dir: str):
        super().__init__()
        self._project_sources_dir = project_sources_dir

    def build_template(self, destination: Path):
        template = Template(self.read_base_content())
        self._copy_to_destination(template.substitute(
            project_sources_dir=self._project_sources_dir
        ), destination)


class FlaskInitTemplate(BaseFileTemplate):
    name = 'app.py'
    template_location = ROOT_TEMPLATES_DIRECTORY / 'flask_init.py.tpl'

    def __init__(self, subdir: str):
        super().__init__(subdir=subdir)

    def build_template(self, destination: Path):
        self._copy_to_destination(self.read_base_content(), destination, '__init__.py')


class FlaskRequirementsTemplate(BaseFileTemplate):
    name = 'requirements.txt'
    template_location = ROOT_TEMPLATES_DIRECTORY / 'flask_requirements.txt.tpl'

    def build_template(self, destination: Path):
        self._copy_to_destination(self.read_base_content(), destination, 'requirements.txt')


class FlaskTestRequirementsTemplate(BaseFileTemplate):
    name = 'test-requirements.txt'
    template_location = ROOT_TEMPLATES_DIRECTORY / 'flask_test_requirements.txt.tpl'

    def build_template(self, destination: Path):
        self._copy_to_destination(self.read_base_content(), destination, 'test-requirements.txt')


class FlaskTestAppTemplate(BaseFileTemplate):
    name = 'test_app.py'
    template_location = ROOT_TEMPLATES_DIRECTORY / 'flask_test_app.py.tpl'

    def __init__(self, project_sources_dir: str, subdir: str):
        super().__init__(subdir=subdir)
        self._project_sources_dir = project_sources_dir

    def build_template(self, destination: Path):
        content = Template(self.read_base_content()).substitute(project_sources_dir=self._project_sources_dir)
        self._copy_to_destination(content, destination, 'test_app.py')


class FlaskViewsTemplate(SimpleFileTemplate):
    name = 'views.py'
    template_location = ROOT_TEMPLATES_DIRECTORY / 'views.py.tpl'


class PythonReadmeTemplate(BaseFileTemplate):
    name = 'README.md'
    template_location = ROOT_TEMPLATES_DIRECTORY / 'python_README.md.tpl'

    def __init__(self, project_name: str):
        super().__init__()
        self._project_name = project_name

    def build_template(self, destination: Path):
        template = Template(self.read_base_content())
        self._copy_to_destination(template.substitute(project_name=self._project_name), destination, 'README.md')


class FlaskReadmeTemplate(BaseFileTemplate):
    name = 'README.md'
    template_location = ROOT_TEMPLATES_DIRECTORY / 'flask_README.md.tpl'

    def __init__(self, project_name: str):
        super().__init__()
        self._project_name = project_name

    def build_template(self, destination: Path):
        template = Template(self.read_base_content())
        self._copy_to_destination(template.substitute(project_name=self._project_name), destination, 'README.md')


class InitTemplate(EmptyFileTemplate):
    name = '__init__.py'

    @property
    def file_name(self):
        return '__init__.py'
