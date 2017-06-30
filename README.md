# fnExchange Slack Plugin
This is a plugin for the fnExchange API router for interacting with Slack.

This plugin currently only provides an Action for posting messages to a Slack
channel using inbound webhooks. This only requires the inbound webhook URL token.

You can get the Slack webhook URL [here](https://my.slack.com/services/new/incoming-webhook/)

# Installation
Simply install this as
```
$ pip install fnexchange-slack
```

# Configuration
To use this plugin with fnExchange, add the appropriate configuration to the `fnexchange.yml`
configuration file under `plugins_enabled`. A sample configuration is provided below.
Of course, note that you can use any alias instead of "slacker".

The plugin **requires** the `url` configuration.

```yaml
...
  plugins_enabled:
    ...
    slacker:
      class_name: 'fnexchange_slack.SlackPlugin'
      config:
        url: 'https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX'
    ...
...
```
