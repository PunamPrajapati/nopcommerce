import configparser
import os

config = configparser.RawConfigParser()
config.read(".\\configurations\\config.ini")
# config_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'configurations', 'config.ini'))
# config.read(config_path)
class ReadConfig:
    @staticmethod
    def get_admin_page_url():
        url = config.get('admin login info', 'admin_page_url')
        return url

    @staticmethod
    def get_username():
        username = config.get('admin login info', 'username')
        return username

    @staticmethod
    def get_password():
        password = config.get('admin login info', 'password')
        return password

    @staticmethod
    def get_invalid_username():
        invalid_username = config.get('admin login info', 'invalid_username')
        return invalid_username