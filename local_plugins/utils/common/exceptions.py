COMMON_CONFIGURATION_ERROR_MESSAGE = 'We have an problem when read/write config file'


class ConfigurationError(Exception):
    pass


class BusinessException(Exception):
    pass


class AutomationException(Exception):
    pass


class AutomationSkipAbleException(Exception):
    pass


class AutomationNotImplementedException(Exception):
    def __init__(self):
        super().__init__('Test is not implemented yet. dreadbot need your support')
