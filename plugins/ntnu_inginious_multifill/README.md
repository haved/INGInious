INGInious plugin for multiple fill-ins
=====================================================

This plugin defines a new problem type named `multifill` 

## Installing

To make the plugin available in the docker containers, make sure both `deploy/frontend.containerfile` has the following lines, or something similar:

```sh
COPY plugins plugins
RUN pip3 install plugins/ntnu_inginious_multifill
pip3 install plugins/ntnu_inginious_multifill
```

We use a custom grading agent.
To the `docker-compose.yml`, add the following container definition:
``` yaml
  agent-multifill:
    depends_on:
      - backend
    deploy:
      replicas: 1
    build:
      dockerfile: plugins/ntnu_inginious_multifill/agent-multifill.containerfile
      args:
        - VERSION=${VERSION}
        - REGISTRY=${REGISTRY}
    environment:
      BACKEND: "tcp://backend:2001"
    volumes:
     # See https://github.com/INGInious/INGInious/issues/352
     - ./tasks/:/inginious/tasks
     - ./backups/:/inginious/backups
     # See https://github.com/INGInious/INGInious/issues/799
     - /tmp/agent_data/:/tmp/agent_data/
    networks:
      - inginious
      
  [...]
  
  frontend:
    [...]
    depends_on:
      [...]
      - agent-multifill
```

## Activating

In your ``configuration.yaml`` file, add the following plugin entry:

```yaml
plugins:
  - plugin_module: 'ntnu_inginious_multifill'
```

## Writing multifill exercises

Make sure you use the `Multifill Grader` grading environment.

## Development
This plugin is developed in a branch in the INGIniuous repository that has everything set up for development on [GitHub](https://github.com/haved/INGInious/tree/plugin-development).

### Updating translations
The multifill agent has translations of the messages it sends to users as feedback.

When the agent source code has changed, run the following from the repository root: 
```sh
pybabel extract -F plugins/ntnu_inginious_multifill/ntnu_inginious_multifill/agent/babel.cfg ./ -o plugins/ntnu_inginious_multifill/ntnu_inginious_multifill/agent/i18n/messages.pot

cd plugins/ntnu_inginious_multifill/ntnu_inginious_multifill/agent/i18n/

# Only first time
pybabel init -i messages.pot -o nb_NO/LC_MESSAGES/messages.po -l nb_NO

# Update po file for languages
pybabel update -i messages.pot -o nb_NO/LC_MESSAGES/messages.po -l nb_NO

# After writing norwegian translations in messages.po, compile into .mo file
pybabel compile -i nb_NO/LC_MESSAGES/messages.po -o nb_NO/LC_MESSAGES/messages.mo -l nb_NO
```


