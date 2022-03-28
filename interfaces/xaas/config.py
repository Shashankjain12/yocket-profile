import os
import configparser

class Config:
    MONGO_URL = 'localhost'
    API_PORT = 8888
    FLASK_DEBUG = True
    RESTPLUS_SWAGGER_UI_DOC_EXPANSION = 'list'
    RESTPLUS_VALIDATE = True
    RESTPLUS_MASK_SWAGGER = False
    RESTPLUS_ERROR_404_HELP = False
    MONGO_PORT = 27017
    LOG_LEVEL = 'INFO'
    LOG_FILE_DIR = 'api.log'
    
    def __init__(self):
        print('in config init')
        self.MONGO_URL = os.environ.get('MONGO_URL') or self.MONGO_URL
        self.FLASK_SERVER_URL = os.environ.get('FLASK_SERVER_URL', '127.0.0.1')
        self.API_PORT = int(os.environ.get('API_PORT')) if os.environ.get('API_PORT') is not None else self.API_PORT
        self.FLASK_DEBUG = self.get_bool_env(os.environ.get('FLASK_DEBUG')) or self.FLASK_DEBUG
        self.RESTPLUS_SWAGGER_UI_DOC_EXPANSION = os.environ.get('RESTPLUS_SWAGGER_UI_DOC_EXPANSION') or self.RESTPLUS_SWAGGER_UI_DOC_EXPANSION
        self.RESTPLUS_MASK_SWAGGER = self.get_bool_env(os.environ.get('RESTPLUS_MASK_SWAGGER')) or self.RESTPLUS_MASK_SWAGGER
        self.RESTPLUS_VALIDATE = self.get_bool_env(os.environ.get('RESTPLUS_VALIDATE')) or self.RESTPLUS_VALIDATE
        self.RESTPLUS_ERROR_404_HELP = self.get_bool_env(os.environ.get('RESTPLUS_ERROR_404_HELP')) or self.RESTPLUS_ERROR_404_HELP
        self.LOG_FILE_DIR = os.environ.get('LOG_FILE_DIR') or self.LOG_FILE_DIR
        
    def get_bool_env(self, strEnv):
        if(strEnv is None):
            return False
        _t = str.upper(strEnv)
        if(_t == 'TRUE'):
            return True
        return False
