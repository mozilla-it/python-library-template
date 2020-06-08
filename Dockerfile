FROM python:3
COPY . /workspace/.
WORKDIR /workspace

RUN pip install .
RUN tox
