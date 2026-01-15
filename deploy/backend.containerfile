ARG BASE_IMAGE=ghcr.io/inginious/core-base:latest
FROM ${BASE_IMAGE}

COPY inginious/backend/ inginious/backend/
COPY inginious/scripts/ inginious/scripts/

# See https://github.com/pypa/setuptools_scm/#usage-from-docker
RUN --mount=source=.git,target=.git,type=bind \
    pip3 install --no-cache-dir -e .

CMD ["sh", "-c", "python3 -m inginious.scripts.backend ${AGENT} ${CLIENT}"]
