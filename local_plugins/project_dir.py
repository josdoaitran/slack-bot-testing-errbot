import os


class ProjectDir:

    @staticmethod
    def get_project_dir():
        return os.path.dirname(os.path.abspath(__file__))
