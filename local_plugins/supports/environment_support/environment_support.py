import os
import configparser

from local_plugins.project_dir import ProjectDir


class EnvironmentSupport:

    @staticmethod
    def get_value_environment(key):
        environment = ''
        key_environment = ''
        env = os.environ['app_env']
        if env == 'stg':
            key_environment = 'STG'
            environment = '/err/local_plugins/supports/environment_support/stg.env'
        if env == 'test':
            key_environment = 'TEST'
            environment = '/err/local_plugins/supports/environment_support/test.env'
        if env == 'local':
            key_environment = 'LOCAL'
            PROJECT_DIR = ProjectDir.get_project_dir()
            environment = PROJECT_DIR + '/supports/environment_support/local.env'

        config = configparser.ConfigParser()
        config.read(environment)
        data = config.get(key_environment, key)
        return data

# print (EnvironmentSupport.get_value_environment('lending_db_host'))
