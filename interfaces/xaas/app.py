import logging.config

import os
from flask import Flask, Blueprint
from xaas import settings
from xaas.config import Config
from api.caas.posts import ns as posts_namespace
from api.caas.users import ns as users_namespace
from api.caas.comments import ns as comments_namespace
from api.caas.likes import ns as likes_namespace
from api.restplus import api

app = Flask(__name__)
logging_conf_path = '/Users/shashankjain/Desktop/yocket/interfaces/logging.conf'
print(logging_conf_path)
logging.config.fileConfig(logging_conf_path)
print(f'logging config path: {logging_conf_path}')
log = logging.getLogger(__name__)

def _get_bool_env(strEnv):

    if(strEnv is None):
        return False
    _t = str.upper(strEnv)
    if(_t == 'TRUE'):
        return True
    return False

def configure_app(flask_app):

    config = Config()

    url = config.FLASK_SERVER_URL
    port = config.API_PORT
    serverName = '{}:{}'.format(url, str(port))

    print(f'server name is {serverName}')

    RESTPLUS_VALIDATE = config.RESTPLUS_VALIDATE
    RESTPLUS_MASK_SWAGGER = config.RESTPLUS_VALIDATE
    RESTPLUS_ERROR_404_HELP = config.RESTPLUS_ERROR_404_HELP

    flask_app.config['SERVER_NAME'] = serverName
    flask_app.config['SWAGGER_UI_DOC_EXPANSION'] = config.RESTPLUS_SWAGGER_UI_DOC_EXPANSION
    flask_app.config['RESTPLUS_VALIDATE'] = RESTPLUS_VALIDATE
    flask_app.config['RESTPLUS_MASK_SWAGGER'] = RESTPLUS_MASK_SWAGGER
    flask_app.config['ERROR_404_HELP'] = RESTPLUS_ERROR_404_HELP

def initialize_app(flask_app):
    configure_app(flask_app)

    blueprint = Blueprint('api', __name__, url_prefix='/api')
    api.init_app(blueprint)
    api.add_namespace(posts_namespace)
    api.add_namespace(users_namespace)
    api.add_namespace(comments_namespace)
    api.add_namespace(likes_namespace)
    flask_app.register_blueprint(blueprint)


def main():
    config = Config()
    initialize_app(app)

    dbg = config.FLASK_DEBUG

    url = config.FLASK_SERVER_URL
    port = config.API_PORT
    serverName = '{}:{}'.format(url, str(port))

    log.info('>>>>> Starting development server at http://{}/api/ <<<<<'.format(serverName))
    app.run(debug=dbg, host="0.0.0.0", port=config.API_PORT)


if __name__ == "__main__":
    main()
