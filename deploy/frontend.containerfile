ARG BASE_IMAGE=ghcr.io/inginious/core-base:latest
FROM ${BASE_IMAGE}

COPY inginious/frontend inginious/frontend/
COPY inginious/client inginious/client/
COPY inginious/scripts inginious/scripts

RUN dnf install -y gcc

# See https://github.com/pypa/setuptools_scm/#usage-from-docker
RUN --mount=source=.git,target=.git,type=bind \
    pip3 install --no-cache-dir -e .

COPY deploy/db_setup.py /tmp/db_setup.py

CMD ["sh", "-c", "python3 /tmp/db_setup.py; python3 -m inginious.scripts.webapp"]
