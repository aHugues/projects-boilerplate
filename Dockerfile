FROM python:3.7-alpine

LABEL maintainer="me@aurelienhugues.com"
LABEL description="Boilerplate for Python projects"
LABEL version="0.0.0"

WORKDIR /usr/app
COPY setup.py README.md MANIFEST.in ./
COPY projects_boilerplate ./projects_boilerplate

RUN pip install .
RUN mkdir /files

VOLUME /files

ENTRYPOINT [ "projects_boilerplate" ]
CMD []
