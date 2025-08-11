# DOCKER-VERSION 1.1.0

ARG   VERSION=latest
ARG   REGISTRY=ghcr.io

FROM  ${REGISTRY}/inginious/core-base:${VERSION}

COPY inginious/common inginious/common
COPY inginious/frontend inginious/frontend
COPY inginious/client inginious/client
COPY inginious/agent/__init__.py inginious/agent/
COPY inginious/scripts inginious/scripts

# See https://github.com/pypa/setuptools_scm/#usage-from-docker
RUN --mount=source=.git,target=.git,type=bind \
    pip3 install --no-cache-dir -e .

COPY plugins plugins
RUN pip3 install --no-cache-dir -e plugins/ntnu_inginious_multifill

CMD ["sh", "-c", "python3 -m ntnu_inginious_multifill.agent.run ${BACKEND}"]
