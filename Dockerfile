FROM python:3
COPY . /workspace/.
WORKDIR /workspace

RUN pip3 install tox
# This DOCKERFILE is intended as the generic CLOUDBUILD configuration for testing
RUN tox
