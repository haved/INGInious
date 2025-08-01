INGInious plugin for multiple fill-ins
=====================================================

This plugins define a new problem type named `multifill` 

## Installing

```sh
pip3 install <path to this repo>
```

You likely want to add the above line to `deploy/frontend.containerfile`

## Activating

In your ``configuration.yaml`` file, add the following plugin entry:

```yaml
plugins:
  - plugin_module: 'ntnu_inginious_multifill'
```


