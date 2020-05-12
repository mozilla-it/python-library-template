FROM python:3
LABEL maintainer="Bryan Sieber bsieber@mozilla.com"

COPY . /workspace/.
WORKDIR /workspace

RUN pip3 install tox pre-commit
RUN tox
