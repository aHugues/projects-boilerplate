[![Build Status](https://travis-ci.org/aHugues/projects-boilerplate.svg?branch=master)](https://travis-ci.org/aHugues/projects-boilerplate)
[![codecov](https://codecov.io/gh/aHugues/projects-boilerplate/branch/master/graph/badge.svg)](https://codecov.io/gh/aHugues/projects-boilerplate)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

# projects-boilerplate
Boilerplate to automatically generate projects

## Features

- Automated generation of projects according to predefined templates
- **WIP:** Support for multiple languages (*Currently only Python*)
- **WIP:** Support for custom projects templates
- Python and Docker deployment

Example command:
```
$ projects-boilerplate -t python -o ~/my_project
```

## Installation

This application needs Python 3.6+ to run.

### Docker

If you have Docker installed, you can pull the image from docker-hub:

```
docker pull ahugues/projects-boilerplate
```

You can also build the image by cloning the repository and running

```
docker build -t projects-boilerplate .
```

### Python

If you have Python 3.6+ installed, you can install `projects-boilerplate` from Pypi: 

```
pip install projects-boilerplate
```

or locally by cloning the repository and running

```
pip install .
```

## Usage

### General notes

`projects-boilerplate` exposes a command line executable names `projects-boilerplate`.

When run without options, `projects-boilerplate` will simply display the help message.

**TOTO: ADD DETAILS HERE**

If using Docker, you can run a `projects-boilerplate` container using:

```
docker run -v "/path/to/your/project":/output projects-boilerplate <options>
```

### CLI reference

```
Usage: projects-boilerplate [OPTIONS] NAME

Options:
  -t, --template [python|flask]  Project template to chose from  [required]
  -o, --output PATH              Directory in which output will be stored
  -d, --docker                   Add support for Dockerisation to destination
                                 project
  -h, --help                     Show this message and exit.
```

## Contributing

Contributions are closed at the moment

## License

Apache 2
