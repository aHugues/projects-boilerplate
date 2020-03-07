"""
Test the python project template
"""

from pathlib import Path

from projects_boilerplate import python_template
from projects_boilerplate.structs import License


def test_build_1(tmp_path):
    template = python_template.PythonProjectTemplate('test-project', License.MIT, True, tmp_path, False)
    template.build()

    assert (tmp_path / 'Dockerfile').exists()
    assert (tmp_path / 'MANIFEST.in').exists()
    assert (tmp_path / 'coverage.ini').exists()
    assert (tmp_path / 'requirements.txt').exists()
    assert (tmp_path / 'setup.py').exists()
    assert (tmp_path / 'LICENSE').exists()
    assert (tmp_path / 'README.md').exists()
    assert (tmp_path / 'mypy.ini').exists()
    assert (tmp_path / 'pytest.ini').exists()
    assert (tmp_path / 'setup.cfg').exists()
    assert (tmp_path / 'test-requirements.txt').exists()
    assert (tmp_path / 'tests' / '__init__.py').exists()
    assert (tmp_path / 'tests' / 'test_sample.py').exists()
    assert (tmp_path / 'test_project' / '__init__.py').exists()
    assert (tmp_path / 'test_project' / 'main.py').exists()
    assert (tmp_path / 'test_project' / 'sample.py').exists()


def test_build_2(tmp_path):
    template = python_template.PythonProjectTemplate('test-project', License.MIT, False, tmp_path, False)
    template.build()

    assert not (tmp_path / 'Dockerfile').exists()
    assert (tmp_path / 'MANIFEST.in').exists()
    assert (tmp_path / 'coverage.ini').exists()
    assert (tmp_path / 'requirements.txt').exists()
    assert (tmp_path / 'setup.py').exists()
    assert (tmp_path / 'LICENSE').exists()
    assert (tmp_path / 'README.md').exists()
    assert (tmp_path / 'mypy.ini').exists()
    assert (tmp_path / 'pytest.ini').exists()
    assert (tmp_path / 'setup.cfg').exists()
    assert (tmp_path / 'test-requirements.txt').exists()
    assert (tmp_path / 'tests' / '__init__.py').exists()
    assert (tmp_path / 'tests' / 'test_sample.py').exists()
    assert (tmp_path / 'test_project' / '__init__.py').exists()
    assert (tmp_path / 'test_project' / 'main.py').exists()
    assert (tmp_path / 'test_project' / 'sample.py').exists()


def test_build_3(tmp_path):
    template = python_template.PythonProjectTemplate('test-project', License.MIT, True, tmp_path, True)
    template.build()

    assert not (tmp_path / 'Dockerfile').exists()
    assert not (tmp_path / 'MANIFEST.in').exists()
    assert not (tmp_path / 'coverage.ini').exists()
    assert not (tmp_path / 'requirements.txt').exists()
    assert not (tmp_path / 'setup.py').exists()
    assert not (tmp_path / 'LICENSE').exists()
    assert not (tmp_path / 'README.md').exists()
    assert not (tmp_path / 'mypy.ini').exists()
    assert not (tmp_path / 'pytest.ini').exists()
    assert not (tmp_path / 'setup.cfg').exists()
    assert not (tmp_path / 'test-requirements.txt').exists()
    assert not (tmp_path / 'tests' / '__init__.py').exists()
    assert not (tmp_path / 'tests' / 'test_sample.py').exists()
    assert not (tmp_path / 'test_project' / '__init__.py').exists()
    assert not (tmp_path / 'test_project' / 'main.py').exists()
    assert not (tmp_path / 'test_project' / 'sample.py').exists()


def test_describe_1(capsys):
    template = python_template.PythonProjectTemplate('test-project', License.MIT, True, Path('/tmp'), False)
    template.describe()

    captured = capsys.readouterr()
    assert captured.out == f"""\
+------------------+----------------+
| Project name     | \x1b[1m\x1b[34mtest-project\x1b[0m   |
| Project template | \x1b[1mPython project\x1b[0m |
| Output directory | \x1b[4m\x1b[1m\x1b[34m/tmp\x1b[0m           |
| License          | MIT            |
| Docker support   | enabled        |
+------------------+----------------+
"""


def test_describe_2(capsys):
    template = python_template.PythonProjectTemplate('test-project', License.MIT, False, Path('/tmp'), False)
    template.describe()

    captured = capsys.readouterr()
    assert captured.out == f"""\
+------------------+----------------+
| Project name     | \x1b[1m\x1b[34mtest-project\x1b[0m   |
| Project template | \x1b[1mPython project\x1b[0m |
| Output directory | \x1b[4m\x1b[1m\x1b[34m/tmp\x1b[0m           |
| License          | MIT            |
| Docker support   | disabled       |
+------------------+----------------+
"""


def test_describe_3(capsys):
    template = python_template.PythonProjectTemplate('test-project', License.MIT, True, Path('/tmp'), True)
    template.describe()

    captured = capsys.readouterr()
    assert captured.out == f"""\
+------------------+----------------+
| Project name     | \x1b[1m\x1b[34mtest-project\x1b[0m   |
| Project template | \x1b[1mPython project\x1b[0m |
| Output directory | \x1b[4m\x1b[1m\x1b[34m/tmp\x1b[0m           |
| License          | MIT            |
| Docker support   | enabled        |
+------------------+----------------+
\x1b[33m
Warning: Dry-run is enabled, nothing will be done\x1b[0m
"""
