import platform

class System:
    @staticmethod
    def get_os():
        return platform.system()

    @staticmethod
    def is_windows():
        return System.get_os() == "Windows"

    @staticmethod
    def is_mac():
        return System.get_os() == "Darwin"

    @staticmethod
    def is_linux():
        return System.get_os() == "Linux"
