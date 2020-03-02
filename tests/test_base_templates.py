# pylint: disable=missing-function-docstring

"""
Test the base_template methods
"""

from pathlib import Path

from projects_boilerplate import base_template


def test_base_file_template(tmp_path):
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
    template._copy_to_destination('toto', tmp_path)  # pylint: disable=protected-access
    assert (tmp_path / 'mock_template.txt').read_text() == 'toto'


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
