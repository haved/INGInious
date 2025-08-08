INGInious plugin for multiple fill-ins
=====================================================

This plugin defines a new problem type named `multifill` 

## Installing

To make the plugin available in the docker containers, make sure both `deploy/frontend.containerfile` and to the `deploy/agent-mcq.containerfile` have the following lines.

```sh
COPY inginious/frontend inginious/frontend
COPY inginious/client inginious/client

[...]

COPY <folder containing this plugin> plugins
RUN pip3 install plugins/ntnu_inginious_multifill
pip3 install plugins/ntnu_inginious_multifill
```

In the case of `agent-mcq`, also add the following argument to the end of `CMD`:
```sh
--ptype ntnu_inginious_multifill.MultifillProblem
```

## Activating

In your ``configuration.yaml`` file, add the following plugin entry:

```yaml
plugins:
  - plugin_module: 'ntnu_inginious_multifill'
```


