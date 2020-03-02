"""
Test the base application
"""

import pytest

from $project_sources_dir import create_app


@pytest.fixture(name='app')
def fixture_app():
    app = create_app()
    return app


def test_app(client):
    response = client.get('/')
    assert response.status_code == 200
    assert "Flask Dockerized" in str(response.data)
