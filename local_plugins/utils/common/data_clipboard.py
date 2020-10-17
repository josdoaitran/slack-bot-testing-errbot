import threading


from local_plugins.utils.common.data_key import DataKey



class Clipboard:
    __DATA_HOLDER__ = threading.local()

    @staticmethod
    def get(key):
        try:
            data_set = Clipboard.__DATA_HOLDER__
            value = data_set.__getattribute__(key)
            return value
        except (KeyError, AttributeError):
            return None

    @staticmethod
    def set(key, value):
        Clipboard.__DATA_HOLDER__.__setattr__(key, value)

    @staticmethod
    def clear():
        Clipboard.__DATA_HOLDER__.__dict__.clear()

