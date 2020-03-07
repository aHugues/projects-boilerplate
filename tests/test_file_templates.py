"""
Test the file templates with some logic inside them
"""

from pathlib import Path

from projects_boilerplate import file_templates
from projects_boilerplate.structs import License


def test_manifest_template():
    template = file_templates.ManifestTemplate()
    assert template.file_name == 'MANIFEST.in'


def test_license_apache(monkeypatch):
    monkeypatch.setattr(file_templates.LicenseTemplate, 'licenses_location', Path('tests/location'))
    template = file_templates.LicenseApacheTemplate()
    assert template.template_location == Path('tests/location/license_apache.tpl')


def test_license_mit(monkeypatch):
    monkeypatch.setattr(file_templates.LicenseTemplate, 'licenses_location', Path('tests/location'))
    template = file_templates.LicenseMitTemplate()
    assert template.template_location == Path('tests/location/license_mit.tpl')


def test_license_gpl(monkeypatch):
    monkeypatch.setattr(file_templates.LicenseTemplate, 'licenses_location', Path('tests/location'))
    template = file_templates.LicenseGplTemplate()
    assert template.template_location == Path('tests/location/license_gpl.tpl')


def test_pytest_template(tmp_path):
    template = file_templates.PytestTemplate('project_test')
    template.build_template(tmp_path)
    assert (tmp_path / 'pytest.ini').read_text() == """\
[pytest]
testpaths = tests/ project_test/
cache_dir = .cache
mccabe-complexity = 10
log_format =
    %(filename)s:%(lineno)d: [%(name)s:%(levelname)s] %(asctime)s: %(message)s
log_date_format = %Y-%m-%d %H:%M:%S
addopts =
    --cov-config coverage.ini
    --cov-report term
    --cov-report html:coverage/html
    --cov project_test/
    --pycodestyle
    --isort
    --mccabe
    --mypy
    --pylint --pylint-rcfile pylint.ini
    --verbose\
"""


def test_sample_test_template(tmp_path):
    template = file_templates.SampleTestTemplate('project_test')
    template.build_template(tmp_path)
    assert (tmp_path / 'test_sample.py').read_text() == """\
\"\"\"
This is a test for the sample file
\"\"\"

from project_test import sample


def test_sample():
    assert sample.sample_method(2) == 4
"""


def test_setup_py_template(tmp_path):
    template = file_templates.SetupPyTemplate('project-test', License.MIT, 'project_test')
    template.build_template(tmp_path)
    assert (tmp_path / 'setup.py').read_text() == """\
import sys
from setuptools import find_packages, setup


from pathlib import Path
with open(str(Path(".") / "README.md"), "r", encoding="utf-8") as f:
    README = f.read()


setup(
    name="project-test",
    version="0.0.0",
    license="MIT",
    url="url_to_your_project",
    description="Add your description here",
    long_description=README,
    long_description_content_type="text/markdown",
    author="Add your name here",
    author_email="Add your email here",
    packages=find_packages(exclude=["tests*"]),
    test_suite="tests",
    extras_require={
        "dev": [
            "pylint"
        ],
        "test": [
            "pytest",
            "pytest-cov",
            "pytest-pycodestyle",
            "pytest-isort",
            "pytest-mccabe",
            "pytest-mypy",
            "pytest-pylint",
            "tox"
        ]
        },
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "project-test=project_test.main:main",
        ]
    },
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
"""


def test_python_dockerfile_template(tmp_path):
    template = file_templates.PythonDockerfileTemplate('project-test', 'project_test')
    template.build_template(tmp_path)
    assert (tmp_path / 'Dockerfile').read_text() == """\
FROM python:3.7-alpine

LABEL maintainer="your email here"
LABEL description="You description here"
LABEL version="0.0.0"

WORKDIR /usr/app
COPY setup.py README.md MANIFEST.in ./
COPY project_test ./project_test

RUN pip install .
RUN mkdir /files

VOLUME /files

ENTRYPOINT [ "project-test" ]
CMD []
"""


def test_flask_dockerfile_template(tmp_path):
    template = file_templates.FlaskDockerfileTemplate('project_test')
    template.build_template(tmp_path)
    assert (tmp_path / 'Dockerfile').read_text() == """\
FROM python:3.7-alpine

LABEL maintainer="your email here"
LABEL description="You description here"
LABEL version="0.0.0"

WORKDIR /usr/app
COPY app.py README.md requirements.txt ./
COPY project_test ./project_test

RUN pip install gunicorn
RUN pip install -r requirements.txt
RUN mkdir /config

VOLUME /config

ENTRYPOINT [ "gunicorn" ]
CMD ["wsgi:app"]
"""


def test_flask_app_template(tmp_path):
    template = file_templates.FlaskAppTemplate('project_test')
    template.build_template(tmp_path)
    assert (tmp_path / 'app.py').read_text() == """\
from project_test import create_app

if __name__ == '__main__':
    app = create_app(debug=True)
    app.run(port=5000, host='0.0.0.0')
"""


def test_flask_wsgi_template(tmp_path):
    template = file_templates.WsgiTemplate('project_test')
    template.build_template(tmp_path)
    assert (tmp_path / 'wsgi.py').read_text() == """\
from project_test import create_app

app = create_app(debug=False)
"""


def test_flask_init_template(tmp_path):
    template = file_templates.FlaskInitTemplate('toto')
    (tmp_path / 'toto').mkdir()
    template.build_template(tmp_path)
    assert (tmp_path / 'toto/__init__.py').read_text() == """\
\"\"\"
Main package for the application
\"\"\"

from flask import Flask

from .views import MAIN_VIEWS


def create_app(debug=False):
    app = Flask(__name__)
    app.debug = debug
    app.register_blueprint(MAIN_VIEWS)
    return app
"""


def test_flask_requirements_template(tmp_path):
    template = file_templates.FlaskRequirementsTemplate()
    template.build_template(tmp_path)
    assert (tmp_path / 'requirements.txt').read_text() == """\
Flask
"""


def test_flask_test_requirements_template(tmp_path):
    template = file_templates.FlaskTestRequirementsTemplate()
    template.build_template(tmp_path)
    assert (tmp_path / 'test-requirements.txt').read_text() == """\
pytest
pylint
pytest-cov
pytest-pycodestyle
pytest-isort
pytest-mccabe
pytest-mypy
pytest-pylint
pytest-flask
"""


def test_flask_test_app_template(tmp_path):
    template = file_templates.FlaskTestAppTemplate('project_test', 'tests')
    (tmp_path / 'tests').mkdir()
    template.build_template(tmp_path)
    assert (tmp_path / 'tests/test_app.py').read_text() == """\
\"\"\"
Test the base application
\"\"\"

import pytest

from project_test import create_app


@pytest.fixture(name='app')
def fixture_app():
    app = create_app()
    return app


def test_app(client):
    response = client.get('/')
    assert response.status_code == 200
    assert "Flask Dockerized" in str(response.data)
"""


def test_python_readme_template(tmp_path):
    template = file_templates.PythonReadmeTemplate("project-test")
    template.build_template(tmp_path)
    assert (tmp_path / 'README.md').read_text() == """\
# project-test

Project automatically generated with [projects boilerplate](https://github.com/aHugues/projects-boilerplate)


## Install and run the project

```
pip install .
```

```
project-test
```

## Run the tests

```
pip install -r test-requirements.txt
pytest
```
"""


def test_flask_readme_template(tmp_path):
    template = file_templates.FlaskReadmeTemplate("project-test")
    template.build_template(tmp_path)
    assert (tmp_path / 'README.md').read_text() == """\
# project-test

Flask server automatically generated with [projects boilerplate](https://github.com/aHugues/projects-boilerplate)


## Install and run the project

```
pip install .
```

```
python app.py
```

## Run in production

```
pip install gunicorn
gunicorn wsgi:app
```

## Run the tests

```
pip install -r test-requirements.txt
pytest
```
"""


def test_init_template():
    template = file_templates.InitTemplate()
    assert template.file_name == '__init__.py'
