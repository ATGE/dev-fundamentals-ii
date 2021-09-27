import json
import os

DEFAULT_CONFIGURATION = dict(host='localhost', port='6739')

DEFAULT_CONFIG_FILE = './configuration.json'


def config_from_var(key, config_file=None):
    config_file = config_file if config_file else {}
    config_var = get_db_settings(**config_file).get(key)
    return config_var


def config_from_default(**kwargs):
    """Retrieve DB settings from default settings. """
    return DEFAULT_CONFIGURATION


def config_from_env(**kwargs):
    """Retrieve DB settings from environment settings. """
    return dict(host=os.environ.get('TRUCK_HOST'), port=os.environ.get('TRUCK_PORT'))


def config_from_file(config_file=None):
    """Returns a parsed config dict"""
    if config_file is None:
        config_file = DEFAULT_CONFIG_FILE
    config = {}
    try:
        with open(config_file, 'r') as file:
            data = file.read()
            config = json.loads(data)
    except FileNotFoundError as ex:
        print(ex.strerror)
    return config


SETTING_RESOLVERS = [
    config_from_env,
    config_from_file,
    config_from_default,
]


def get_db_settings(**kwargs):
    """Parse db settings.
    """
    all_settings = {}
    for setting_method in SETTING_RESOLVERS:
        settings = setting_method(**kwargs)
        if settings:
            settings.update((k, v) for k, v in all_settings.items() if v)
            all_settings = settings

    return all_settings
