import logging
import traceback

from flask_restx import Api
from xaas import settings

log = logging.getLogger(__name__)

api = Api(version='1.0', title="Posts API",
          description='Api for creation of posts and liking, commenting on the posts')


@api.errorhandler
def default_error_handler(e):
    message = 'An unhandled exception occurred.'
    log.exception(message)

    if not settings.FLASK_DEBUG:
        return {'message': message}, 500
