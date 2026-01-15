ARG BASE_IMAGE=ghcr.io/inginious/core-base:latest
FROM ${BASE_IMAGE}

COPY inginious/agent/__init__.py inginious/agent/
COPY inginious/agent/mcq_agent/ inginious/agent/mcq_agent/
COPY inginious/scripts inginious/scripts

# See https://github.com/pypa/setuptools_scm/#usage-from-docker
RUN --mount=source=.git,target=.git,type=bind \
    pip3 install --no-cache-dir -e .

CMD ["sh", "-c", "python3 -m inginious.scripts.agent_mcq ${BACKEND}"]
