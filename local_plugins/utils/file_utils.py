import os
from pathlib import Path
from urllib import parse

import yaml

from local_plugins.utils.common.exceptions import ConfigurationError

def create_file(fileName, content):
    f = open(fileName + ".json", "w+")
    f.write(content)
    f.close()

def delete_file(fileName):
    os.remove(fileName)

def get_yaml_string_from_path(path):
    check_file_exist(path)
    with open(path, 'r') as stream:
        try:
            file_string = yaml.load(stream, Loader=yaml.FullLoader)
            return file_string

        except yaml.YAMLError as ex:
            print(ex.__cause__)


def get_value_from_yaml(path, key):
    file = get_yaml_string_from_path(path)
    value = file.get(key)
    if value is not None:
        return value
    else:
        raise ConfigurationError('An error when get_value_from_file by path: ' + path + ' and key: ' + key)


def check_file_exist(path):
    my_file = Path(path)
    if my_file.is_file() is False:
        raise ConfigurationError('Could not find your file in path %s. Please check and try again' % path)


def get_file_content_from_path(path):
    check_file_exist(path)
    with open(path, 'r') as stream:
        file_string = stream.read().split()
        last_index = len(file_string)
        first_item = file_string[0].replace('[', '')
        last_item = file_string[last_index - 1].replace(']', '')
        file_string[0] = first_item
        file_string[last_index - 1] = last_item
        values = []
        for i in range(last_index):
            t = int(file_string[i].replace(',', ''))
            values.append(t)
        return values


def get_code_from_url(url):
    return parse.parse_qs(parse.urlparse(url).query)['code'][0]


def create_folder_if_not_exist(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

