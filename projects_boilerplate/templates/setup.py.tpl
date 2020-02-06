import sys
from setuptools import find_packages, setup


from pathlib import Path
with open(str(Path(".") / "README.md"), "r", encoding="utf-8") as f:
    README = f.read()


setup(
    name="$project_name",
    version="0.0.0",
    license="$license",
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
            "$project_name=$sources_dir.main:main",
        ]
    },
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
