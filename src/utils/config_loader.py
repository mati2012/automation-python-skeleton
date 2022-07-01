import os


def read_config_file(section, key):
    from configparser import ConfigParser

    config_path = os.getenv('project_path') + '/config.ini'

    config = ConfigParser()
    config.read(config_path)

    value = config.get(section, key)

    if value.lower() == 'true':
        value = True
    elif value.lower() == 'false':
        value = False

    return value


def read_urls_in_config(key):
    return read_config_file('urls', key)
