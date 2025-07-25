import configparser
config = configparser.RawConfigParser()
config.read(".\\configurations\\config.ini")
#to ready the config file
class Read_Config:
    @staticmethod
    def get_admin_url():
       url = config.get('admin login info', 'admin_page_url')
       return url
    @staticmethod
    def get_admin_username():
        username = config.get('admin login info', 'username')
        return username
    @staticmethod
    def get_admin_password():
        password = config.get('admin login info', 'password')
        return password
    @staticmethod
    def get_invalid_user():
        invalid_username = config.get('admin login info', 'invalid_username')
        return invalid_username

