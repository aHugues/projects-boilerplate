FROM python:3.7-alpine

LABEL maintainer="your email here"
LABEL description="You description here"
LABEL version="0.0.0"

WORKDIR /usr/app
COPY app.py README.md requirements.txt ./
COPY $project_sources_dir ./$project_sources_dir

RUN pip install gunicorn
RUN pip install -r requirements.txt
RUN mkdir /config

VOLUME /config

ENTRYPOINT [ "gunicorn" ]
CMD ["wsgi:app"]
