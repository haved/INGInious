ARG  VERSION=main
ARG  REGISTRY=ghcr.io

ARG  BASE_IMAGE=${REGISTRY}/inginious/core-base:${VERSION}
FROM ${BASE_IMAGE}

ARG  PYTHON_VERSION=3.14
ENV  PYTHON_VERSION="${PYTHON_VERSION}"

COPY inginious/frontend inginious/frontend/
COPY inginious/client inginious/client/
COPY inginious/agent/__init__.py inginious/agent/

# See https://github.com/pypa/setuptools_scm/#usage-from-docker
RUN  --mount=source=.git,target=.git,type=bind \
    pip"${PYTHON_VERSION}" install --no-cache-dir -e .

COPY plugins plugins
RUN pip"${PYTHON_VERSION}" install --no-cache-dir -e plugins/ntnu_inginious_multifill

CMD ["sh", "-c", "python${PYTHON_VERSION} -m ntnu_inginious_multifill.agent.run ${BACKEND}"]
