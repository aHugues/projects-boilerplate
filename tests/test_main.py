"""
test the main methods
"""

import pytest

from projects_boilerplate.main import (
    select_license,
    select_project_template_class,
)
from projects_boilerplate.structs import License


def test_select_project_template_class():
    assert select_project_template_class('flask').name == 'flask'
    assert select_project_template_class('python').name == 'python'
    with pytest.raises(KeyError):
        select_project_template_class('toto')


def test_select_license():
    assert select_license('mit') is License.MIT
    assert select_license('MIT') is License.MIT
    assert select_license('GpL') is License.GPL
    assert select_license('apache') is License.APACHE
    assert select_license('Apache') is License.APACHE
    with pytest.raises(ValueError, match='Invalid license name toto'):
        select_license('toto')
