# pylint: disable=missing-function-docstring,protected-access

"""
Test the base_template methods
"""

from pathlib import Path

from projects_boilerplate import base_template
from projects_boilerplate.structs import License


def test_base_file_template_1(tmp_path):
    class MockBaseTemplate(base_template.BaseFileTemplate):
        template_location = Path(tmp_path / 'mock_template.txt.tpl')
        name = 'test.txt'

        def __init__(self, subdir='.'):
            super().__init__(subdir=subdir)
            self.destination_called = None

        def build_template(self, destination):
            self.destination_called = destination

    file_content = """\
Line 1
this is line 2
"""
    (tmp_path / 'mock_template.txt.tpl').write_text(file_content)
    template = MockBaseTemplate()

    assert template.file_name == 'mock_template.txt'
    assert template.full_name == './test.txt'
    assert template.read_base_content() == file_content
    template._copy_to_destination('toto', tmp_path)
    assert (tmp_path / 'mock_template.txt').read_text() == 'toto'


def test_base_file_template_2(tmp_path):
    class MockBaseTemplate(base_template.BaseFileTemplate):
        template_location = Path(tmp_path / 'mock_template.txt.tpl')
        name = 'test.txt'

        def __init__(self, subdir='.'):
            super().__init__(subdir=subdir)
            self.destination_called = None

        def build_template(self, destination):
            self.destination_called = destination

    file_content = """\
Line 1
this is line 2
"""
    (tmp_path / 'mock_template.txt.tpl').write_text(file_content)
    template = MockBaseTemplate()
    template._copy_to_destination('toto', tmp_path, destination_filename='machin.txt')
    assert (tmp_path / 'machin.txt').read_text() == 'toto'


def test_simple_file_template(tmp_path):
    class MockFileTemplate(base_template.SimpleFileTemplate):
        template_location = Path(tmp_path / 'mock_template.txt.tpl')
        name = 'test.txt'

    file_content = """\
Line 1
this is line 2
"""
    (tmp_path / 'mock_template.txt.tpl').write_text(file_content)
    template = MockFileTemplate()
    template.build_template(tmp_path)
    assert (tmp_path / 'mock_template.txt').read_text() == file_content


def test_empty_file_template(tmp_path):
    class MockEmptyFileTemplate(base_template.EmptyFileTemplate):
        @property
        def file_name(self):
            return 'toto.txt'

    template = MockEmptyFileTemplate()
    template.build_template(tmp_path)
    assert (tmp_path / 'toto.txt').exists()


def test_base_project_template_1(tmp_path, capsys):
    class MockEmptyFileTemplate(base_template.EmptyFileTemplate):
        @property
        def file_name(self):
            return 'toto.txt'

    class MockBaseProjecttemplate(base_template.BaseProjectTemplate):
        dirs = ['toto', 'tata']
        file_templates = [MockEmptyFileTemplate()]

        def describe(self):
            pass

    template = MockBaseProjecttemplate('test', License.MIT, False, tmp_path, True)

    template.build()
    captured = capsys.readouterr()
    assert captured.out == "\x1b[4m\x1b[1m\nBuilding directories\x1b[0m\n[\x1b[32m🗸\x1b[0m] toto\n\
[\x1b[32m🗸\x1b[0m] tata\n\x1b[4m\x1b[1m\nBuilding file templates\x1b[0m\n[\x1b[32m🗸\x1b[0m] ./\n\
\x1b[32m\nProject successfully built!\x1b[0m\n"
    assert not (tmp_path / 'toto').exists()
    assert not (tmp_path / 'tata').exists()
    assert not (tmp_path / 'toto.txt').exists()


def test_base_project_template_2(tmp_path, capsys):
    class MockEmptyFileTemplate(base_template.EmptyFileTemplate):
        @property
        def file_name(self):
            return 'toto.txt'

    class MockBaseProjecttemplate(base_template.BaseProjectTemplate):
        dirs = ['toto', 'tata']
        file_templates = [MockEmptyFileTemplate()]

        def describe(self):
            pass

    template = MockBaseProjecttemplate('test', License.MIT, False, tmp_path, False)

    template.build()
    captured = capsys.readouterr()
    assert captured.out == "\x1b[4m\x1b[1m\nBuilding directories\x1b[0m\n[\x1b[32m🗸\x1b[0m] toto\n\
[\x1b[32m🗸\x1b[0m] tata\n\x1b[4m\x1b[1m\nBuilding file templates\x1b[0m\n[\x1b[32m🗸\x1b[0m] ./\n\
\x1b[32m\nProject successfully built!\x1b[0m\n"
    assert (tmp_path / 'toto').exists()
    assert (tmp_path / 'tata').exists()
    assert (tmp_path / 'toto.txt').exists()
