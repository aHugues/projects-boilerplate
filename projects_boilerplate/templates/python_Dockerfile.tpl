FROM python:3.7-alpine

LABEL maintainer="your email here"
LABEL description="You description here"
LABEL version="0.0.0"

WORKDIR /usr/app
COPY setup.py README.md MANIFEST.in ./
COPY $project_sources_dir ./$project_sources_dir

RUN pip install .
RUN mkdir /files

VOLUME /files

ENTRYPOINT [ "$project_name" ]
CMD []
