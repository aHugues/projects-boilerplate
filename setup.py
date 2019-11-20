import sys
from setuptools import find_packages, setup


from pathlib import Path
with open(str(Path(".") / "README.md"), "r", encoding="utf-8") as f:
    README = f.read()


setup(
    name="projects-boilerplate",
    version="0.0.0",
    license="Apache",
    url="https://github.com/aHugues/projects-boilerplate.git",
    description="Boilerplate to automatically generate projects",
    long_description=README,
    long_description_content_type="text/markdown",
    author="Aurélien Hugues",
    author_email="me@aurelienhugues.com",
    packages=find_packages(exclude=["tests*"]),
    include_package_data=True,
    install_requires=[],
    test_suite="tests",
    extras_require={
        "dev": [
            "codecov",
            "black",
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
            "codecov",
            "tox"
        ]
        },
    python_requires=">=3.6",
    # entry_points={"console_scripts": ["port-eye=port_eye.main:main"]},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
